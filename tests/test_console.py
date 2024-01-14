#!/usr/bin/python3
"""
Test console
"""
import unittest
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand


class TestConsole(unittest.TestCase):
    """
    Test console
    """
    def test_destroy(self):
        """
        Test destroy function
        """
        command = 'create User'
        expected_promptt = '** no instance found **'

        with patch('sys.stdout', new=StringIO()) as fake_out:
            HBNBCommand().onecmd(command)

        command = 'destroy User 123'

        with patch('sys.stdout', new=StringIO()) as fake_out:
            HBNBCommand().onecmd(command)
            promptt = fake_out.getvalue().strip()

        self.assertEqual(promptt, expected_promptt)

    def test_show(self):
        """
        Test show function
        """
        command = 'show'
        expected_promptt = '** class name missing **'

        with patch('sys.stdout', new=StringIO()) as fake_out:
            HBNBCommand().onecmd(command)
            promptt = fake_out.getvalue().strip()

        self.assertEqual(promptt, expected_promptt)

    def test_create_with_invalid_class_name(self):
        """
        Test create for invalid class name
        """
        command = 'create InvalidClass'
        expected_promptt = '** class doesn\'t exist **'

        with patch('sys.stdout', new=StringIO()) as fake_out:
            HBNBCommand().onecmd(command)
            promptt = fake_out.getvalue().strip()

        self.assertEqual(promptt, expected_promptt)

    def test_create_command_no_class_name(self):
        """
        Test create command with no class name
        """
        command = 'create'
        expected_promptt = '** class name missing **'

        with patch('sys.stdout', new=StringIO()) as fake_out:
            HBNBCommand().onecmd(command)
            promptt = fake_out.getvalue().strip()

        self.assertEqual(promptt, expected_promptt)

    def test_parms(self):
        """
        test params for errorr
        """
        with patch("sys.stdout", new=StringIO()) as promptt:
            inning = "create"
            expected = "** class name missing **"
            HBNBCommand().onecmd(inning)
            self.assertEqual(expected, promptt.getvalue().strip())

    def test_new_cmd(self):
        """ Test without commands or args """
        with patch("sys.stdout", new=StringIO()) as promptt:
            self.assertEqual("", promptt.getvalue())

    def test_issues(self):
        """ test uncorrect id or uuid """
        invalid_id = 23421123
        with patch("sys.stdout", new=StringIO()) as promptt:
            inning = f'BaseModel.show("{invalid_id}")'
            HBNBCommand().onecmd(inning)
            rdd = "** no instance found **"
            self.assertEqual(promptt.getvalue().strip(), rdd)

        """ test to un giv any knowen class """
        with patch("sys.stdout", new=StringIO()) as promptt:
            inning = 'show'
            HBNBCommand().onecmd(inning)
            rdd = "** class name missing **"
            self.assertEqual(promptt.getvalue().strip(), rdd)

        """ test not an existing cls """
        with patch("sys.stdout", new=StringIO()) as promptt:
            inning = 'places.show("232342")'
            HBNBCommand().onecmd(inning)
            rdd = "** class doesn't exist **"
            self.assertEqual(promptt.getvalue().strip(), rdd)

        """ test smae as the last withopt """
        with patch("sys.stdout", new=StringIO()) as promptt:
            inning = 'Place.show()'
            HBNBCommand().onecmd(inning)
            rdd = "** instance id missing **"
            self.assertEqual(promptt.getvalue().strip(), rdd)


if __name__ == "__main__":
    unittest.main()
