import unittest
from datetime import datetime

from src.model.sales import Sales


class TestSalesModel(unittest.TestCase):
    KWARGS = {
        'id': 0,
        'seller_id': "Test_1",
        'customer_name': "Customer_test",
        'date_sale': datetime.now().strftime("%d/%m/%Y %H:%M:%S"),
        'product_id': 2,
        'amount': 2,
    }

    def test_dict_model(self):
        model = Sales(self.KWARGS)
        model_dict = model.get_dict_model()
        model_dict.pop('_sa_instance_state')
        assert self.KWARGS == model_dict
