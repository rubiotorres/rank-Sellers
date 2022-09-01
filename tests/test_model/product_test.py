import unittest

from src.model.seller import Seller


class TestProductModel(unittest.TestCase):
    KWARGS = {
        'id': 0,
        'name': "Test_1",
        'sales': 2,
    }

    def test_dict_model(self):
        model = Seller(self.KWARGS)
        model_dict = model.get_dict_model()
        model_dict.pop('_sa_instance_state')
        assert self.KWARGS == model_dict
