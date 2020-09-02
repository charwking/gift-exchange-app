import cherrypy
from cherrypy.test import helper

from src.GiftExchangeApp import GiftExchangeApp
from src.db import Db
from src.models.User import User
from src.templates import render


class GiftExchangeAppTest(helper.CPWebCase):
    @staticmethod
    def setup_server():
        cherrypy.tree.mount(GiftExchangeApp())

    def test_index_is_hello_world(self):
        expectedUsers = [
            {"name": "Pat"},
            {"name": "Sam"},
            {"name": "Alex"},
            {"name": "Lee"},
            {"name": "Taylor"},
        ]

        Db.session.query(User).delete()
        for user in expectedUsers:
            Db.session.add(User(name=user["name"]))
        Db.session.commit()

        self.getPage("/")
        self.assertStatus("200 OK")
        expectedBody = render("index.html", {"users": expectedUsers})
        self.assertBody(expectedBody)

    def test_ping_is_pong(self):
        self.getPage("/ping")
        self.assertStatus("200 OK")
        self.assertBody("pong")
