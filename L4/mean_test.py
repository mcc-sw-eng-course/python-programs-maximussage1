import exercise_8
import statistics
import math
import unittest
import json
import os
from exercise_14 import MyPowerList as exercise14_MyPowerList
from roman_converter import convertToRoman as excercise9_roman
from exercise_15 import UsersDatabase as exercise15_UsersDataBase
from exercise_15 import User as exercise15_User




# exercise 8

class Excercise8(unittest.TestCase):

    def test_sample_mean_invalid_inputs(self):
        test_cases = [
            ["a", "b"],
            [True, False],
            5
        ]
        for test in test_cases:
            with self.assertRaises(TypeError):
                exercise_8.sample_mean(test)

    def test_sample_mean_valid_inputs(self):
        test = [1, 2, 3, 4]
        expected = statistics.mean(test)
        result = exercise_8.sample_mean(test)
        self.assertEqual(expected, result)

        test = []
        expected = 0.0
        result = exercise_8.sample_mean(test)
        self.assertEqual(expected, result)

        test = [3.0, 4.0, 5.1]
        expected = statistics.mean(test)
        result = exercise_8.sample_mean(test)
        self.assertEqual(expected, result)

        test = [5]
        self.assertEqual(5.0, exercise_8.sample_mean(test))

        test = [0]
        self.assertEqual(0.0, exercise_8.sample_mean(test))

        test = [-2, -3, -4]
        expected = statistics.mean(test)
        result = exercise_8.sample_mean(test)
        self.assertEqual(expected, result)

    def test_standard_deviation_invalid_input(self):
        test_cases = [
            ["a", "b"],
            [True, False],
            5
        ]
        for test in test_cases:
            with self.assertRaises(TypeError):
                exercise_8.sample_standard_deviation(test)

    def test_standard_deviation_valid_inputs(self):
        test = [1, 2, 3, 4]
        expected = statistics.stdev(test)
        result = exercise_8.sample_standard_deviation(test)
        self.assertEqual(expected, result)
        test = []
        expected = 0.0
        result = exercise_8.sample_standard_deviation(test)
        self.assertEqual(expected, result)

        test = [3.0, 4.0, 5.1]
        expected = statistics.stdev(test)
        result = exercise_8.sample_standard_deviation(test)
        self.assertEqual(expected, result)

        test = [5]
        self.assertEqual(0.0, exercise_8.sample_standard_deviation(test))

        test = [0]
        self.assertEqual(0.0, exercise_8.sample_standard_deviation(test))

        test = [-2, -3, -4]
        expected = statistics.stdev(test)
        result = exercise_8.sample_standard_deviation(test)
        self.assertEqual(expected, result)

    def test_sample_median_invalid_inputs(self):
        test_cases = [
            ["a", "b"],
            [True, False],
            5
        ]
        for test in test_cases:
            with self.assertRaises(TypeError):
                exercise_8.median(test)

    def test_sample_median_valid_input(self):
        test = [1, 2, 3, 4]
        expected = statistics.median(test)
        result = exercise_8.median(test)
        self.assertEqual(expected, result)
        test = []
        expected = 0.0
        result = exercise_8.median(test)
        self.assertEqual(expected, result)

        test = [3.0, 4.0, 5.1]
        expected = statistics.median(test)
        result = exercise_8.median(test)
        self.assertEqual(expected, result)

        test = [5]
        self.assertEqual(5, exercise_8.median(test))

        test = [0]
        self.assertEqual(0.0, exercise_8.median(test))

        test = [-2, -3, -4]
        expected = statistics.median(test)
        result = exercise_8.median(test)
        self.assertEqual(expected, result)

    def test_npercentile_invalid_inputs(self):
        test_cases = [
            ["a", "b"],
            [True, False],
            5
        ]
        for test in test_cases:
            with self.assertRaises(TypeError):
                exercise_8.npercentile(test, 25)

        with self.assertRaises(ValueError):
            exercise_8.npercentile([2, 3, 4, 5], 0)

        with self.assertRaises(ValueError):
            exercise_8.npercentile([2, 3, 4, 5], 100)

    def test_npercentile_valid_inputs(self):
        test = [x for x in range(1, 100)]
        self.assertEqual(25, exercise_8.npercentile(test, 25))
        self.assertEqual(40, exercise_8.npercentile(test, 40))
        self.assertEqual(90, exercise_8.npercentile(test, 90))
        self.assertEqual(33, exercise_8.npercentile(test, 33))
        self.assertEqual(0.0, exercise_8.npercentile([], 90))
        self.assertEqual(0.0, exercise_8.npercentile(None, 90))

        test = [x for x in range(1, 11)]
        self.assertEqual(2.75, exercise_8.npercentile(test, 25))

    def test_quartile_invalid_inputs(self):
        test_cases = [
            ["a", "b"],
            [True, False],
            5
        ]
        for test in test_cases:
            with self.assertRaises(TypeError):
                exercise_8.nquartile(test, 25)

    def test_quartile_valid_inputs(self):
        test = [x for x in range(1, 100)]
        result = exercise_8.nquartile(test)
        self.assertEqual(25, result[0])
        self.assertEqual(50, result[1])
        self.assertEqual(75, result[2])

# Exercise14
class MyPowerListTest(unittest.TestCase):
    TEST_JSON_FILENAME = "test01.json"

    def setUp(self):
        self.under_test_list = [3, 4, 5, 12, 3, 5]

        # Create the file for testing
        with open(MyPowerListTest.TEST_JSON_FILENAME, "w") as file:
            json.dump(self.under_test_list, file)

    def tearDown(self):
        #  Delete the test JSON files
        if os.path.exists(MyPowerListTest.TEST_JSON_FILENAME):
            os.remove(MyPowerListTest.TEST_JSON_FILENAME)

    def test_successful_reading_of_file(self):
        under_test = exercise14_MyPowerList()
        self.assertIsNotNone(under_test)

        result = under_test.read_from_text_file(MyPowerListTest.TEST_JSON_FILENAME)
        self.assertTrue(result)
        self.assertEqual(self.under_test_list, under_test._backend)

        expected_str = "[" + ", ".join([str(x) for x in self.under_test_list]) + "]"

        # Test str representation of MyPowerList
        self.assertEqual(str(under_test), expected_str)

    def test_successful_reading_of_file_no_extension(self):
        under_test = exercise14_MyPowerList()
        self.assertIsNotNone(under_test)

        # Remove the extension, the code should be able to handle it
        result = under_test.read_from_text_file(MyPowerListTest.TEST_JSON_FILENAME[:-5])
        self.assertTrue(result)
        self.assertEqual(self.under_test_list, under_test._backend)

        expected_str = "[" + ", ".join([str(x) for x in self.under_test_list]) + "]"

        # Test str representation of MyPowerList
        self.assertEqual(str(under_test), expected_str)


class Excercise9Test(unittest.TestCase):

    def test_simple_numbers(self):
        self.assertEqual("I", excercise9_roman(1))
        self.assertEqual("V", excercise9_roman(5))
        self.assertEqual("X", excercise9_roman(10))
        self.assertEqual("L", excercise9_roman(50))
        self.assertEqual("C", excercise9_roman(100))
        self.assertEqual("D", excercise9_roman(500))
        self.assertEqual("M", excercise9_roman(1000))

    def test_compound_numbers(self):
        self.assertEqual("II", excercise9_roman(2))
        self.assertEqual("IV", excercise9_roman(4))
        self.assertEqual("IX", excercise9_roman(9))
        self.assertEqual("VII", excercise9_roman(7))
        self.assertEqual("CLIX", excercise9_roman(159))
        self.assertEqual("CCCXLIII", excercise9_roman(343))
        self.assertEqual("DCXCIX", excercise9_roman(699))
        self.assertEqual("MMXIX", excercise9_roman(2019))
        self.assertEqual("MCMXCI", excercise9_roman(1991))

    # Rene method returns a string saying 'invalid' for invalid values
    # Carlos method raises an exception
    def test_invalid_value(self):
        self.assertEqual("invalid", excercise9_roman("Carlos"))
        self.assertEqual("invalid", excercise9_roman(0))
        self.assertEqual("invalid", excercise9_roman(-10))
        self.assertEqual("invalid", excercise9_roman(3.14))
        self.assertEqual("invalid", excercise9_roman(2000000))
        self.assertEqual("invalid", excercise9_roman(True))
        with self.assertRaises(TypeError):
            excercise9_roman()

    def test_non_null_str_value(self):
        result = excercise9_roman(10)
        self.assertIsNotNone(result)
        self.assertIsInstance(result, str)




# Exercise15
class UserTest(unittest.TestCase):

    def setUp(self):
        # This will allow us to have a deterministic test
        exercise15_User.NEXT_ID = 1

    @classmethod
    def tearDownClass(cls):
        # Make sure that the IDs are resetted
        exercise15_User.NEXT_ID = 1

    def test_generate_id(self):
        test1 = exercise15_User.generate_id()
        test2 = exercise15_User.generate_id()
        test3 = exercise15_User.generate_id()

        self.assertTrue(test1 != test2 and test1 != test3 and test2 != test3)
        self.assertEqual(1, test1)
        self.assertEqual(2, test2)
        self.assertEqual(3, test3)

        user1 = exercise15_User("Name", "Address", "123456", "test@localhost")
        user2 = exercise15_User("Name", "Address", "123456", "test@localhost")

        # User's IDs should get sequentially bigger
        self.assertNotEqual(user1, user2)
        self.assertEqual(4, user1.user_id)
        self.assertEqual(5, user2.user_id)

    def test_str_representation(self):
        name = "TestName1"
        address = "Test Address 123"
        phone = "555-987-2345"
        email = "test@localhost"
        under_test = exercise15_User(name, address, phone, email)
        expected_str = f"Name: {name}, Address: {address}, Phone: {phone}, Email: {email}"

        self.assertEqual(str(under_test), expected_str)

        name = "AnotherName"
        address = "Another Address 546"
        phone = "555-987-1234"
        email = "test@127.0.0.1"
        under_test = exercise15_User(name, address, phone, email)
        expected_str = f"Name: {name}, Address: {address}, Phone: {phone}, Email: {email}"

        self.assertEqual(str(under_test), expected_str)


class UserDatabaseTest(unittest.TestCase):
    TEST_JSON_FILENAME = "test01.json"

    def setUp(self):
        exercise15_User.NEXT_ID = 1
        self.under_test = exercise15_UsersDataBase()

    def tearDown(self):
        #  Delete all the test JSON files
        if os.path.exists(UserDatabaseTest.TEST_JSON_FILENAME):
            os.remove(UserDatabaseTest.TEST_JSON_FILENAME)

    @classmethod
    def tearDownClass(cls):
        # Reset the User IDs
        exercise15_User.NEXT_ID = 1

    def test_new_user(self):
        name = "Test New User"
        address = "Test Address"
        phone = "555 332 1234"
        email = "mail@itesm.mx"
        user1_id = self.under_test.new_user(name, address, phone, email)

        self.assertTrue(len(self.under_test.users) == 1)
        for u in self.under_test.users.values():
            self.assertEqual(name, u.name)
            self.assertEqual(address, u.address)
            self.assertEqual(phone, u.phone)
            self.assertEqual(email, u.email)
            self.assertEqual(user1_id, u.user_id)

        self.under_test.new_user(name, address, phone, email)
        self.assertTrue(len(self.under_test.users) == 2)

    def test_save_to_file(self):
        name = "Test New User"
        address = "Test Address"
        phone = "555 332 1234"
        email = "mail@itesm.mx"
        self.under_test.new_user(name, address, phone, email)
        self.under_test.new_user(name, address, phone, email)

        db_before_serialization = self.under_test.users

        self.under_test.save_to_text_file(UserDatabaseTest.TEST_JSON_FILENAME)

        # Check that the file exists in the filesystem
        self.assertTrue(os.path.exists(UserDatabaseTest.TEST_JSON_FILENAME))

        with open(UserDatabaseTest.TEST_JSON_FILENAME, "r") as file:
            data = json.load(file)

        for k in data.keys():
            file_user = data.get(k)
            user_before_serialization = db_before_serialization.get(k)

            self.assertIsNotNone(file_user)
            self.assertIsNotNone(user_before_serialization)

            self.assertEqual(user_before_serialization.user_id, file_user.get("user_id"))
            self.assertEqual(user_before_serialization.name, file_user.get("name"))
            self.assertEqual(user_before_serialization.address, file_user.get("address"))
            self.assertEqual(user_before_serialization.phone, file_user.get("phone"))
            self.assertEqual(user_before_serialization.email, file_user.get("email"))

    def test_save_to_file_no_extension(self):
        name = "Test New User"
        address = "Test Address"
        phone = "555 332 1234"
        email = "mail@itesm.mx"
        self.under_test.new_user(name, address, phone, email)
        self.under_test.new_user(name, address, phone, email)

        db_before_serialization = self.under_test.users

        # Remove the extension from the file, the class should add it later
        self.under_test.save_to_text_file(UserDatabaseTest.TEST_JSON_FILENAME[:-5])

        # Check that the file exists in the filesystem
        self.assertTrue(os.path.exists(UserDatabaseTest.TEST_JSON_FILENAME))

        with open(UserDatabaseTest.TEST_JSON_FILENAME, "r") as file:
            data = json.load(file)

        for k in data.keys():
            file_user = data.get(k)
            user_before_serialization = db_before_serialization.get(k)

            self.assertIsNotNone(file_user)
            self.assertIsNotNone(user_before_serialization)

            self.assertEqual(user_before_serialization.user_id, file_user.get("user_id"))
            self.assertEqual(user_before_serialization.name, file_user.get("name"))
            self.assertEqual(user_before_serialization.address, file_user.get("address"))
            self.assertEqual(user_before_serialization.phone, file_user.get("phone"))
            self.assertEqual(user_before_serialization.email, file_user.get("email"))

    def test_save_to_file_with_empty_filename(self):
        # An empty filename should raise a ValueError
        with self.assertRaises(ValueError):
            self.under_test.save_to_text_file("")

        with self.assertRaises(ValueError):
            self.under_test.save_to_text_file(None)

    def test_load_from_file(self):
        user_id = 7
        name = "Test New User"
        address = "Test Address"
        phone = "555 332 1234"
        email = "mail@itesm.mx"

        test_case = {
            str(user_id): {
                "user_id": user_id,
                "name": name,
                "address": address,
                "phone": phone,
                "email": email
            }
        }

        # Simulate a file with a previous MyPowerList
        with open(UserDatabaseTest.TEST_JSON_FILENAME, "w") as file:
            json.dump(test_case, file)

        self.under_test.load_from_file(UserDatabaseTest.TEST_JSON_FILENAME)
        self.assertTrue(len(self.under_test.users) == 1)

        db_user = self.under_test.users.get(str(user_id))
        self.assertIsInstance(db_user, exercise15_User)
        self.assertEqual(user_id, db_user.user_id)
        self.assertEqual(name, db_user.name)
        self.assertEqual(address, db_user.address)
        self.assertEqual(phone, db_user.phone)
        self.assertEqual(email, db_user.email)

    def test_load_from_file_no_extension(self):
        user_id = 7
        name = "Test New User"
        address = "Test Address"
        phone = "555 332 1234"
        email = "mail@itesm.mx"

        test_case = {
            str(user_id): {
                "user_id": user_id,
                "name": name,
                "address": address,
                "phone": phone,
                "email": email
            }
        }

        # Simulate a file with a previous MyPowerList
        with open(UserDatabaseTest.TEST_JSON_FILENAME, "w") as file:
            json.dump(test_case, file)

        # Remove the extension from the filename
        self.under_test.load_from_file(UserDatabaseTest.TEST_JSON_FILENAME[:-5])
        self.assertTrue(len(self.under_test.users) == 1)

        db_user = self.under_test.users.get(str(user_id))
        self.assertIsInstance(db_user, exercise15_User)
        self.assertEqual(user_id, db_user.user_id)
        self.assertEqual(name, db_user.name)
        self.assertEqual(address, db_user.address)
        self.assertEqual(phone, db_user.phone)
        self.assertEqual(email, db_user.email)

    def test_search(self):
        name = "Test New User Search"
        address = "Test Address Search"
        phone = "555 332 4321"
        email = "search@itesm.mx"

        new_user_id = self.under_test.new_user(name, address, phone, email)

        retrieved_user = self.under_test.search(new_user_id)

        self.assertIsNotNone(retrieved_user, "No user was found and it should've been retrieved.")

        self.assertEqual(retrieved_user.name, name)
        self.assertEqual(retrieved_user.address, address)
        self.assertEqual(retrieved_user.phone, phone)
        self.assertEqual(retrieved_user.email, email)

        # Invalid users should return None
        invalid_user = self.under_test.search(99)
        self.assertIsNone(invalid_user)

if __name__ == '__main__':
    unittest.main()
