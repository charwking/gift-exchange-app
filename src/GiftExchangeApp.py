import cherrypy
import os
from src.db import Db
from src.models.User import User
from src.templates import render

cherrypy.config.update(
    {
        "environment": os.environ.get("ENVIRONMENT"),
        "server.socket_port": int(os.environ.get("SERVER_PORT", 5050)),
    }
)

Db.init()


class GiftExchangeApp:
    @cherrypy.expose
    def index(self):
        users = Db.session.query(User).all()
        return render("index.html", {"users": users})

    @cherrypy.expose
    def ping(self):
        return "pong"
