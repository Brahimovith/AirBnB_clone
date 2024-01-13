#!/usr/bin/python3
import unittest
from models.user import User
from datetime import datetime
from time import sleep
"""test User"""
class Testamenity(unittest.TestCase):
    def test_initialisation(self):
        m = User()
        User.password = "brahim"
        User.email = "a@b"
        User.first_name = "b"
        User.last_name = "s"
        self.assertEqual(User.password, "brahim", "valeur erronee")
        self.assertEqual(User.email, "a@b", "valeur erronee")
        self.assertEqual(User.first_name, "b", "valeur erronee")
        self.assertEqual(User.last_name, "s", "valeur erronee")
        

    def test_type(self):
        self.assertEqual(User, type(User()))
    
    def test_id_differnet(self):
        a = User()
        b = User()
        self.assertNotEqual(a.id, b.id)
    
    def test_str_rep(self):
        a = User()
        a.id = "12345"
        dd = datetime.now()
        a.created_at = a.updated_at = dd
        dd = repr(dd)
        ch = a.__str__()
        self.assertIn("[User] (12345)", ch)
        self.assertIn("'created_at': "+dd, ch)
        self.assertIn("'updated_at': "+dd, ch)
        self.assertIn("'id': '12345'", ch)
    
    def test_different_date(self):
        a = User()
        sleep(0.09)
        b = User()
        self.assertLess(a.created_at, b.created_at)
        self.assertLess(a.updated_at, b.updated_at)
    
    def test_todict(self):
        u = User()
        dic = u.to_dict()
        self.assertEqual(str, type(dic["id"]))
        self.assertEqual(str, type(dic["updated_at"]))
        self.assertEqual(str, type(dic["created_at"]))

    def test_to_dict(self):
        bm = User()
        self.assertTrue(dict, type(bm.to_dict()))
        self.assertIn("id", bm.to_dict())
        self.assertIn("created_at", bm.to_dict())
        self.assertIn("updated_at", bm.to_dict())
        self.assertIn("__class__", bm.to_dict())
if __name__ == "__main__":
    unittest.main()
