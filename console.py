#!/usr/bin/python3
"""
"""
import cmd
import shlex
import models
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class HBNBCommand(cmd.Cmd):
    """
    """
    prompt = "(hbnb)"
    existing_class = ["BaseModel", "User", "State",
                       "City", "Amenity", "Place", "Review"]

    def emptyline(self):
        """
        Just pass, Do nothing
        """
        pass

    def do_EOF(self, arg):
        """
        """
        print()
        return True

    def do_quit(self, arg):
        """
        """
        return True

    def help_quit(self, arg):
        """
        """
        print("Quit to exit")
    
    def do_create(self, args):
        """_summary_

        Args:
            arg (_type_): _description_
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
        """_summary_

        Args:
            arg (_type_): _description_
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
        """_summary_

        Args:
            arg (_type_): _description_
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
        """_summary_

        Args:
            arg (_type_): _description_
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
        """_summary_

        Args:
            line (str): _description_

        Returns:
            _type_: _description_
        """
        arguments = args.split('.')
        class_name = arguments[0]

        cmd_fun = arguments[1].split('(')
        cmd_fun_name = cmd_fun[0]

        param = cmd_fun[1].split(')')[0]
        splitted_params= param.split(',')

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
                param_id = splitted_params[0]
                update_key = splitted_params[1]
                update_value = splitted_params[2]
                return cmd_fun_dict[cmd_fun_name]("{} {} {} {}".format(class_name,
                                                                 param_id,
                                                                 update_key,
                                                                 update_value))
            else:
                return cmd_fun_dict[cmd_fun_name](f"{class_name} {param}")

        print(f"*** Unknown syntax: {args}")
        return False

if __name__ == "__main__":
    HBNBCommand().cmdloop()
