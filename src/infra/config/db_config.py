from sqlalchemy import create_engine

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