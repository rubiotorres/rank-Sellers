from unittest import mock, TestCase
from unittest.mock import MagicMock, call

from src.factory.mysql_conn import MysqlConn
from src.model.sales import Sales
from src.model.seller import Seller
from src.service.service_sales import ServiceSales
from src.service.service_sellers import ServiceSellers


class TestSalesService(TestCase):
    @mock.patch.object(MysqlConn, "create_table", return_value=None)
    def setUp(self, mock_create_table):
        self.service_sellers = ServiceSellers()
        self.service = ServiceSales(self.service_sellers)

    @mock.patch.object(MysqlConn, "add_element", return_value=MagicMock())
    def test_register_sales(self, mock_add_element):
        self.service.register_sales({"seller_id": 1, "customerName": "louis", "product_id": 2, "amount": 2})
        self.assertEqual(mock_add_element.call_count, 1)

    @mock.patch.object(MysqlConn, "find_all",
                       return_value=[Sales({"seller_id": 1, "customerName": "louis", "product_id": 2, "amount": 2}),
                                     Sales({"seller_id": 1, "customerName": "louis", "product_id": 2, "amount": 1})])
    @mock.patch.object(ServiceSellers, "get_sellers", return_value=[Seller({"id": 1, "name": "teste_2", "amount": 1}),
                                                                    Seller({"id": 2, "name": "teste_1", "amount": 2})])
    def test_get_sales(self, mock_get_sellers, mock_find_all):
        sales = self.service.get_sales()

        self.assertEqual(list(sales.keys())[0], 1)
        self.assertEqual(len(sales.keys()), 2)

    @mock.patch.object(MysqlConn, "delete_row", return_value=MagicMock())
    def test_delete_sale(self, mock_delete_row):
        self.service.delete_sale(2)
        self.assertEqual(mock_delete_row.call_args, call(Sales, 'id', 2))

    @mock.patch.object(MysqlConn, "find_filter", return_value=MagicMock())
    def test_get_sale_by_id(self, mock_get_sale_by_id):
        self.service.get_sale_by_id(2)
        self.assertEqual(mock_get_sale_by_id.call_args, call(Sales, 'id', 2))
