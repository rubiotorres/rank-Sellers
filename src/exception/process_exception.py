class ProcessSystemException(Exception):  # pragma: no cover
    """
    Exceção lançada em situações de erros de sistema tratados.
    """

    def __init__(self, message=None):
        self.__message = message

    @property
    def message(self):
        return self.__message
