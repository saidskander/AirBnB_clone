#!/usr/bin/python3
import unittest
import pep8
import os
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
                         0, "Found code Errors/warning).")


class TestModels(unittest.TestCase):
    """ Funtion to test the BaseModel"""

    def setUp(self):
        """ Set a variable """
        self.user_1 = User()
        self.user_1.name = 'Jeniffer'
        self.user_1.lastname = "Vanegas"
        self.user_1.email = 'airbnb@holbertonshool.com'
        self.user_1.password = "root"
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
        self.user_1.save()
        self.assertTrue(os.path.isfile('file.json'))
        self.assertTrue(hasattr(self.user_1, "__init__"))
        self.assertTrue(hasattr(self.user_1, "email"))
        self.assertTrue(hasattr(self.user_1, "password"))
        self.assertTrue(hasattr(self.user_1, "first_name"))
        self.assertTrue(hasattr(self.user_1, "last_name"))

    def test_user_name(self):
        """ check if the name is create """
        self.assertEqual(self.user_1.name, 'Jeniffer')

    def test_user_lastname(self):
        """ chaeck if the lastname is create """
        self.assertEqual(self.user_1.lastname, "Vanegas")

    def test_user_email(self):
        """ chaeck if the email is create """
        self.assertEqual(self.user_1.email, 'airbnb@holbertonshool.com')

    def test_user_password(self):
        """ chaeck if the password is create """
        self.assertEqual(self.user_1.password, "root")

    def test_models_to_dict(self):
        model_1 = self.user_1.to_dict()
        self.assertIsInstance(model_1["created_at"], str)
        self.assertIsInstance(model_1["updated_at"], str)
        self.assertIsInstance(model_1["email"], str)
        self.assertIsInstance(model_1["id"], str)

    def test_user_instance(self):
        """ check if user_1 is instance of User """
        self.assertIsInstance(self.user_1, User)

if __name__ == '__main__':
    unittest.main()
