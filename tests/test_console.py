import unittest
from io import StringIO
from unittest.mock import patch
from console import HBNBCommand

class TestConsole(unittest.TestCase):
    def test_destroy(self):
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
        command = 'show'
        expected_output = '** class name missing **'
    
        with patch('sys.stdout', new=StringIO()) as fake_out:
            HBNBCommand().onecmd(command)
            output = fake_out.getvalue().strip()
    
        self.assertEqual(output, expected_output)

    def test_create_with_invalid_class_name(self):
        command = 'create InvalidClass'
        expected_output = '** class doesn\'t exist **'
    
        with patch('sys.stdout', new=StringIO()) as fake_out:
            HBNBCommand().onecmd(command)
            output = fake_out.getvalue().strip()
    
        self.assertEqual(output, expected_output)

    def test_create_command_no_class_name(self):
        command = 'create'
        expected_output = '** class name missing **'
    
        with patch('sys.stdout', new=StringIO()) as fake_out:
            HBNBCommand().onecmd(command)
            output = fake_out.getvalue().strip()
    
        self.assertEqual(output, expected_output)