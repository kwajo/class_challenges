'''
Research the heights of the following structures:

-   Eiffel Tower
-   Big Ben
-   Taj Mahal

Create a python script which:

-   Declares a variable for each structure's height 
-   Prints the name and height of each structure
-   Calculates and prints the total height of all three structures added together

Extension Task

-   Define a function which adds three numbers
-   Prompts the user to enter the height for each structure and prints the total height 
-   Handle users entering negative numbers
'''



'''
KWAJO's Notes ~~~

If I could get some feedback on commenting as well as code that would be great.
'''


'''
---(structure)---

the structure is a class for building structure objects
the object contains a name variable and a height variable

variables:
    * name (typeless)
    * height (typeless)

methods:
   
    * init
    * valid (boolean)


    [init] initalizes an object with a given *name* and *height*

    [valid] will return True for a valid *structure* otherwise returns False.
     A *structure* is valid if the folling conditions are met:
   
    *name* is a string
    *name* length is below 32

    *height* is a positive integer below 20000

'''
class structure:

    '''
    initialize new structure object
    '''
    def __init__(self,name,height):
        self.name = name
        self.height = height

    '''
    is valid structure. This checks to see if the structure is valid
    '''
    def valid(self):
        try:
            self.name = str(self.name) 
            self.height = int(self.height)
            if self.height > 0 and len(self.name) <= 32 and self.height < 20000 and is_ascii_string(self.name):
                return True
            return False
        except:
            return False

'''
calls is_ascii_between function on each char in _str. This function is dedicated to checking that a character
is either a number, letter or space for the purpose of the challenge
'''
def is_ascii_string(_str):
    for c in _str:
        if (not is_ascii_between('a','z',c)) and (not is_ascii_between('A','Z',c)) and (not is_ascii_between('0','9',c)) and (not is_ascii_between(' ',' ',c)):
            return False
    return True


'''
returns True if c is an ascii value between min and max otherwise returns False
'''
def is_ascii_between(min,max,c):
    return (ord(c) >= ord(min) and ord(c) <= ord(max))


'''
---(structure_manager)---

The structure manager class is a class for holding structures and performing operations on groups of structures.
The class contains the following functions

variables:
    * structures[] (typeless)
    * total_height (type int)

methods:
    *init
    *add_structure
    *list_structures
    *return_heightf
    *print_data

    [init] initializes structure manager object with empty values

    [add_structure] appends a *structure* to the managers *structures[]* list. This function will add 
    structures that are not valid as defined by the structure.valid() function so validation must be
    handled externally.
    
    [list_structures] returns the *structures[]* list

    [return_height] returns the precalculated height of all *structure* in the *structures[]* list

    [print_data] prints  structure.name and structure.height of all *structure* in *structures[]* list
    then prints *total_height*

'''
    

class structure_manager:

    '''
    initialize empty *structure_manager* instance
    '''
    def __init__(self):
        self.structures = []
        self.totalHeight = int(0)
    
    '''
    add a *structure* to *structures[]*
    '''
    def add_structure(self,structure):
        self.structures.append(structure)
        self.totalHeight = self.totalHeight + structure.height
    '''
    *structures[]* get method
    '''
    def list_structures(self):
        return self.structures

    '''
    *totalHeight* get method
    '''
    def return_height(self):
        return self.totalHeight
    '''
    data dump for all *structures* in *structures[]*
    '''
    def print_data(self):
        for struct in self.structures:
            print (struct.name)
            print (struct.height)
        print (self.totalHeight)



'''
---(main)---
1)
this code will setup a *structure_manager* instance , create 3 *structure* instaces and 
populate the the structure_manager with the three structure instances if they are valid.
It will then print the information of all strucures in the structure manager.


2)
Allows the user to continue adding structures to the structure manager for as long as desired.
'''

def main():
    

    #0)
    '''
    tests because Idk how to write tests in python yet.
    
    print(is_ascii_between('a','z','f')) #true
    print(is_ascii_between('a','`','f')) #false

    print(is_ascii_between('A','Z','Q')) #true
    print(is_ascii_between('A',';','Z')) #false

    print(is_ascii_between('0','9','3')) #true
    print(is_ascii_between('0','9','>')) #false

    print(is_ascii_string('asdasdsadasdDSADASDASD88asd')) #true
    print(is_ascii_string('ASDSADAS9asdasd(d')) #false
    '''
    #1)



    sm = structure_manager()


    Eiffel = structure('Eiffel Tower', 100)
    Taj = structure('Taj Mahal', 50)
    Big = structure('Big Ben',45)

    

    sm.add_structure(Eiffel) if Eiffel.valid() else print('idk how this fucked up')
    sm.add_structure(Taj) if Taj.valid() else print('idk how this fucked up')
    sm.add_structure(Big) if Big.valid() else print('idk how this fucked up')

    sm.print_data()
    #struct_list = sm.list_structures()


    #2)
    while input('Would you like to add a another structure (y) or any key to escape') == 'y':
        name = input("Structure_name: ")
        height = input('Structure_height: ')
        struct = structure(name,height)
        sm.add_structure(struct) if struct.valid() else print('invalid input')
    sm.print_data()
'''
Code execution starts here
'''
if __name__ == '__main__':
    main()
