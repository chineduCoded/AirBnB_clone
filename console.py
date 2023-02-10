#!/usr/bin/python3
"""Defines HBNBCommand Class"""
import sys
from models import storage
from models.base_model import BaseModel
import cmd


class HBNBCommand(cmd.Cmd):
    """HBNB entry point"""
    prompt = "(hbnb) "
    classes = ["BaseModel"]

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def help_quit(self):
        print("Quitt command to exit the program\n")

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        return True

    def help_EOF(self):
        print("EOF command to exit the program\n")

    def emptyline(self):
        """Do nothing when empty line is entered"""
        pass

    def do_create(self, args):
        """Create a new instance of BaseModel"""
        if len(args) == 0:
            print("** class name missing **")
        elif args not in self.classes:
            print("** class doesn't exist **")
            return False
        else:
            new = eval("{}()".format(args))
            new.save()
            print(new.id)

    def help_create(self):
        """help create"""
        print("Create command to create a class instance\n")

    def do_show(self, line):
        """show an instance"""
        args = line.split()
        if len(args) == 0:
            print("** class name missing **")
            return False
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
            return False

        if len(args) < 2:
            print("** instance id missing **")
            return False

        objs = storage.all()
        for i in objs.keys():
            if i == "{}.{}".format(args[0], args[1]):
                print(objs[i])
                return False
        print("** no instance found **")

    def help_show(self):
        """help show"""
        print("Show command to show instance of class\n")

    def do_destroy(self, line):
        """deletes an instance based on the class id"""
        args = line.split()
        if len(line) == 0:
            print("** class name missing **")
            return False
        elif args[0] not in self.classes:
            print("** clas doesn't exist **")
            return False
        elif len(args) < 2:
            print("** instance id missing **")
            return False
        else:
            objs = storage.all()
            for i in objs:
                if i == "{}.{}".format(args[0], args[1]):
                    objs.pop(i)
                    storage.save()
                    return False
            print("** no instance found **")

    def help_destroy(self):
        """help destroy"""
        print("Destroy command to destroy instance of class\n")

    def do_all(self, line):
        """Displays all the instance of class"""
        args = line.split()
        objs = storage.all()

        if len(args) == 0:
            for i in objs:
                str_arg = str(objs[i])
                print(str_arg)
        elif line not in self.classes:
            print("** class doesn't exist **")
            return False
        else:
            for i in objs:
                if i.startswith(args[0]):
                    str_arg = str(objs[i])
                    print(str_arg)
        return False

    def help_all(self):
        """help display all"""
        print("All command to display all instancess\n")

    def do_update(self, line):
        ''' updates an instance based on class name and id'''
        args = line.split()
        flag = 0

        if len(line) == 0:
            print('** class name missing **')
            return False

        try:
            class_name = line.split()[0]
            eval("{}()".format(class_name))
        except IndexError:
            print('** class doesn\'t exist **')
            return False

        try:
            instance_id = line.split()[1]
        except IndexError:
            print('** instance id missing **')
            return False

        objs = storage.all()
        try:
            class_change = objs["{}.{}".format(class_name, instance_id)]
        except IndexError:
            print('** no instance found **')
            return False

        try:
            attr_name = line.split()[2]
        except IndexError:
            print('** attribute name missing **')
            return False

        try:
            update_value = line.split()[3]
        except IndexError:
            print('** value missing **')
            return False

        if update_value.isdecimal() is True:
            setattr(classs_change, attr_name, int(update_value))
            storage.save()
        else:
            try:
                setattr(class_change, attr_name, float(update_value))
                storage.save()
            except:
                setattr(class_change, attr_name, str(update_value))
                storage.save()

    def help_update(self):
        """help updates an instance"""
        print("Update command to update an instance of class\n")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
