#!/usr/bin/python3
"""
"""
import cmd
import shlex
import re
import ast
import sys
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
    """Class that extend from cmd
    """
    prompt = "(hbnb) "
    cls = ["BaseModel", "User", "State", "City", "Amenity", "Place", "Review"]

    def emptyline(self):
        """
        Just pass, Do nothing
        """
        if not sys.stdin.isatty():
            print()

    def do_EOF(self, arg):
        """EOF to exit the process
        """
        if not sys.stdin.isatty():
            print()
        return True

    def do_quit(self, arg):
        """Quit command to exit the program
        """
        if not sys.stdin.isatty():
            print()

        return True

    def do_help(self, arg):
        """_summary_

        Args:
            arg (_type_): _description_
        """
        if not sys.stdin.isatty():
            print()
        cmd.Cmd.do_help(self, arg)

    # def help_quit(self, arg):
    #     """
    #     """
    #     print("Quit to exit")

    def do_create(self, args):
        """_summary_

        Args:
            arg (_type_): _description_
        """
        command_args = shlex.split(args)

        if len(command_args) == 0:
            print("** class name missing **")
        elif command_args[0] not in self.cls:
            print("** class doesn't exist **")
        else:
            try:
                created_instance = eval(f"{command_args[0]}()")
            except Exception:
                pass

            storage.save()
            print(created_instance.id)

    def do_show(self, args):
        """_summary_

        Args:
            arg (_type_): _description_
        """
        command_args = shlex.split(args)

        if len(command_args) == 0:
            print("** class name missing **")
        elif command_args[0] not in self.cls:
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
        """_summary_

        Args:
            arg (_type_): _description_
        """
        command_args = shlex.split(args)

        if len(command_args) == 0:
            print("** class name missing **")
        elif command_args[0] not in self.cls:
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
        """_summary_

        Args:
            arg (_type_): _description_
        """
        all_objects = storage.all()
        command_args = shlex.split(args)

        if len(command_args) == 0:
            for key, value in all_objects.items():
                print(str(value))
        elif command_args[0] not in self.cls:
            print("** class doesn't exist **")
        else:
            for key, value in all_objects.items():
                if key.split('.')[0] == command_args[0]:
                    print(str(value))

    def do_update(self, args):
        """Update the class object
        """
        command_args = shlex.split(args)
        if len(command_args) == 0:
            print("** class name missing **")
        elif command_args[0] not in self.cls:
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
        """_summary_

        Args:
            arg (_type_): _description_
        """
        command_args = shlex.split(args)
        if len(command_args) == 0:
            print("** class name missing **")
        elif command_args[0] not in self.cls:
            print("** class doesn't exist **")
        else:
            all_objects = storage.all()
            count = 0
            for key, value in all_objects.items():
                if key.split('.')[0] == command_args[0]:
                    count += 1
            print(count)

    def default(self, args):
        """_summary_

        Args:
            line (str): _description_

        Returns:
            _type_: _description_
        """
        arguments = args.split('.')
        class_name = arguments[0]
        cnm = class_name

        # cf = cmd_fun  just for pycodestyle
        cf = arguments[1].split('(')
        cf_name = cf[0]

        param = cf[1].split(')')[0]

        cf_dict = {
            'all': self.do_all,
            'show': self.do_show,
            'destroy': self.do_destroy,
            'update': self.do_update,
            'create': self.do_create,
            'count': self.do_count,
        }

        if cf_name in cf_dict.keys():
            if cf_name == "update":
                param_id, dict_arg = split_dict(param)
                try:
                    if isinstance(dict_arg, str):
                        attrs = dict_arg
                        return cf_dict[cf_name](f"{cnm} {param_id} {attrs}")
                    elif isinstance(dict_arg, dict):
                        da = dict_arg
                        return cf_dict[cf_name](f"{cnm} {param_id} {da}")
                except Exception:
                    print(f"*** Unknown syntax: {dict_arg}")
            else:
                return cf_dict[cf_name]("{} {}".format(cnm, param))

        print(f"*** Unknown syntax: {args}")
        return False


if __name__ == "__main__":
    HBNBCommand().cmdloop()
