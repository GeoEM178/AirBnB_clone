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


if __name__ == "__main__":
    unittest.main()
