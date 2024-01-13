#!/usr/bin/python3
import unittest
from models.base_model import BaseModel
"""test BaseModel"""

class test_basemodel(unittest.TestCase):
    def test_initialisation(self):
        m = BaseModel()
        self.assertIsNotNone(m.id)
        self.assertIsNotNone(m.updated_at)
        self.assertIsNotNone(m.created_at)
    
    def test_unique_id(self):
        b1 = BaseModel()
        b2 = BaseModel()
        self.assertNotEqual(b1.id, b2.id)
    
    def test_to_dict(self):
        bm = BaseModel()
        self.assertTrue(dict, type(bm.to_dict()))
        self.assertIn("id", bm.to_dict())
        self.assertIn("created_at", bm.to_dict())
        self.assertIn("updated_at", bm.to_dict())
        self.assertIn("__class__", bm.to_dict())
    
    def test_save(self):
        m = BaseModel()





if __name__ == "__main__":
    unittest.main()
