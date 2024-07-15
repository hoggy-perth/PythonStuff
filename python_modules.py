# This prints out a full list of the python built in modules
# https://docs.python.org/3/library/sys.html
import sys

def print_hi(name):
    print(f'{name}')

if __name__ == '__main__':
    modules = sys.builtin_module_names
    #Quesion is what type of variable is modules?
    print_hi(modules)
    #modules variable is a Tuple.
    print(type(modules))
    #So how to deal with Tuples
    #Tuple items are ordered, unchangeable, and allow duplicate values.
    print(len(modules))
    #Freaky for loop syntax works out the tuple contents
    #Use the index method to get the current tuple number 
    for x in modules:
        z=modules.index(x) #index is method for objects of index Type
        print(z,x)
