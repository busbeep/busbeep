import unittest
import transaction

from pyramid import testing

from .models import DBSession

def _initDb():
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
    return DBSession

class TestMyView(unittest.TestCase):
    def setUp(self):
        self.config = testing.setUp()
        self.session = _initDb()

    def tearDown(self):
        DBSession.remove()
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
        

