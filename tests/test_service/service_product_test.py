from unittest import mock, TestCase
from unittest.mock import MagicMock, call

from src.factory.mysql_conn import MysqlConn
from src.model.product import Product
from src.service.service_product import ServiceProduct


class TestSalesService(TestCase):
    @mock.patch.object(MysqlConn, "create_table", return_value=None)
    def setUp(self, mock_create_table):
        self.service = ServiceProduct()

    @mock.patch.object(MysqlConn, "find_filter", return_value=MagicMock())
    def test_is_seller_already_registered(self, mock_filter_conn):
        self.service.is_seller_already_registered({"name": "test_1"})
        self.assertEqual(mock_filter_conn.call_args, call(Product, 'name', 'test_1'))

    @mock.patch.object(MysqlConn, "add_element", return_value=MagicMock())
    @mock.patch.object(ServiceProduct, "is_seller_already_registered", return_value=MagicMock())
    def test_register_product_exist(self, mock_seller, mock_add_element):
        response = self.service.register_product({"name": 1, "price": 2})
        self.assertIsInstance(response, MagicMock)

    @mock.patch.object(MysqlConn, "add_element", return_value=MagicMock())
    @mock.patch.object(ServiceProduct, "is_seller_already_registered", return_value=None)
    def test_register_product_no_exist(self, mock_seller, mock_add_element):
        response = self.service.register_product({"name": 1, "price": 2})
        self.assertIsInstance(response, Product)

    @mock.patch.object(MysqlConn, "find_all", return_value=[Product({"name": 1, "price": 2})])
    def test_is_seller_get_product(self, mock_find_all):
        self.service.get_product()
        self.assertEqual(mock_find_all.call_args, call(Product))
