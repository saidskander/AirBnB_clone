#!/usr/bin/python3
""" Unittest for state class """
import unittest
import datetime
import uuid
import os
from models.state import State
from models.engine.file_storage import FileStorage
from models import storage


class TestState(unittest.TestCase):
    """ Tests the State class's """

    def setUp(self):
        """ setting kwargs in the exact way """
        try:
            os.remove("file.json")
        except:
            pass
        self.state1 = State(number=89,
                            created_at="2019-11-13T01:25:18.335269",
                            updated_at="2019-11-13T01:25:18.335279",
                            id="0e5ad480-ebf5-4bc8-9771-2a0e8daff35d")
        self.state2 = State()
        self.state3 = State()
        self.state4 = State(first_name="Betty",
                            last_name="Holberton",
                            email="airbnb@holbertonschool.com",
                            password="root",
                            created_at="2019-11-13T01:25:18.335289",
                            updated_at="2019-11-13T01:25:18.335299",
                            id="0e5ad480-ebf5-4bc8-9771-2a0e8daff36d")

    def tearDown(self):
        try:
            os.remove("file.json")
        except:
            pass

    def test_attrs(self):
        new = State(name="Holberton",
                    first_name="Betty",
                    last_name="Holberton",
                    email="airbnb@holbertonshool.com",
                    password="root",
                    created_at="2019-11-13T01:25:18.335289",
                    updated_at="2019-11-13T01:25:18.335299",
                    id="0e5ad480-ebf5-4bc8-9771-2a0e8daff36d")
        self.assertEqual(new.name, "Holberton")

    def test_attrs2(self):
        new = State()
        self.assertEqual(new.name, "")

    def test_init_insufficient_kwargs(self):
        with self.assertRaises(Exception):
            state0 = State(number=89)

    def test_init_sufficient_kwargs(self):
        self.assertEqual(self.state1.number, 89)
        self.assertEqual(self.state1.created_at,
                         datetime.datetime(2019, 11, 13, 1, 25, 18, 335269))
        self.assertEqual(self.state1.updated_at,
                         datetime.datetime(2019, 11, 13, 1, 25, 18, 335279))

    def test_init_defaults(self):
        self.assertIs(type(self.state2.created_at), datetime.datetime)
        self.assertIs(type(self.state3.created_at), datetime.datetime)
        self.assertIs(type(self.state2.updated_at), datetime.datetime)
        self.assertIs(type(self.state3.updated_at), datetime.datetime)
        self.assertIs(type(self.state2.id), str)
        self.assertIs(type(self.state3.id), str)
        self.assertNotEqual(self.state2.created_at, self.state3.created_at)
        self.assertNotEqual(self.state2.updated_at, self.state3.updated_at)
        self.assertNotEqual(self.state2.id, self.state3.id)

    def test_str(self):
        self.assertEqual(str(self.state1),
                         "[State] ({}) {}".format(
                             "0e5ad480-ebf5-4bc8-9771-2a0e8daff35d",
                             self.state1.__dict__))

    def test_str_class_attrs(self):
        self.assertIn('email', self.state4.__dict__.keys())
        self.assertIn('password', self.state4.__dict__.keys())
        self.assertIn('first_name', self.state4.__dict__.keys())
        self.assertIn('last_name', self.state4.__dict__.keys())
        self.assertEqual(str(self.state4),
                         "[State] ({}) {}".format(
                             "0e5ad480-ebf5-4bc8-9771-2a0e8daff36d",
                             self.state4.__dict__))
        self.assertNotIn('email', self.state1.__dict__.keys())
        self.assertNotIn('password', self.state1.__dict__.keys())
        self.assertNotIn('first_name', self.state1.__dict__.keys())
        self.assertNotIn('last_name', self.state1.__dict__.keys())
        self.assertNotIn('email', self.state2.__dict__.keys())
        self.assertNotIn('password', self.state2.__dict__.keys())
        self.assertNotIn('first_name', self.state2.__dict__.keys())
        self.assertNotIn('last_name', self.state2.__dict__.keys())

    def test_str_instance_attrs(self):
        self.assertNotIn('number', self.state2.__dict__.keys())
        self.assertIn('number', self.state1.__dict__.keys())

    def test_save(self):
        self.assertEqual(self.state1.updated_at,
                         datetime.datetime(2019, 11, 13, 1, 25, 18, 335279))
        self.state1.save()
        self.assertNotEqual(self.state1.updated_at,
                            datetime.datetime(2019, 11, 13, 1, 25, 18, 335279))
        self.assertEqual(type(self.state1.updated_at), datetime.datetime)

    def test_save_instance_attrs(self):
        self.state1.save()
        self.assertEqual(self.state1.number, 89)

    def test_save_class_attrs(self):
        self.state4.save()
        self.assertEqual(self.state4.first_name, "Betty")
        self.assertEqual(self.state4.last_name, "Holberton")
        self.assertEqual(self.state4.email, "airbnb@holbertonschool.com")
        self.assertEqual(self.state4.password, "root")

    def test_to_dict(self):
        dict1 = {'number': 89,
                 '__class__': "State",
                 'created_at': "2019-11-13T01:25:18.335269",
                 'updated_at': "2019-11-13T01:25:18.335279",
                 'id': "0e5ad480-ebf5-4bc8-9771-2a0e8daff35d"}
        self.assertEqual(self.state1.to_dict(), dict1)

    def test_to_dict_instance_attrs(self):
        self.state1.astring = "pew! pew pew!!!"
        self.state1.afloat = 9.87654321
        dict1 = {'number': 89,
                 'astring': "pew! pew pew!!!",
                 'afloat': 9.87654321,
                 '__class__': "State",
                 'created_at': "2019-11-13T01:25:18.335269",
                 'updated_at': "2019-11-13T01:25:18.335279",
                 'id': "0e5ad480-ebf5-4bc8-9771-2a0e8daff35d"}
        self.assertEqual(self.state1.to_dict(), dict1)

    def test_to_dict_class_attrs(self):
        dict4 = {'first_name': "Betty",
                 'last_name': "Holberton",
                 'email': "airbnb@holbertonschool.com",
                 'password': "root",
                 '__class__': "State",
                 'created_at': "2019-11-13T01:25:18.335289",
                 'updated_at': "2019-11-13T01:25:18.335299",
                 'id': "0e5ad480-ebf5-4bc8-9771-2a0e8daff36d"}
        self.assertEqual(self.state4.to_dict(), dict4)
