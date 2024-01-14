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
        expected_output = '** no instance found **'

        with patch('sys.stdout', new=StringIO()) as fake_out:
            HBNBCommand().onecmd(command)

        command = 'destroy User 123'

        with patch('sys.stdout', new=StringIO()) as fake_out:
            HBNBCommand().onecmd(command)
            output = fake_out.getvalue().strip()

        self.assertEqual(output, expected_output)

    def test_show(self):
        """
        Test show function
        """
        command = 'show'
        expected_output = '** class name missing **'

        with patch('sys.stdout', new=StringIO()) as fake_out:
            HBNBCommand().onecmd(command)
            output = fake_out.getvalue().strip()

        self.assertEqual(output, expected_output)

    def test_create_with_invalid_class_name(self):
        """
        Test create for invalid class name
        """
        command = 'create InvalidClass'
        expected_output = '** class doesn\'t exist **'

        with patch('sys.stdout', new=StringIO()) as fake_out:
            HBNBCommand().onecmd(command)
            output = fake_out.getvalue().strip()

        self.assertEqual(output, expected_output)

    def test_create_command_no_class_name(self):
        """
        Test create command with no class name
        """
        command = 'create'
        expected_output = '** class name missing **'

        with patch('sys.stdout', new=StringIO()) as fake_out:
            HBNBCommand().onecmd(command)
            output = fake_out.getvalue().strip()

        self.assertEqual(output, expected_output)

    def test_args_length(self):
        """
        test if args length < 1 to print [** class name missing **]
        """
        with patch("sys.stdout", new=StringIO()) as output:
            input = "create"
            expected = "** class name missing **"
            HBNBCommand().onecmd(input)
            self.assertEqual(expected, output.getvalue().strip())


    def test_empty_line(self):
        """ Test handling empty lines """
        with patch("sys.stdout", new=StringIO()) as output:
            self.assertEqual("", output.getvalue())


    def test_errors(self):
        """ test passing invalid id """
        invalid_id = 23421123
        with patch("sys.stdout", new=StringIO()) as output:
            input = f'BaseModel.show("{invalid_id}")'
            HBNBCommand().onecmd(input)  # excute command
            res = "** no instance found **"
            self.assertEqual(output.getvalue().strip(), res)

        """ test passing no class """
        with patch("sys.stdout", new=StringIO()) as output:
            input = 'show'
            HBNBCommand().onecmd(input)  # excute command
            res = "** class name missing **"
            self.assertEqual(output.getvalue().strip(), res)

        """ test passing incorrect class """
        with patch("sys.stdout", new=StringIO()) as output:
            input = 'places.show("232342")'
            HBNBCommand().onecmd(input)  # excute command
            res = "** class doesn't exist **"
            self.assertEqual(output.getvalue().strip(), res)

        """ test passing not passing id """
        with patch("sys.stdout", new=StringIO()) as output:
            input = 'Place.show()'
            HBNBCommand().onecmd(input)  # excute command
            res = "** instance id missing **"
            self.assertEqual(output.getvalue().strip(), res)


if __name__ == "__main__":
    unittest.main()
