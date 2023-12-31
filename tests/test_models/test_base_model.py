#!/usr/bin/python3
"""
This module contains the test cases for BaseModel class
methods.

"""
import time
from datetime import datetime
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
import re
import unittest
from uuid import uuid4
import os


class TestBaseModel(unittest.TestCase):
    """
    Test cases for the BaseModel class in the models/base_model module.

    """

# ========== SPECIAL METHOD TESTS ==========
    def setUp(self):
        """Set() helps tests method accordingly"""
        pass

    def tearDown(self):
        """tearDown() performs clean up after each method has been called"""
        pass


# ========== TESTS FOR CLASS ATRRIBUTES/OBJECT INSTANCES ==========

    my_obj = BaseModel()

    def test_set_obj(self):
        """Sets the object/instance occurance"""
        self.my_obj.name = "BaseObject"
        self.my_obj.my_number = 89

    def test_my_obj_types(self):
        """Tests the object type of the class"""
        obj_type = "<class 'models.base_model.BaseModel'>"
        self.assertTrue(type(self.my_obj), obj_type)

    def test_my_obj_wthout_argument(self):
        """Test if argument is passed to the class or not"""
        with self.assertRaises(TypeError) as e:
            BaseModel.__init__()
            self.assertEqual(
                """__init__() missing 1 required positional argument:
                'self'""", str(e.exception)
            )

    def test_my_obj_id(self):
        """Tests if the id value are unique"""
        obj_list = []
        for obj_id in range(34):
            obj_list.append(BaseModel().id)
        self.assertEqual(len(obj_list), len(set(obj_list)))

    def test_attributes(self):
        """Tests attributes value for instace of the BaseModel class."""
        pass

    def test_date_time(self):
        """Tests if updated_at and created_at are same at time of creation"""
        my_obj = BaseModel()
        now = datetime.now()
        # get the time difference
        t_difference = my_obj.updated_at - my_obj.created_at
        self.assertTrue(abs(t_difference.total_seconds()) < 0.01)
        t_difference = my_obj.created_at - now
        self.assertTrue(abs(t_difference.total_seconds()) < 0.01)

# ========== THE __STR__ METHOD TESTS ==========

    def test_init_without_argument(self):
        """Tests init method with no argument passed unto it"""
        pass

    def test_many_args(self):
        """Test init method with so many arguments"""
        pass

# ========== THE __STR__ METHOD TESTS ==========

    def test_my_obj_str_rep(self):
        """Test cases for the BaseModel class in the models/base_model."""

    def test_str_representation(self):
        """ Test the string representation of the object."""
        my_obj = BaseModel()
        string_repr = str(my_obj)
        # check if class name is present.

        self.assertIn("[BaseModel]", string_repr)
        # check if 'id' attribute is present.
        self.assertTrue(hasattr(my_obj, 'id'))
        # check if 'created_at' attribute is present
        self.assertTrue(hasattr(my_obj, 'created_at'))
        # check if 'updated_at' attribute is present
        self.assertTrue(hasattr(my_obj, 'updated_at'))

    def test_str_method(self):
        """Test for str method"""

        # This module use a regular expression.
        my_obj = BaseModel()
        reg = re.compile(r"^\[(.*)\] \((.*)\) (.*)$")
        match_char = reg.match(str(my_obj))
        self.assertIsNotNone(match_char)
        self.assertEqual(match_char.group(1), "BaseModel")
        self.assertEqual(match_char.group(2), my_obj.id)
        special_char = match_char.group(3)
        special_char = re.sub(
            r"(datetime\.datetime\([^)]*\))", "'\\1'", special_char
        )
        # to be continued

# ========== THE TO_DICT METHOD TESTS ==========

    def test_without_args_dict(self):
        """Tests for dictionary with no aruments(to_dict method)"""
        pass

    def test_excess_args_dict(self):
        """Tests for excess arguments to dictionary"""
        pass

    def test_save_method(self):
        """ Test that the save method updates the 'updated_at' attribute."""
        obj = BaseModel()
        prev_updated_at = obj.updated_at
        obj.save
        self.assertNotEqual(prev_updated_at, obj.updated_at)
        # check if 'updated_at' was updated.

    def test_to_dict_method(self):
        """ Test that the to_dict method returns a valid dictionary
        representation of the object."""

        my_obj = BaseModel()
        my_obj.name = "frank"
        my_obj.age = 23
        dict_method = my_obj.to_dict()
        is_it = self.assertEqual  # stores the assertEqual function/method
        is_it(dict_method['id'], my_obj.id)
        is_it(dict_method['__class__'], type(my_obj).__name__)
        is_it(dict_method['created_at'], my_obj.created_at.isoformat())
        is_it(dict_method['updated_at'], my_obj.updated_at.isoformat())
        is_it(dict_method['name'], my_obj.name)
        is_it(dict_method['age'], my_obj.age)

    def test_is_type(self):
        """Type test with kwargs from dictionary."""
        my_dict = {
            '__class__': 'BaseModel',
            'updated_at': datetime(
                2040, 12, 30, 23, 59, 30, 123456).isoformat(),
            'created_at': datetime.now().isoformat(),
            'id': uuid4(),
            'key_val': 'anything',
            'int': 100,
            'float': 1.00
        }
        new_dict = BaseModel(**my_dict)
        self.assertEqual(new_dict.to_dict(), my_dict)

    def test_is_type2(self):
        """Tests type test in dictinary"""


# ========== THE SAVE METHOD TESTS ==========

    def test_save_method(self):
        """ Test that the save method 'updated_at' attribute."""
        my_obj = BaseModel()
        time.sleep(0.3)    # ellaps time for .3 secs.
        present_time = datetime.now()
        my_obj.save()
        ellapsed = my_obj.updated_at - present_time
        self.assertTrue(abs(ellapsed.total_seconds()) < 0.01)

    # def test_excess_args_save(self):
    #     """Tests save() with too many arguments."""
    #     self.resetStorage()
    #     with self.assertRaises(TypeError) as e:
    #         BaseModel.save(self, 98)
    #         erro_msg = "save() 1 positional argument but 2 were given"
    #         self.assertEqual(str(e.exception), erro_msg)

    # def test_without_args_save(self):
    #     """Tests save() with no arguments passed."""
    #     self.reloadStorage()
    #     with self.assertRaises(TypeError) as e:
    #         BaseModel.save()
    #     erro_msg = "save() missing 1 required positional argument: 'self'"
    #     self.assertEqual(str(e.exception), erro_msg)

    # def test_storage_save(self):
    #     """
    #     Test for the function call of save() that it's from the storage
    #     module.
    #     """
    #     self.resetStorage()
    #     my_obj = BaseModel()
    #     my_obj.save()
    #     key = "{}.{}".format(type(my_obj).__name__, my_obj.id)
    #     obj = {key: my_obj.to_dict()}    # converts to dictionary file.
    #     self.assertTrue(os.path.isfile(FileStorage.__FileStorage__file_path))
    #     with open(
    #         FileStorage.__FileStorage__file_path, 'r', encoding='utf-8'
    #         ) as f:
    #         self.assertEqual(len(f.read()), len(json.dumps(obj)))
    #         f.seek(0)
    #         self.assertEqual(json.load(f), obj)


if __name__ == '__main':
    unittest.main()
