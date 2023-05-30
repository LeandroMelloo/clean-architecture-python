from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

class DBConnectionHandler:
    """ Sqlalchemy connection database """

    # __init__ -> construtor
    def __init__(self):
        # __connection_string -> atributo privado
        self.__connection_string = "sqlite:///storage.db"
        self.session = None

    def get_engine(self):
        """ 
            Return connection Engine 
            :param - None
            :param - engine connection to Database
        """
        engine = create_engine(self.__connection_string)
        return engine
    
    def __enter__(self):
        engine = create_engine(self.__connection_string)
        session_maker = sessionmaker()
        self.session = session_maker(bind=engine)
        return self
    
    def __exit__(self, exc_type, exc_value, exc_tb):
        self.session.close()