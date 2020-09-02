import cherrypy
from src.GiftExchangeApp import GiftExchangeApp

cherrypy.quickstart(GiftExchangeApp())
