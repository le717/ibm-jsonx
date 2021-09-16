import unittest

import ibm_jsonx


class TestFromJson(unittest.TestCase):
    def setUp(self):
        self.data = ibm_jsonx.file_to_jsonx("tests/test.json")

    def test_string_with_name_name(self):
        print(self.data)
        # self.assertEqual(self.data)

    def test_string_special_with_name_ficoScore(self):
        pass

    def test_dict_with_name_address(self):
        pass

    def test_dict_address_postalCode_should_be_number(self):
        pass

    def test_list_with_name_phoneNumbers(self):
        pass

    def test_list_phoneNumbers_items_should_all_be_strings(self):
        pass

    def test_null_with_name_additionalInfo(self):
        pass

    def test_bool_with_name_remote(self):
        pass

    def test_float_with_name_height(self):
        pass
