#!/usr/bin/python3
import unittest
from models.review import Review
from datetime import datetime
from time import sleep
"""test Review"""

class Testamenity(unittest.TestCase):
    def test_initialisation(self):
        m = Review()
        Review.place_id = 123
        Review.user_id = 111
        Review.text = "br"
        self.assertEqual(Review.text, "br", "valeur erronee")
        self.assertEqual(Review.user_id, 111, "valeur erronee")
        self.assertEqual(Review.place_id, 123, "valeur erronee")
        

    def test_type(self):
        self.assertEqual(Review, type(Review()))
    
    def test_id_differnet(self):
        a = Review()
        b = Review()
        self.assertNotEqual(a.id, b.id)
    
    def test_str_rep(self):
        a = Review()
        a.id = "12345"
        dd = datetime.now()
        a.created_at = a.updated_at = dd
        dd = repr(dd)
        ch = a.__str__()
        self.assertIn("[Review] (12345)", ch)
        self.assertIn("'created_at': "+dd, ch)
        self.assertIn("'updated_at': "+dd, ch)
        self.assertIn("'id': '12345'", ch)
    
    def test_different_date(self):
        a = Review()
        sleep(0.09)
        b = Review()
        self.assertLess(a.created_at, b.created_at)
        self.assertLess(a.updated_at, b.updated_at)

    def test_todict(self):
        u = Review()
        dic = u.to_dict()
        self.assertEqual(str, type(dic["id"]))
        self.assertEqual(str, type(dic["updated_at"]))
        self.assertEqual(str, type(dic["created_at"]))

    def test_to_dict(self):
        bm = Review()
        self.assertTrue(dict, type(bm.to_dict()))
        self.assertIn("id", bm.to_dict())
        self.assertIn("created_at", bm.to_dict())
        self.assertIn("updated_at", bm.to_dict())
        self.assertIn("__class__", bm.to_dict())
if __name__ == "__main__":
    unittest.main()
