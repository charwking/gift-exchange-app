import sqlalchemy
import src.models

from os import environ
from sqlalchemy.ext.declarative import declarative_base
from src.models.BaseModel import BaseModel


class Db:

    engine = None
    session = None

    @staticmethod
    def init():
        Db.__init_engine()
        Db.__init_models()
        Db.__init_session()

    @staticmethod
    def __init_engine():
        connection_string = (
            "mysql+mysqlconnector://"
            f"{environ.get('DB_USER')}:"
            f"{environ.get('DB_PASS')}@"
            f"{environ.get('DB_HOST')}:"
            f"{environ.get('DB_PORT')}/"
            f"{environ.get('DB_NAME')}"
        )
        echo_sql = environ.get("DB_ECHO_SQL") == "true"

        Db.engine = sqlalchemy.create_engine(connection_string, echo=echo_sql)

    @staticmethod
    def __init_models():
        BaseModel.metadata.create_all(Db.engine)

    @staticmethod
    def __init_session():
        Session = sqlalchemy.orm.sessionmaker()
        Session.configure(bind=Db.engine)
        Db.session = Session()
