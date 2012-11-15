import unittest
import transaction

from pyramid import testing

from .models import DBSession

class TestMyView(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()
        from sqlalchemy import create_engine
        engine = create_engine('sqlite://')
        from .models import (
            Base,
            MyModel,
            )
        DBSession.configure(bind=engine)
        Base.metadata.create_all(engine)
        with transaction.manager:
            model = MyModel(name='one', value=55)
            DBSession.add(model)

    def tearDown(self):
        DBSession.remove()
        testing.tearDown()

    def test_it(self):
        from .views import my_view
        request = testing.DummyRequest()
        info = my_view(request)
        self.assertEqual(info['one'].name, 'one')
        self.assertEqual(info['project'], 'app')

class FunctionalTests(unittest.TestCase):
    import os
    from paste.deploy.loadwsgi import appconfig
    here = os.path.dirname(__file__)
    settings = appconfig('config:' + os.path.join(here, '../', 'development.ini'))

    def setUp(self):
        print self.settings
        settings = {
            'sqlalchemy.url':'sqlite:///home/home/python/prod/busbeep/app/app.sqlite'
        }
        from app import main
        #the_app = main({'wrong':'sad face'}, settings={'sqlalchemy.url':'hi there'})
        #the_app = main({}, **self.settings)
        the_app = main({}, **settings)
        from webtest import TestApp
        self.testapp = TestApp(the_app)

    def test_root(self):
        assert True

