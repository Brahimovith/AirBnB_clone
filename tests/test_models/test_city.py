#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
from models.city import City
from datetime import datetime
from time import sleep
"""test City"""
class Testcity(unittest.TestCase):
    def test_initialisation(self):
        m = City()
        City.name = "brahim"
        City.state_id = 123

        self.assertEqual(City.name, "brahim", "valeur erronee")
        self.assertEqual(City.state_id, 123, "valeur erronee")
        

    def test_type(self):
        self.assertEqual(City, type(City()))
    
    def test_id_differnet(self):
        a = City()
        b = City()
        self.assertNotEqual(a.id, b.id)
    
    def test_str_rep(self):
        a = City()
        a.id = "12345"
        dd = datetime.now()
        a.created_at = a.updated_at = dd
        dd = repr(dd)
        ch = a.__str__()
        self.assertIn("[City] (12345)", ch)
        self.assertIn("'created_at': "+dd, ch)
        self.assertIn("'updated_at': "+dd, ch)
        self.assertIn("'id': '12345'", ch)
    
    def test_different_date(self):
        a = City()
        sleep(0.09)
        b = City()
        self.assertLess(a.created_at, b.created_at)
        self.assertLess(a.updated_at, b.updated_at)

    def test_todict(self):
        u = City()
        dic = u.to_dict()
        self.assertEqual(str, type(dic["id"]))
        self.assertEqual(str, type(dic["updated_at"]))
        self.assertEqual(str, type(dic["created_at"]))

    def test_to_dict(self):
        bm = City()
        self.assertTrue(dict, type(bm.to_dict()))
        self.assertIn("id", bm.to_dict())
        self.assertIn("created_at", bm.to_dict())
        self.assertIn("updated_at", bm.to_dict())
        self.assertIn("__class__", bm.to_dict())

    
if __name__ == "__main__":
    unittest.main()
