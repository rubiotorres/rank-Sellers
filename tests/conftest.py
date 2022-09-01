import os
import sys
from unittest import mock
from unittest.mock import MagicMock, patch

import pytest as pytest

from src.factory.mysql_conn import MysqlConn

os.environ['IS_TEST'] = "1"


@pytest.fixture(scope="session", autouse=True)
def default_session_fixture(request):
    """
    :type request: _pytest.python.SubRequest
    :return:
    """
    with patch('src.factory.mysql_conn.MysqlConn.connect'):
        yield
