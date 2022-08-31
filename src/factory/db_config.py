from abc import ABC, abstractmethod

from src.exception.process_exception import ProcessSystemException


class DbConfig(ABC):  # pragma: no cover
    """
    Estrutura base para configurações de banco de dados
    """

    def __init__(self, user, password, host, database, port, connection_string):

        self.__user = user
        self.__password = password
        self.__host = host
        self.__database = database
        self.__port = int(port)
        self.__connection_string = connection_string

        self.__validate_configuration()

    @property
    def user(self):
        """
        Recupera a configuração de usuário do banco de dados
        """
        return self.__user

    @property
    def password(self):
        """
        Recupera a configuração de senha do banco de dados
        """
        return self.__password

    @property
    def host(self):
        """
        Recupera a configuração do host do banco de dados
        """
        return self.__host

    @property
    def database(self):
        """
        Recupera a configuração do nome do banco de dados
        """
        return self.__database

    @property
    def port(self):
        """
        Recupera a configuração da porta do banco de dados
        """
        return self.__port

    @property
    def connection_string(self):
        """
        Recupera a configuração da porta do banco de dados
        """
        return self.__connection_string

    def __validate_configuration(self):
        """
        Valida a configuração do banco de dados
        """
        if (not self.__connection_parameters_is_valid()) and (not self.__connection_string_is_valid()):
            raise ProcessSystemException(self.get_error_message())

    def __connection_parameters_is_valid(self):
        """
        Valida a configuração do banco de dados para os parâmetros
        """

        if self.user and self.password and self.host and self.database and self.port:
            return True

        return False

    def __connection_string_is_valid(self):
        """
        Valida a configuração do banco de dados para connection string
        """
        if self.__connection_string:
            return True

        return False

    @abstractmethod
    def get_error_message(self):  # pragma: no cover
        """
        Retorna mensagem de erro para configuração do banco de dados
        """
        pass
