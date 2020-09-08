import cherrypy
from src.gift_exchange_app import GiftExchangeApp

cherrypy.quickstart(GiftExchangeApp())
