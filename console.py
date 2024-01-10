#!/usr/bin/python3
"""
"""
import cmd
import shlex
import models
from models import storage
from models.base_model import BaseModel

class HBNBCommand(cmd.Cmd):
    """
    """
    prompt = "(hbnb)"
    existing_class = ["BaseModel"]

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
            created_instance = BaseModel()
            created_instance.save()
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

if __name__ == "__main__":
    HBNBCommand().cmdloop()
