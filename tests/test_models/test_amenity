#!/usr/bin/python3
import unittest
from datetime import datetime
from models.base_model import BaseModel
from models.amenity import Amenity
from time import sleep
"""test Amenity"""

class Testamenity(unittest.TestCase):
    def test_initialisation(self):
        m = Amenity()
        Amenity.name = "brahim"
        self.assertEqual(Amenity.name, "brahim", "valeur erronee")
        

    def test_type(self):
        self.assertEqual(Amenity, type(Amenity()))
    
    def test_id_differnet(self):
        a = Amenity()
        b = Amenity()
        self.assertNotEqual(a.id, b.id)
    
    def test_str_rep(self):
        a = Amenity()
        a.id = "12345"
        dd = datetime.now()
        a.created_at = a.updated_at = dd
        dd = repr(dd)
        ch = a.__str__()
        self.assertIn("[Amenity] (12345)", ch)
        self.assertIn("'created_at': "+dd, ch)
        self.assertIn("'updated_at': "+dd, ch)
        self.assertIn("'id': '12345'", ch)
    
    def test_different_date(self):
        a = Amenity()
        sleep(0.09)
        b = Amenity()
        self.assertLess(a.created_at, b.created_at)
        self.assertLess(a.updated_at, b.updated_at)
    
    def test_todictstr(self):
        u = Amenity()
        dic = u.to_dict()
        self.assertEqual(str, type(dic["id"]))
        self.assertEqual(str, type(dic["updated_at"]))
        self.assertEqual(str, type(dic["created_at"]))

    def test_to_dict(self):
        bm = Amenity()
        self.assertTrue(dict, type(bm.to_dict()))
        self.assertIn("id", bm.to_dict())
        self.assertIn("created_at", bm.to_dict())
        self.assertIn("updated_at", bm.to_dict())
        self.assertIn("__class__", bm.to_dict())

if __name__ == "__main__":
    unittest.main()
