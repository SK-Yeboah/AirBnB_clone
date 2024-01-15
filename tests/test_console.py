#!/usr/bin/python3 
import unittest
from unittest.mock import patch
from io import StringIO
from console import HBNBCommand


class TestHBNBCommand(unittest.TestCase):
    @patch('sys.stdout', new_callable=StringIO)
    def assert_output(self, expected_output, mock_stdout):
        HBNBCommand().onecmd(expected_output)
        self.assertEqual(mock_stdout.getvalue().strip(), expected_output.strip())

    def test_quit_command(self):
        self.assertTrue(HBNBCommand().onecmd("quit"))

    def test_EOF_command(self):
        self.assertTrue(HBNBCommand().onecmd("EOF"))

    @patch('sys.stdout', new_callable=StringIO)
    def test_emptyline(self, mock_stdout):
        HBNBCommand().onecmd("\n")
        self.assertEqual(mock_stdout.getvalue().strip(), "")

    def test_default_command_invalid_syntax(self):
        self.assert_output("*** Unknown syntax: invalid_syntax", "invalid_syntax")

    def test_default_command_valid_syntax(self):
        with patch('console.HBNBCommand.do_create', return_value=True):
            self.assertTrue(HBNBCommand().onecmd("create BaseModel"))

    def test_create_command_missing_class_name(self):
        self.assert_output("** class name missing **", "create")

    @patch('models.storage.save')
    @patch('models.storage.new')
    def test_create_command_success(self, mock_new, mock_save):
        self.assert_output("123456", "create BaseModel")

    def test_show_command_invalid_syntax(self):
        self.assert_output("Invalid syntax. Use: <class name>.show('<id>') or Usage: show <class> <id>", "show")
        self.assert_output("Invalid syntax. Use: <class name>.show('<id>') or Usage: show <class> <id>", "show BaseModel")
        self.assert_output("Invalid syntax. Use: <class name>.show('<id>') or Usage: show <class> <id>", "show BaseModel invalid_id")

    def test_show_command_class_not_exist(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            HBNBCommand().onecmd("show InvalidClass 123")
            self.assertEqual(mock_stdout.getvalue().strip(), "Class 'InvalidClass' doesn't exist.")

    def test_show_command_instance_not_found(self):
        with patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            HBNBCommand().onecmd("show BaseModel invalid_id")
            self.assertEqual(mock_stdout.getvalue().strip(), "No instance found with id 'invalid_id' in class 'BaseModel'")

    @patch('models.storage.all')
    @patch('sys.stdout', new_callable=StringIO)
    def test_show_command_success(self, mock_stdout, mock_all):
        mock_all.return_value = {'BaseModel.123': "{'id': '123', 'name': 'test'}"}
        HBNBCommand().onecmd("show BaseModel 123")
        self.assertEqual(mock_stdout.getvalue().strip(), "{'id': '123', 'name': 'test'}")

    @patch('models.storage.save')
    @patch('models.storage.all')
    @patch('sys.stdout', new_callable=StringIO)
    def test_destroy_command_success(self, mock_stdout, mock_all, mock_save):
        mock_all.return_value = {'BaseModel.123': "{'id': '123', 'name': 'test'}"}
        HBNBCommand().onecmd("destroy BaseModel 123")
        self.assertEqual(mock_stdout.getvalue().strip(), "")
        self.assertEqual(mock_save.call_count, 1)

    def test_all_command_invalid_syntax(self):
        self.assert_output("Invalid syntax1. Use: <class name>.all()", "all")
        self.assert_output("Class 'InvalidClass' doesn't exist.", "all InvalidClass")

    @patch('models.storage.all')
    @patch('sys.stdout', new_callable=StringIO)
    def test_all_command_success(self, mock_stdout, mock_all):
        mock_all.return_value = {'BaseModel.123': "{'id': '123', 'name': 'test'}"}
        HBNBCommand().onecmd("all BaseModel")
        # self.assertEqual(mock_stdout.getvalue().strip(), "Instances of BaseModel: ['{'id': '123', 'name': 'test'}']")
        self.assertEqual(mock_stdout.getvalue().strip(), "BaseModel\n{'id': '123', 'name': 'test'}")


    @patch('models.storage.all')
    @patch('sys.stdout', new_callable=StringIO)
    def test_count_command_success(self, mock_stdout, mock_all):
        mock_all.return_value = {'BaseModel.123': "{'id': '123', 'name': 'test'}"}
        HBNBCommand().onecmd("count BaseModel")
        self.assertEqual(mock_stdout.getvalue().strip(), "Number of instances of BaseModel: 1")

    def test_update_command_invalid_syntax(self):
        self.assert_output("Invalid syntax. Usage: update <class name> <id> <attribute name> '<attribute value>' or "
            "<class name>.update(<id>, <attribute name>, '<attribute value>') or "
            "<class name>.update(<id>, <dictionary>)", "update")
        self.assert_output("Invalid syntax. Usage: update <class name> <id> <attribute name> '<attribute value>' or "
            "<class name>.update(<id>, <attribute name>, '<attribute value>') or "
            "<class name>.update(<id>, <dictionary>)", "update BaseModel")
        self.assert_output("Invalid syntax. Usage: update <class name> <id> <attribute name> '<attribute value>' or "
            "<class name>.update(<id>, <attribute name>, '<attribute value>') or "
            "<class name>.update(<id>, <dictionary>)", "update BaseModel 123")
        self.assert_output("Invalid syntax. Usage: update <class name> <id> <attribute name> '<attribute value>' or "
            "<class name>.update(<id>, <attribute name>, '<attribute value>') or "
            "<class name>.update(<id>, <dictionary>)", "update BaseModel 123 attribute_name")
        self.assert_output("Invalid syntax. Usage: update <class name> <id> <attribute name> '<attribute value>' or "
            "<class name>.update(<id>, <attribute name>, '<attribute value>') or "
            "<class name>.update(<id>, <dictionary>)", "update BaseModel 123 attribute_name 'new_value' invalid_arg")

    @patch('models.storage.save')
    @patch('models.storage.new')
    def test_update_command_success(self, mock_new, mock_save):
        self.assert_output("", "update BaseModel 123 attribute_name 'new_value'")
        self.assertEqual(mock_save.call_count, 1)

if __name__ == '__main__':
    unittest.main()
