from pathlib import Path
import unittest

import ibm_jsonx


class TestFromJson(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.data = ibm_jsonx.to_jsonx(Path("tests/test.json"))

    def test_root_element_is_object(self):
        self.assertTrue(
            self.data.startswith('<?xml version="1.0" encoding="UTF-8"?><json:object')
        )

    def test_string_with_name_name(self):
        self.assertIn('<json:string name="name"', self.data)

    def test_string_special_with_name_ficoScore(self):
        self.assertIn('<json:string name="ficoScore"', self.data)

    def test_string_special_ampersand_is_entity(self):
        self.assertIn('<json:string name="&amp;">&amp;</json:string>', self.data)

    def test_dict_with_name_address(self):
        self.assertIn('<json:object name="address"', self.data)

    def test_list_with_name_phoneNumbers(self):
        self.assertIn('<json:array name="phoneNumbers"', self.data)

    def test_null_with_name_additionalInfo(self):
        self.assertIn('<json:null name="additionalInfo" />', self.data)

    def test_bool_with_name_remote(self):
        self.assertIn('<json:boolean name="remote"', self.data)

    def test_float_with_name_height(self):
        self.assertIn('<json:number name="height"', self.data)
