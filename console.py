#!/usr/bin/python3

"""
"""
import cmd
import shlex
import re
import ast
import models
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


def split_dict(param):
    """_summary_

    Args:
    param : dictionary

    Returns:
        _type_: _description_
    """
    dict_braces = re.search(r"\{(.*?)\}", param)
    if dict_braces:
        splitted_id = shlex.split(param[:dict_braces.span()[0]])
        id = [i.strip(",") for i in splitted_id][0]
        str_dict = dict_braces.group(1)
        try:
            dict_arg = ast.literal_eval("{" + str_dict + "}")
        except Exception:
            print(f"*** Unknown syntax: {dict_arg}")
            return
        return id, dict_arg
    else:
        cmd_args = param.split(",")
        try:
            param_id = cmd_args[0]
            param_key = cmd_args[1]
            param_value = cmd_args[2]
            return f"{param_id}", f"{param_key} {param_value}"
        except Exception:
            print(f"*** Unknown syntax: {dict_arg}")


class HBNBCommand(cmd.Cmd):
    """Console class"""

    prompt = "(hbnb)"
    existing_class = ["BaseModel", "User", "State", "City", "Amenity",
                             "Place", "Review"]

    def emptyline(self):
        """
        Just pass, Do nothing
        """
        pass

    def do_EOF(self, arg):
        """
        End operation by typing EOF or Ctrl+d
        """
        print()
        return True

    def do_quit(self, arg):
        """
        Quit console by typing 'quit'
        """
        return True

    def help_quit(self, arg):
        """
        Help command
        """
        print("Quit to exit")

    def do_create(self, args):
        """
        Create a new instance command
        """
        command_args = shlex.split(args)

        if len(command_args) == 0:
            print("** class name missing **")
        elif command_args[0] not in self.existing_class:
            print("** class doesn't exist **")
        else:
            try:
                created_instance = eval(f"{command_args[0]}()")
            except Exception:
                pass

            storage.save()
            print(created_instance.id)

    def do_show(self, args):
        """
        Print the string representation
        of object based on the class name
        """
        command_args = shlex.split(args)

        if len(command_args) == 0:
            print("** class name missing **")
        elif command_args[0] not in self.existing_class:
            print("** class doesn't exist **")
        elif len(command_args) < 2:
            print("** instance id missing **")
        else:
            all_objects = storage.all()
            key = "{}.{}".format(command_args[0], command_args[1])

            if key in all_objects:
                print(all_objects[key])
            else:
                print("** no instance found **")

    def do_destroy(self, args):
        """
        Destroy command to delete an object based on class and id
        """
        command_args = shlex.split(args)

        if len(command_args) == 0:
            print("** class name missing **")
        elif command_args[0] not in self.existing_class:
            print("** class doesn't exist **")
        elif len(command_args) < 2:
            print("** instance id missing **")
        else:
            all_objects = storage.all()
            key = "{}.{}".format(command_args[0], command_args[1])

            if key in all_objects:
                del all_objects[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, args):
        """
        Prints all string representation of all instances
        based or not on the class name
        """
        all_objects = storage.all()
        command_args = shlex.split(args)

        if len(command_args) == 0:
            for key, value in all_objects.items():
                print(str(value))
        elif command_args[0] not in self.existing_class:
            print("** class doesn't exist **")
        else:
            for key, value in all_objects.items():
                if key.split('.')[0] == command_args[0]:
                    print(str(value))

    def do_update(self, args):
        """
        Update command to update an instance based on
        the class name and id by adding or updating attribute
        """
        command_args = shlex.split(args)
        if len(command_args) == 0:
            print("** class name missing **")
        elif command_args[0] not in self.existing_class:
            print("** class doesn't exist **")
        elif len(command_args) < 2:
            print("** instance id missing **")
        else:
            all_objects = storage.all()
            key = "{}.{}".format(command_args[0], command_args[1])

            if key not in all_objects:
                print("** no instance found **")
            elif len(command_args) < 3:
                print("** attribute name missing **")
            elif len(command_args) < 4:
                print("** value missing **")
            else:
                updated_obj = all_objects[key]

                bass_dict = re.search(r"\{(.*?)\}", args)
                if bass_dict:
                    str_dict = bass_dict.group(1)
                    try:
                        dict_arg = ast.literal_eval("{" + str_dict + "}")
                    except Exception:
                        print(f"*** Unknown syntax: {dict_arg}")

                    dict_keys = list(dict_arg.keys())
                    dict_values = list(dict_arg.values())

                    dict_keys1 = dict_keys[0]
                    dict_keys2 = dict_keys[1]
                    dict_values1 = dict_values[0]
                    dict_values2 = dict_values[1]

                    setattr(updated_obj, dict_keys1, dict_values1)
                    setattr(updated_obj, dict_keys2, dict_values2)

                else:
                    attr_key = command_args[2]
                    attr_value = command_args[3]

                    try:
                        attr_value = eval(attr_value)
                    except Exception:
                        pass
                    setattr(updated_obj, attr_key, attr_value)

                    updated_obj.save()

    def do_count(self, args):
        """
        Prints count of instances of a class
        """
        command_args = shlex.split(args)
        if len(command_args) == 0:
            print("** class name missing **")
        elif command_args[0] not in self.existing_class:
            print("** class doesn't exist **")
        else:
            all_objects = storage.all()
            count = 0
            for key, value in all_objects.items():
                if key.split('.')[0] == command_args[0]:
                    count += 1
            print(count)

    def default(self, args):
        """
        Default console operation
        """
        arguments = args.split('.')
        class_name = arguments[0]

        cmd_fun = arguments[1].split('(')
        cmd_fun_name = cmd_fun[0]

        param = cmd_fun[1].split(')')[0]
        # splitted_params= param.split(',')

        cmd_fun_dict = {
            'all': self.do_all,
            'show': self.do_show,
            'destroy': self.do_destroy,
            'update': self.do_update,
            'create': self.do_create,
            'count': self.do_count,
        }

        if cmd_fun_name in cmd_fun_dict.keys():
            if cmd_fun_name == "update":
                # param_id = splitted_params[0]
                # update_key = splitted_params[1]
                # update_value = splitted_params[2]
                param_id, dict_arg = split_dict(param)
                try:
                    if isinstance(dict_arg, str):
                        attrs = dict_arg
                        return cmd_fun_dict[cmd_fun_name]
                        ("{} {} {}".format(class_name, param_id, attrs))
                    elif isinstance(dict_arg, dict):
                        dict_attr = dict_arg
                        return cmd_fun_dict[cmd_fun_name]
                        ("{} {} {}".format(class_name, param_id, dict_attr))
                except Exception:
                    print(f"*** Unknown syntax: {dict_arg}")
            else:
                return cmd_fun_dict[cmd_fun_name]
                ("{} {}".format(class_name, param))

        print(f"*** Unknown syntax: {args}")
        return False


if __name__ == "__main__":
    HBNBCommand().cmdloop()
