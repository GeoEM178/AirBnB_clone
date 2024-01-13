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


def aflos(khr):
    """_summary_

    Args:
    khr : dictionary

    Returns:
        _type_: _description_
    """
    kws_kmos = re.search(r"\{(.*?)\}", khr)
    if kws_kmos:
        mflaa = shlex.split(khr[:kws_kmos.span()[0]])
        id = [i.strip(",") for i in mflaa][0]
        kms_hrf = kws_kmos.group(1)
        try:
            ks_hgt = ast.literal_eval("{" + kms_hrf + "}")
        except Exception:
            print(f"*** Unknown syntax: {ks_hgt}")
            return
        return id, ks_hgt
    else:
        am_gq = khr.split(",")
        try:
            r_id = am_gq[0]
            khr_key = am_gq[1]
            khr_value = am_gq[2]
            return f"{r_id}", f"{khr_key} {khr_value}"
        except Exception:
            print(f"*** Unknown syntax: {ks_hgt}")


class HBNBCommand(cmd.Cmd):
    """
    """
    prompt = "(hbnb)"
    mawgood = ["BaseModel", "User", "State",
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

    def default(self, args):
        """_summary_

        Args:
            line (str): _description_

        Returns:
            _type_: _description_
        """
        arguments = args.split('.')
        cdfn = arguments[0]

        cmd_fun = arguments[1].split('(')
        cfdn = cmd_fun[0]

        khr = cmd_fun[1].split(')')[0]
        # splitted_khrs= khr.split(',')

        cfd = {
            'all': self.do_all,
            'show': self.do_show,
            'destroy': self.do_destroy,
            'update': self.do_update,
            'create': self.do_create,
            'count': self.do_count,
        }

        if cfdn in cfd.keys():
            if cfdn == "update":
                # r_id = splitted_khrs[0]
                # update_key = splitted_khrs[1]
                # update_value = splitted_khrs[2]
                r_id, ks_hgt = aflos(khr)
                try:
                    if isinstance(ks_hgt, str):
                        attrs = ks_hgt
                        return cfd[cfdn]("{} {} {}".format(cdfn, r_id, attrs))
                    elif isinstance(ks_hgt, dict):
                        dar = ks_hgt
                        return cfd[cfdn]("{} {} {}".format(cdfn, r_id, dar))
                except Exception:
                    print(f"*** Unknown syntax: {ks_hgt}")
            else:
                return cfd[cfdn]("{} {}".format(cdfn, khr))

        print(f"*** Unknown syntax: {args}")
        return False

    def do_create(self, args):
        """_summary_

        Args:
            arg (_type_): _description_
        """
        awmr = shlex.split(args)

        if len(awmr) == 0:
            print("** class name missing **")
        elif awmr[0] not in self.mawgood:
            print("** class doesn't exist **")
        else:
            try:
                monsheea = eval(f"{awmr[0]}()")
            except Exception:
                pass

            storage.save()
            print(monsheea.id)

    def do_all(self, args):
        """_summary_

        Args:
            arg (_type_): _description_
        """
        kol_hgrq = storage.all()
        awmr = shlex.split(args)

        if len(awmr) == 0:
            for key, value in kol_hgrq.items():
                print(str(value))
        elif awmr[0] not in self.mawgood:
            print("** class doesn't exist **")
        else:
            for key, value in kol_hgrq.items():
                if key.split('.')[0] == awmr[0]:
                    print(str(value))

    def do_show(self, args):
        """_summary_

        Args:
            arg (_type_): _description_
        """
        awmr = shlex.split(args)

        if len(awmr) == 0:
            print("** class name missing **")
        elif awmr[0] not in self.mawgood:
            print("** class doesn't exist **")
        elif len(awmr) < 2:
            print("** instance id missing **")
        else:
            kol_hgrq = storage.all()
            key = "{}.{}".format(awmr[0], awmr[1])

            if key in kol_hgrq:
                print(kol_hgrq[key])
            else:
                print("** no instance found **")

    def do_destroy(self, args):
        """_summary_

        Args:
            arg (_type_): _description_
        """
        awmr = shlex.split(args)

        if len(awmr) == 0:
            print("** class name missing **")
        elif awmr[0] not in self.mawgood:
            print("** class doesn't exist **")
        elif len(awmr) < 2:
            print("** instance id missing **")
        else:
            kol_hgrq = storage.all()
            key = "{}.{}".format(awmr[0], awmr[1])

            if key in kol_hgrq:
                del kol_hgrq[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_update(self, args):
        """
        """
        awmr = shlex.split(args)
        if len(awmr) == 0:
            print("** class name missing **")
        elif awmr[0] not in self.mawgood:
            print("** class doesn't exist **")
        elif len(awmr) < 2:
            print("** instance id missing **")
        else:
            kol_hgrq = storage.all()
            key = "{}.{}".format(awmr[0], awmr[1])

            if key not in kol_hgrq:
                print("** no instance found **")
            elif len(awmr) < 3:
                print("** attribute name missing **")
            elif len(awmr) < 4:
                print("** value missing **")
            else:
                updated_obj = kol_hgrq[key]

                bass_dict = re.search(r"\{(.*?)\}", args)
                if bass_dict:
                    kms_hrf = bass_dict.group(1)
                    try:
                        ks_hgt = ast.literal_eval("{" + kms_hrf + "}")
                    except Exception:
                        print(f"*** Unknown syntax: {ks_hgt}")

                    dict_keys = list(ks_hgt.keys())
                    dict_values = list(ks_hgt.values())

                    dict_keys1 = dict_keys[0]
                    dict_keys2 = dict_keys[1]
                    dict_values1 = dict_values[0]
                    dict_values2 = dict_values[1]

                    setattr(updated_obj, dict_keys1, dict_values1)
                    setattr(updated_obj, dict_keys2, dict_values2)

                else:
                    attr_key = awmr[2]
                    attr_value = awmr[3]

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
        awmr = shlex.split(args)
        if len(awmr) == 0:
            print("** class name missing **")
        elif awmr[0] not in self.mawgood:
            print("** class doesn't exist **")
        else:
            kol_hgrq = storage.all()
            count = 0
            for key, value in kol_hgrq.items():
                if key.split('.')[0] == awmr[0]:
                    count += 1
            print(count)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
