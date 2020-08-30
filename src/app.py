import cherrypy
import os

cherrypy.config.update(
    {
        "environment": os.environ.get("ENVIRONMENT"),
        "server.socket_port": int(os.environ.get("SERVER_PORT", 5050)),
    }
)


class GiftExchangeApp:
    @cherrypy.expose
    def index(self):
        return "Hello world!"

    @cherrypy.expose
    def ping(self):
        return "pong"


if __name__ == "__main__":
    cherrypy.quickstart(GiftExchangeApp())
