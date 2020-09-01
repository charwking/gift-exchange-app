import cherrypy
from cherrypy.test import helper
from src import app, templates


class MainTest(helper.CPWebCase):
    @staticmethod
    def setup_server():
        cherrypy.tree.mount(app.GiftExchangeApp())

    def test_index_is_hello_world(self):
        self.getPage("/")
        self.assertStatus("200 OK")
        expectedUsers = [
            {"id": 1, "name": "Pat"},
            {"id": 2, "name": "Sam"},
            {"id": 3, "name": "Alex"},
            {"id": 4, "name": "Lee"},
            {"id": 5, "name": "Taylor"},
        ]
        expectedBody = templates.render("index.html", {"users": expectedUsers})
        self.assertBody(expectedBody)

    def test_ping_is_pong(self):
        self.getPage("/ping")
        self.assertStatus("200 OK")
        self.assertBody("pong")
