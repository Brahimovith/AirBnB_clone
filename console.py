#!usr/bin/python3
"""definition console"""
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.amenity import Amenity
import shlex

class HBNBCommand(cmd.Cmd):
    """"Defines the HolbertonBnB command interpreter.
    Attributes:
            prompt (str): The command prompt."""
    
    prompt = "(hbnb) "
    classes = ["BaseModel", "User", "City", "Place", "State", "Review", "Amenity"]

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True
    
    def do_EOF(self, arg):
        """end of file"""
        print("")
        return True
    def do_help(self, arg):
        """(type help <topic>)"""
        return super().do_help(arg)
    def emptyline(self):
        """saut ligne"""
        pass
    def do_create(self, arg):
        """cree un nouvel object"""
        c = shlex.split(arg)
        if not arg:
            print("** class name missing **")
        elif c[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            bm = eval(f"{c[0]}()")
            print("{}".format(bm.id))
            storage.save()
    def do_show(self, arg):
        """afficher object"""
        c = shlex.split(arg)
        if not arg:
            print("** class name missing **")
        elif c[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(c) < 2:
            print("** instance id missing **")
        else:
            o = storage.all()
            k = "{}.{}".format(c[0], c[1])
            if k in o:
                print(o[k])
            else:
                print("** no instance found **")
    def default(self, arg):
        """defaut"""
        liste = arg.split('.')
        cc = liste[0]
        comm = liste[1].split('(')
        m = comm[0]
        idd = comm[1].split(')')[0]
        dictio = {'count': self.do_count, 'all':self.do_all, 'show': self.do_show, 'update': self.do_update, 'destroy': self.do_destroy}
        if m in dictio.keys():
            return dictio[m]("{} {}".format(cc, idd))
        print("*** Unknown syntax: {}".format(arg))
        return False



    def do_destroy(self, arg):
        """detruire object"""
        c = shlex.split(arg)
        if not arg:
            print("** class name missing **")
        elif c[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(c) < 2:
            print("** instance id missing **")
        else:
            o = storage.all()
            k = "{}.{}".format(c[0], c[1])
            if k in o:
                del o[k]
                storage.save()
            else:
                print("** no instance found **")
    def do_all(self, arg):
        """all object"""
        o = storage.all()
        c = shlex.split(arg)
        l=[]
        if not arg:
            for k, v in o.items():
                l.append(str(v))
            print("{}".format(l))
        elif c[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        else:
            for k, v in o.items():
                if k.split('.')[0] == c[0]:
                    l.append(str(v))
            print("{}".format(l))
    def do_count(self, arg):
        """count objects"""
        o = storage.all()
        count = 0
        c = shlex.split(arg)
        if c:
            if c[0] in HBNBCommand.classes:
                
                for i in o.values():
                    if i.__class__.__name__ == c[0]:
                        count = count + 1
                print(count)
            else:
                print("*** invalid class name ***")
        else:
            print("*** class name missing ***")     

    def do_update(self, arg):
        """update objects"""
        c = shlex.split(arg)
        if not arg:
            print("** class name missing **")
        elif c[0] not in HBNBCommand.classes:
            print("** class doesn't exist **")
        elif len(c) < 2:
            print("** instance id missing **")
        else:
            o = storage.all()
            k = "{}.{}".format(c[0], c[1])
            if k not in o:
                print("** no instance found **")
            elif len(c) < 3:
                print("** attribute name missing **")
            elif len(c) < 4:
                print("** value missing **")
            else:
                oo = o[k]
                n = c[2]
                val = c[3]
                try:
                    val = eval(val)
                except Exception:
                    pass
                setattr(oo, n, val)
                oo.save()
        



if __name__ == '__main__':
    HBNBCommand().cmdloop()

