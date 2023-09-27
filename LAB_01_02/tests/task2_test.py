import unittest
from unittest.mock import patch
from io import StringIO
import sys
import re
import LAB_01_02.tasks
# Импортируем ваш код
sys.path.append("H:/Мой диск/5 сем/VPO/VPO_LABS_TALAY/LAB_01_02")
from tasks.task2 import Person, get_number, get_name, input_person_data, print_person_data

class TestPerson(unittest.TestCase):

    def test_person_creation(self):
        person = Person('John', 'Doe', 30)
        self.assertEqual(person.first_name, 'John')
        self.assertEqual(person.last_name, 'Doe')
        self.assertEqual(person.age, 30)

    def test_get_number(self):
        with patch('builtins.input', side_effect=['abc', '0', '5']):
            captured_output = StringIO()
            with patch('sys.stdout', new=captured_output):
                number = get_number('Enter a number: ')
                self.assertEqual(number, 5)
            output = captured_output.getvalue()
            self.assertIn('Try again, enter a positive number:', output)

    def test_get_name(self):
        with patch('builtins.input', side_effect=['123', 'John Doe']):
            captured_output = StringIO()
            with patch('sys.stdout', new=captured_output):
                name = get_name('Enter a name: ')
                self.assertEqual(name, 'John Doe')
            output = captured_output.getvalue()
            self.assertIn('Try again, use only letters:', output)

class TestInputOutput(unittest.TestCase):

    def test_input_person_data(self):
        input_values = ['2', 'John', 'Doe', '30', 'Alice', 'Smith', '25']
        with patch('builtins.input', side_effect=input_values):
            persons, min_age, max_age, sum_of_all_ages = input_person_data()
            self.assertEqual(len(persons), 2)
            self.assertEqual(min_age, 25)
            self.assertEqual(max_age, 30)
            self.assertEqual(sum_of_all_ages, 55)

    def test_print_person_data(self):
        persons = [Person('John', 'Doe', 30), Person('Alice', 'Smith', 25)]
        captured_output = StringIO()
        with patch('sys.stdout', new=captured_output):
            print_person_data(persons, 25, 30, 55)
        output = captured_output.getvalue()
        self.assertIn('Surname Name Age', output)
        self.assertIn('Doe John 30', output)
        self.assertIn('Smith Alice 25', output)
        self.assertIn('Min. Age = 25, Max. Age = 30, Average Age = 27.5', output)

if __name__ == '__main__':
    unittest.main()
