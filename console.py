#!/usr/bin/python3
"""
Command interpreter for the AirBnB clone project
"""

import cmd
from models import storage
import shlex
import json
import re
from models.base_model import BaseModel
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.user import User




class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb)"
    __classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Place",
        "Amenity",
        "Review"
    }

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True
    
    def do_EOF(self, arg):
        """EOF command to exit the program"""
        print()
        return True

    def emptyline(self):
        """Do nothing on empty input line"""
        pass

    def default(self, arg):
        """Default behavior for cmd module when input is invalid"""
        # match = re.match(r"^([a-zA-Z_]\w*)\.([a-zA-Z_]\w*)\(\)$", arg)
        # match = re.match(r"^\s*([a-zA-Z_]\w*)\.([a-zA-Z_]\w*)\(\s*('.*'|\".*\"|[^\)]*)\s*\)\s*$", arg)
        match = re.match(r"^\s*([a-zA-Z_]\w*)\.([a-zA-Z_]\w*)\(\s*('.*'|\".*\"|[^\)]*)?\s*\)\s*$", arg)


        if match:
            class_name, method_name, method_arg = match.groups()
            method_arg = method_arg.strip('"\'')


        print(f"Debug: class_name={class_name}, method_name={method_name}, method_arg={method_arg}")
        

          # Access the __classes attribute using the mangled name
        if class_name in self._HBNBCommand__classes and hasattr(self, f"do_{method_name}"):
            if method_arg:
                call = f"{class_name}.{method_name}('{method_arg}')"
            else:
                 call = f"{class_name}.{method_name}({method_arg})"
            print(f"Debug: call={call}")
            return getattr(self, f"do_{method_name}")(call)
        print("*** Unknown syntax: {}".format(arg))
        return False

    

        
        if match:
            class_name, method_name = match.groups()
            print(f"Debug: class_name={class_name}, method_name={method_name}")

            # Access the __classes attribute using the mangled name
            if class_name in self._HBNBCommand__classes and hasattr(self, f"do_{method_name}"):
                call = f"{class_name}.{method_name}()"
                print(f"Debug: call={call}")
                return getattr(self, f"do_{method_name}")(call)

        print("*** Unknown syntax1: {}".format(arg))
        return False

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it to the JSON file, and prints the id"""
        if not arg:
            print("** class name missing **")
            return
        try:
            new_instance = eval(arg)()
            new_instance.save()
            print(new_instance.id)
        except NameError:
            print("** class doesn't exist **")
    
    # def do_show(self, arg):
    #     """Prints the string representation of an instance based on the class name and id"""
    #     args = shlex.split(arg)
    #     if not args:
    #         print("** class name missing **")
    #         return
    #     try:
    #         class_name = args[0]
    #         obj_id = args[1]
    #         key = "{}.{}".format(class_name, obj_id)
    #         print(storage.all()[key])
    #     except IndexError:
    #         print("** instance id missing **")
    #     except KeyError:
    #         print("** no instance found **")
    #     except NameError:
    #         print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints the string representation of an instance based on the class name and ID"""
        # match = re.match(r'^(\w+)\.show\(([^)]+)\)$', arg)
        # match = re.match(r'^\s*(\w*)\.show\((?:"([\w-]+)")?\)\s*$', arg)
        match = re.match(r'^\s*(\w+)\.show\(\s*[\'"]([\w-]+)[\'"]\s*\)\s*$', arg)
        match2 = re.match(r'^\s*(\w+)\s+([\'"]?[\w-]+[\'"]?)\s*$', arg)




        print(arg)
        

        if not (match or match2):
            print("Invalid syntax. Use: <class name>.show('<id>') or Usage: show <class> <id>")
            return
        
        class_name, instance_id = match.groups() if match else match2.groups()
        print(f"Debug: class_name={class_name}, method_name=show, method_arg={instance_id}")

        try:
            class_type = eval(class_name)
        except NameError:
            print(f"Class '{class_name}' doesn't exist.")
            return
        
        key = f"{class_name}.{instance_id}"

        print(key)

        if key in storage.all():
            print(storage.all()[key])
        else:
            print(f"No instance found with id '{instance_id}' in class '{class_name}'")

        
        return
        
        class_name = match.group(1)
        obj_id = match.group(2).strip("'\"")

        try:
            class_type = globals().get(class_name)
        except NameError:
            print(f"Class '{class_name}' doesn't exist.")
            return

        if class_type is None:
            print(f"Class '{class_name}' doesn't exist.")
            return

        key = "{}.{}".format(class_name, obj_id)
        obj = storage.all().get(key)

        if obj is None:
            print(f"No instance found with ID '{obj_id}' in class '{class_name}'.")
        else:
            print(obj)
        
    
    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id (save the change into the JSON file)."""
        # match_format = re.match(r'^\s*(\w+)\.destroy\(\s*[\'"]([\w-]+)[\'"]\s*\)\s*$', arg)

        match = re.match(r'^\s*(\w+)\.destroy\(\s*[\'"]([\w-]+)[\'"]\s*\)\s*$', arg)
        match2 = re.match(r'^\s*(\w+)\s+([\'"]?[\w-]+[\'"]?)\s*$', arg)

        if not (match or match2):
                print("Invalid syntax. Use: <class name>.show('<id>') or Usage: show <class> <id>")
                return
        
        class_name, instance_id = match.groups() if match else match2.groups()
        print(f"Debug: class_name={class_name}, method_name=show, method_arg={instance_id}")

        try:
            class_type = eval(class_name)
        except NameError:
            print(f"Class '{class_name}' doesn't exist.")
            return
        
        instances = storage.all()
        instance_key = "{}.{}".format(class_name, instance_id)

        if instance_key not in instances:
            print("No instance found.")
        else:
            del instances[instance_key]
            storage.save()
            
    # def do_destroy(self, arg):
    #     """Deletes an instance based on the class name and id, then saves the change into the JSON file"""
    #     args = shlex.split(arg)
    #     if not args:
    #         print("** class name missing **")
    #         return
    #     try:
    #         class_name = args[0]
    #         obj_id = args[1]
    #         key = "{}.{}".format(class_name, obj_id)
    #         del storage.all()[key]
    #         storage.save()
    #     except IndexError:
    #         print("** instance id missing **")
    #     except KeyError:
    #         print("** no instance found **")
    #     except NameError:
    #         print("** class doesn't exist **")


    def do_all(self, arg):
        """Prints all string representation of all instances based or not on the class name"""
        # Use regular expression to extract class name
        # match = re.match(r'^(\w+)(\.all\(\))$', arg)
        match = re.match(r'^(\w+)$|^(\w+)(\.all\(\))$', arg)
       

        if not match:
            print("Invalid syntax1. Use: <class name>.all()")
            return

        class_name = match.group(1) or match.group(2)
        print(class_name)
        print(self.__classes)
    

        if class_name not in self.__classes:
            print(f"Class '{class_name}' doesn't exist.")
            # print(f"class '{class_name}' exist")
            return
        
        # class_type = eval(class_name)
        # # class_type = globals()[class_name]


        # print(class_type)
        # return

        try:
            class_type = eval(class_name)
        except NameError:
            print(f"Class '{class_name}' doesn't exist.")
            return

        instances = []
        for obj_id, obj in storage.all().items():
            if type(obj).__name__ == class_name:
                instances.append(str(obj))

        print(f"Instances of {class_name}: {instances}")

    def do_count(self, arg):
        """Count the number of instances of a class"""
        match = re.match(r'^(\w+)(\.count\(\))$', arg)

        if not match:
            print("Invalid syntax. Use: <class name>.count()")
            return

        class_name = match.group(1)

        try:
            class_type = globals().get(class_name)
        except NameError:
            print(f"Class '{class_name}' doesn't exist.")
            return

        if class_type is None:
            print(f"Class '{class_name}' doesn't exist.")
            return

        count = 0
        for obj_id, obj in storage.all().items():
            if type(obj).__name__ == class_name:
                count += 1

        print(f"Number of instances of {class_name}: {count}")


            
    # def do_all(self, arg):
    #     """Prints all string representation of all instances based or not on the class name"""
    #     args = shlex.split(arg)
    #     print(f"Debug: args={args}")


    #     if not args:
    #         print("** class name missing **")
    #         return

    #     class_name = args[0]

    #     try:
    #         # Use eval to get the class type
    #         class_type = eval(class_name)
    #     except NameError:
    #         print("** class doesn't exist1 **")
    #         print(f"Debug: ** class doesn't exist: {class_name} **")

    #         return

    #     instances = []
    #     for obj_id, obj in storage.all().items():
    #         if type(obj).__name__ == class_name:
    #             instances.append(str(obj))

    #     print(instances)


    def do_update(self, arg):
        """Updates an instance based on the class name and id by adding or updating attribute"""

        # match = re.match(r'^(update\s+(\w+)\s+([a-zA-Z0-9-]+)\s+([a-zA-Z_]\w+)\s+"([^"]+)"|'r'(\w+)\.update\(([^)]+)\))$', arg)
        match = re.match(r'^(update\s+(\w+)\s+([a-zA-Z0-9-]+)\s+([a-zA-Z_]\w+)\s+"([^"]+)"|'
                     r'(\w+)\s+([a-zA-Z0-9-]+)\s+"([^"]+)"|'
                     r'(\w+)\.update\(([^)]+)\))$', arg)
       



        if match:
            groups = match.groups()
            class_name, obj_id, attr_name, attr_value = groups[1], groups[2], groups[3], groups[4]

        else:
            print("Invalid syntax. Usage: update <class> <id> <attribute_name> <attribute_value> or "
                "<class>.update(<id>, <attribute_name>, <attribute_value>) or "
                "<class>.update(<id>, <dictionary>)")
            return
        print(arg)
        return

        args = shlex.split(arg)
        if not args:
            print("** class name missing **")
            return
        try:
            class_name = args[0]
            obj_id = args[1]
            key = "{}.{}".format(class_name, obj_id)
            obj = storage.all()[key]
            if len(args) < 3:
                print("** attribute name missing **")
                return
            attribute = args[2]
            if len(args) < 4:
                print("** value missing **")
                return
            value = args[3]
            setattr(obj, attribute, value)
            storage.save()
        except IndexError:
            print("** instance id missing **")
        except KeyError:
            print("** no instance found **")
        except NameError:
            print("** class doesn't exist **")

if __name__ == '__main__':
    HBNBCommand().cmdloop()