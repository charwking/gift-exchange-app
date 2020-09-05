import cherrypy
import os
from src import templates

cherrypy.config.update(
    {
        "environment": os.environ.get("ENVIRONMENT"),
        "server.socket_port": int(os.environ.get("SERVER_PORT", 5050)),
    }
)


class GiftExchangeApp:
    @cherrypy.expose
    def index(self):
        users = [
            {"id": 1, "name": "Pat"},
            {"id": 2, "name": "Sam"},
            {"id": 3, "name": "Alex"},
            {"id": 4, "name": "Lee"},
            {"id": 5, "name": "Taylor"},
        ]
        return templates.render("index.html", {"users": users})

    @cherrypy.expose
    def ping(self):
        return "pong"


if __name__ == "__main__":
    cherrypy.quickstart(GiftExchangeApp())
