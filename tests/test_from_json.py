import unittest

import ibm_jsonx


class TestFromJson(unittest.TestCase):
    def setUp(self):
        self.data = ibm_jsonx.file_to_jsonx("tests/test.json")

    def test_root_element_is_object(self):
        self.assertTrue(
            self.data.startswith('<?xml version="1.0" encoding="UTF-8"?><json:object')
        )

    def test_string_with_name_name(self):
        print(self.data)
        self.assertIn('<json:string name="name"', self.data)

    def test_string_special_with_name_ficoScore(self):
        self.assertIn('<json:string name="ficoScore"', self.data)

    @unittest.skip("missing impl")
    def test_string_special_value_with_name_ficoScore(self):
        self.assertIn('<json:string name="ficoScore"> > 640</json:string>', self.data)

    def test_dict_with_name_address(self):
        self.assertIn('<json:object name="address"', self.data)

    @unittest.skip("need to think about this")
    def test_dict_address_postalCode_should_be_number(self):
        pass

    def test_list_with_name_phoneNumbers(self):
        self.assertIn('<json:array name="phoneNumbers"', self.data)

    @unittest.skip("need to think about this")
    def test_list_phoneNumbers_items_should_all_be_strings(self):
        pass

    def test_null_with_name_additionalInfo(self):
        self.assertIn('<json:null name="additionalInfo" />', self.data)

    def test_bool_with_name_remote(self):
        self.assertIn('<json:boolean name="remote"', self.data)

    def test_float_with_name_height(self):
        self.assertIn('<json:number name="height"', self.data)
