#!/usr/bin/python3
import os
import pep8
import unittest
from models.user import User
from models.engine.file_storage import FileStorage


def setUpModule():
    """ Funtion to set module """
    pass


def tearDownModule():
    """ Function to delete module"""
    pass


class TestStringMethods(unittest.TestCase):
    """ test the checking pep8 """
    def testpep8(self):
        stylepep8 = pep8.StyleGuide(quiet=True)
        pathfile1 = "models/user.py"
        pathfile2 = "tests/test_models/test_user.py"
        test = stylepep8.check_files([pathfile1, pathfile2])
        self.assertEqual(test.total_errors,
                         0, "Found code Errors/warning")


class Test_base_models(unittest.TestCase):
    """setUp Funtion to test the BaseModel"""

    def setUp(self):
        """ Seting variables """
        self.user_first = User()
        self.user_first.name = 'Jeniffer'
        self.user_first.lastname = "Vanegas"
        self.user_first.email = 'airbnb@holbertonshool.com'
        self.user_first.password = "root"
        print("setUp")

    def tearDown(self):
        """ End variable """
        print("tearDown")

    @classmethod
    def setUpClass(cls):
        """ define class """
        print("setUpClass")

    @classmethod
    def tearDownClass(cls):
        """ close the class """
        print("tearDownClass")

    def test_user_doc(self):
        self.assertIsNotNone(User.__doc__)
        self.assertIsNotNone(User.__init__.__doc__)

    def test_place_city(self):
        """ check if the city name is create """
        self.user_first.save()
        self.assertTrue(os.path.isfile('file.json'))
        self.assertTrue(hasattr(self.user_first, "__init__"))
        self.assertTrue(hasattr(self.user_first, "email"))
        self.assertTrue(hasattr(self.user_first, "password"))
        self.assertTrue(hasattr(self.user_first, "first_name"))
        self.assertTrue(hasattr(self.user_first, "last_name"))

    def test_user_name(self):
        """ check if the name is create """
        self.assertEqual(self.user_first.name, 'Jeniffer')

    def test_user_lastname(self):
        """ check if the last name is create """
        self.assertEqual(self.user_first.lastname, "Vanegas")

    def test_user_email(self):
        """ check the email if its created """
        self.assertEqual(self.user_first.email, 'airbnb@holbertonshool.com')

    def test_user_password(self):
        """ check the password if its created """
        self.assertEqual(self.user_first.password, "root")

    def test_models_to_dict(self):
        model_first = self.user_first.to_dict()
        self.assertIsInstance(model_first["created_at"], str)
        self.assertIsInstance(model_first["updated_at"], str)
        self.assertIsInstance(model_first["email"], str)
        self.assertIsInstance(model_first["id"], str)

    def test_user_instance(self):
        """ check user_first if is instance of User """
        self.assertIsInstance(self.user_first, User)

if __name__ == '__main__':
    unittest.main()
