import unittest
import transaction

from pyramid import testing

def _initDb():
    from sqlalchemy import create_engine
    engine = create_engine('sqlite://')
    from .models import (
        DBSession,
        Base,
        MyModel,
        )
    DBSession.configure(bind=engine)
    Base.metadata.create_all(engine)
    with transaction.manager:
        model = MyModel(name='one', value=55)
        DBSession.add(model)
    return DBSession

def _registerRoutes(config):
    config.add_route("transmitter","/transmitter/{t_num}")


class ViewWikiTests(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()

    def tearDown(self):
        testing.tearDown()

    def _callFUT(self, request):
        from .views import my_view
        return my_view(request)

    def test_it(self):
        _registerRoutes(self.config)
        request = testing.DummyRequest()
        response = self._callFUT(request)
        self.assertEqual(response['one'].name, 'one')

    def test_transmitter(self):
        from .views import my_transmitter

        request = testing.DummyRequest()
        response = my_transmitter(request)
        self.assertEqual(response['hmm'], 'testing confusion')




class TestMyView(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()
        self.session = _initDb()

    def tearDown(self):
        self.session.remove()
        testing.tearDown()

    def test_it(self):
        from .views import my_view
        request = testing.DummyRequest()
        info = my_view(request)
        self.assertEqual(info['one'].name, 'one')
        self.assertEqual(info['project'], 'app')

#    def test_transmitter_url(self):
#        from .views import  my_view
#        request = testing.DummyRequest()
#        info = my_view(request)


class FunctionalTests(unittest.TestCase):
    import os
    from paste.deploy.loadwsgi import appconfig
    here = os.path.dirname(__file__)
    settings = appconfig('config:' + os.path.join(here, '../', 'development.ini'))

    def setUp(self):
        from app import main
        the_app = main({}, **self.settings)
        from webtest import TestApp
        self.testapp = TestApp(the_app)

    def test_root(self):
        assert True
