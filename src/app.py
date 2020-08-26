import cherrypy

class GiftExchangeApp():

   @cherrypy.expose
   def index(self):
      return 'Hello world!'

   @cherrypy.expose
   def ping(self):
      return 'pong'

if __name__ == '__main__':
   cherrypy.quickstart(GiftExchangeApp())
