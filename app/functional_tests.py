from tests import TestMyView

class FunctionalTests(TestMyView):
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
