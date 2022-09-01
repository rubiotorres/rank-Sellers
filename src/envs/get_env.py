import json
import os

from src.exception.process_exception import ProcessSystemException


def get_env_value(env_name, default_value=None, env_type="str"):
    """
        Método responsável por retornar o valor da variável de
        ambiente informada no parâmetro env_name.
    """
    converter = {
        "int": int,
        "json": json.loads,
        "str": str
    }[env_type]

    env_value = os.getenv(env_name, default_value)

    try:
        return converter(env_value)
    except Exception:
        raise ProcessSystemException(
            f"Ocorreu um erro ao converter a variável de ambiente {env_name} com valor {env_value} para {env_type}.")
