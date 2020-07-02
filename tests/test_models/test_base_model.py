#!/usr/bin/python3
import unittest
import pep8
import os
from models.__init__ import storage
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage


def setUpModule():
    """ set update module """
    pass


class TestStringMethods(unittest.TestCase):
    """ pep8 checker """
    def testpep8(self):
        style = pep8.StyleGuide(quiet=True)
        file1 = "models/base_model.py"
        file2 = "tests/test_models/test_base_model.py"
        check = style.check_files([file1, file2])
        self.assertEqual(check.total_errors, 0,
                         "errors and warnings")


class TestModels(unittest.TestCase):

    def setUp(self):
        """ put a variable """
        self.my_model = BaseModel()
        self.my_model.my_number = 55
        print("setUp")

    def tearDown(self):
        """ Ending of the variable """
        print("tearDown")

    @classmethod
    def setUpClass(cls):
        """ Set a Class """
        print("setUpClass")

    @classmethod
    def tearDownClass(cls):
        """ Def a Class"""
        print("tearDownClass")

    def test_models_doc(self):
        """ test models docs """
        self.assertIsNotNone(BaseModel.__doc__)
        self.assertIsNotNone(BaseModel.__init__.__doc__)
        self.assertIsNotNone(BaseModel.save.__doc__)
        self.assertIsNotNone(BaseModel.__str__.__doc__)
        self.assertIsNotNone(BaseModel.to_dict.__doc__)

    def test_models_name(self):
        """ testig names if its created """
        self.my_model.name = 'Holberton'
        self.assertEqual(self.my_model.name, 'Holberton')

    def test_models_number(self):
        """ testing if the number is created """
        self.assertEqual(self.my_model.my_number, 55)

    def test_models_exist(self):
        """ testing if the json & methods are existed """
        self.my_model.save()
        self.assertTrue(os.path.isfile('file.json'))
        self.assertTrue(hasattr(self.my_model, "__init__"))
        self.assertTrue(hasattr(self.my_model, "__str__"))
        self.assertTrue(hasattr(self.my_model, "save"))
        self.assertTrue(hasattr(self.my_model, "to_dict"))

    def test_models_not_empty(self):
        """ testing if the json file is not empty """
        self.assertTrue('file.json')

    def test_models_save(self):
        """ testing if the save function works perfectly """
        a = self.my_model.updated_at()
        self.my_model.save()
        self.assertNotEqual(a, self.my_model.update_at)
        self.assertNotEqual(self.my_model.created_at,
                            self.my_model.updated_at)

    def test_models_instance(self):
        """ testing if user_1 is instance of User """
        self.assertIsInstance(self.my_model, BaseModel)

    def test_models_to_dict(self):
        model_1 = self.my_model.to_dict()
        self.assertIsInstance(model_1["created_at"], str)
        self.assertIsInstance(model_1["updated_at"], str)
        self.assertIsInstance(model_1["my_number"], int)
        self.assertIsInstance(model_1["id"], str)

if __name__ == '__main__':
    unittest.main()
