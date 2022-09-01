from abc import ABC, abstractmethod

from src.factory.db_config import DbConfig


class DbConnection(ABC):

    @abstractmethod
    def connect(self, config: DbConfig):  # pragma: no cover
        """
        Retorna a conexão com o banco de dados

        :param `config`: configuração de banco de dados
        """
        pass

    @abstractmethod
    def close(self):  # pragma: no cover
        """
        Fecha a conexão com o banco de dados
        """
        pass

    @abstractmethod
    def execute_query(self, query: str):  # pragma: no cover
        """
        Executa a query
        """
        pass

    @abstractmethod
    def execute_update(self, update: str):  # pragma: no cover
        """
        Executa o upadate
        """
        pass

    @abstractmethod
    def execute_update_commit(self, update: str):  # pragma: no cover
        """
        Executa o upadate e faz o commit da transação
        """
        pass
