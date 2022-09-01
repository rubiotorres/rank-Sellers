from unittest import mock, TestCase
from unittest.mock import MagicMock, call

from src.factory.mysql_conn import MysqlConn
from src.model.seller import Seller
from src.service.service_sellers import ServiceSellers


class TestSellerService(TestCase):
    @mock.patch.object(MysqlConn, "create_table", return_value=None)
    def setUp(self, mock_create_table):
        self.service = ServiceSellers()

    @mock.patch.object(MysqlConn, "find_filter", return_value=MagicMock())
    def test_is_seller_already_registered(self, mock_filter_conn):
        self.service.is_seller_already_registered({"name": "test_1"})
        self.assertEqual(mock_filter_conn.call_args, call(Seller, 'name', 'test_1'))

    @mock.patch.object(MysqlConn, "count_rows", return_value=6)
    def test_has_less_than_five_vendors_denied(self, mock_count_rows):
        response = self.service.has_less_than_five_vendors()
        self.assertTrue(response)
        self.assertEqual(mock_count_rows.call_args, call(Seller))

    @mock.patch.object(MysqlConn, "count_rows", return_value=4)
    def test_has_less_than_five_vendors_accept(self, mock_count_rows):
        response = self.service.has_less_than_five_vendors()
        self.assertFalse(response)
        self.assertEqual(mock_count_rows.call_args, call(Seller))

    @mock.patch.object(MysqlConn, "add_element", return_value=MagicMock())
    def test_register_sellers(self, mock_add_element):
        response = self.service.register_sellers({"name": 1})
        self.assertEqual(str(response), 'id: None | Name: 1 | Sales: None')

    @mock.patch.object(MysqlConn, "find_all_desc", return_value=MagicMock())
    def test_get_sellers(self, mock_find_all_desc):
        self.service.get_sellers()
        self.assertEqual(mock_find_all_desc.call_count, 1)

    @mock.patch.object(MysqlConn, "update_element_seller", return_value=MagicMock())
    def test_update_sellers(self, mock_update_element_seller):
        new_seller = Seller({"name": 1})
        self.service.update_sellers(new_seller, 2)
        self.assertEqual(mock_update_element_seller.call_count, 1)

    @mock.patch.object(MysqlConn, "find_filter", return_value=MagicMock())
    def test_get_seller_by_id(self, mock_filter_conn):
        self.service.get_seller_by_id(2)
        self.assertEqual(mock_filter_conn.call_args, call(Seller, 'id', 2))
