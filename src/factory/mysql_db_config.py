from src.envs.environment_variable import DB_USER, DB_PASSWORD, DB_HOST, DB_DATABASE, DB_PORT, \
    DB_CONN_STRING, DB_CHARSET, DB_CONN_TIMEOUT_SEC

from src.factory.db_config import DbConfig


class MysqlDbConfig(DbConfig):
    """
    Classe que implementa a interface SupplyDbConfig, com a configuração para o banco ml_v2 
    """
    DB_USER = DB_USER
    DB_PASSWORD = DB_PASSWORD
    DB_HOST = DB_HOST
    DB_DATABASE = DB_DATABASE
    DB_PORT = DB_PORT
    DB_CONN_STRING = DB_CONN_STRING
    DB_CHARSET = DB_CHARSET
    DB_CONN_TIMEOUT_SEC = DB_CONN_TIMEOUT_SEC

    def __init__(self):
        super().__init__(
            self.DB_USER,
            self.DB_PASSWORD,
            self.DB_HOST,
            self.DB_DATABASE,
            self.DB_PORT,
            self.DB_CONN_STRING,
        )

    def get_error_message(self):
        return "[Erro ao conectar no banco] Erro na configuração de conexão com o mlv2. Por favor, forneça os " \
               "parâmetros ou string de conexão "
