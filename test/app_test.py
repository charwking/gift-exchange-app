import cherrypy
from cherrypy.test import helper
from src import app


class MainTest(helper.CPWebCase):
    @staticmethod
    def setup_server():
        cherrypy.tree.mount(app.GiftExchangeApp())

    def test_index_is_hello_world(self):
        self.getPage("/")
        self.assertStatus("200 OK")
        self.assertBody("Hello world!")

    def test_ping_is_pong(self):
        self.getPage("/ping")
        self.assertStatus("200 OK")
        self.assertBody("pong")
