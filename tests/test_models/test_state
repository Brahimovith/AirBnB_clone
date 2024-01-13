#!/usr/bin/python3
import unittest
from models.state import State
from datetime import datetime
from time import sleep
"""test State"""

class Testamenity(unittest.TestCase):
    def test_initialisation(self):
        m = State()
        State.name = "brahim"
        State.state_id = 123
        self.assertEqual(State.name, "brahim", "valeur erronee")
        self.assertEqual(State.state_id, 123, "valeur erronee")
        

    def test_type(self):
        self.assertEqual(State, type(State()))
    
    def test_id_differnet(self):
        a = State()
        b = State()
        self.assertNotEqual(a.id, b.id)
    
    def test_str_rep(self):
        a = State()
        a.id = "12345"
        dd = datetime.now()
        a.created_at = a.updated_at = dd
        dd = repr(dd)
        ch = a.__str__()
        self.assertIn("[State] (12345)", ch)
        self.assertIn("'created_at': "+dd, ch)
        self.assertIn("'updated_at': "+dd, ch)
        self.assertIn("'id': '12345'", ch)
    
    def test_different_date(self):
        a = State()
        sleep(0.09)
        b = State()
        self.assertLess(a.created_at, b.created_at)
        self.assertLess(a.updated_at, b.updated_at)

    def test_todict(self):
        u = State()
        dic = u.to_dict()
        self.assertEqual(str, type(dic["id"]))
        self.assertEqual(str, type(dic["updated_at"]))
        self.assertEqual(str, type(dic["created_at"]))

    def test_to_dict(self):
        bm = State()
        self.assertTrue(dict, type(bm.to_dict()))
        self.assertIn("id", bm.to_dict())
        self.assertIn("created_at", bm.to_dict())
        self.assertIn("updated_at", bm.to_dict())
        self.assertIn("__class__", bm.to_dict())
if __name__ == "__main__":
    unittest.main()
