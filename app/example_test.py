import unittest

from tests import TestMyView

from pyramid import testing

class ViewIntegrationTests(TestMyView):
    def setUp(self):
        """ This sets up the application registry with the
        registrations your application declares in its ``includeme``
        function.
        """
        import app
        self.config = testing.setUp()
       #self.config.include('app')

    def tearDown(self):
        """ Clear out the application registry """
        testing.tearDown()

    #def test_my_view(self):
    #    from app.views import my_view
    #    request = testing.DummyRequest()
    #    result = my_view(request)
    #   #self.assertEqual(result.status, '200 OK')
    #    body = result.app_iter[0]
    #    self.failUnless('Welcome to' in body)
    #    self.assertEqual(len(result.headerlist), 2)
    #    self.assertEqual(result.headerlist[0],
    #                     ('Content-Type', 'text/html; charset=UTF-8'))
    #    self.assertEqual(result.headerlist[1], ('Content-Length',
    #                                            str(len(body))))

