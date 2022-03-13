import unittest
from app.models import User


class TestUser(unittest.TestCase):
    
    def setUp(self):
        self.new_user = User(name='Eugene',email="eugenemarkke@gmail.com",password='password')
        
    def test_no_acces_password(self):
        with self.assertRaises(AttributeError):
            self.new_user.password
            
    def test_first_name(self):
        self.assertEquals(self.new_user.first_name, self.new_user.name.split()[0])