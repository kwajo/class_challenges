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



class structure:
    def __init__(self,name,height):
        self.name = name
        self.height = height

    def valid(self):
        try:
            self.name = str(self.name) 
            self.height = int(self.height)
            if self.height > 0:
                return True
            return False
        except:
            return False

'''
this class contains an empty list for storing structures
it also has a precalculated total height
'''
    

class structure_manager:
    def __init__(self):
        self.structures = []
        self.totalHeight = int(0)
       
    def add_structure(self,structure):
        self.structures.append(structure)
        self.totalHeight = self.totalHeight + structure.height
    
    def list_structures(self):
        return self.structures

    def return_height(self):
        return self.totalHeight
    
    def print_data(self):
        for struct in self.structures:
            print (struct.name)
            print (struct.height)
        print (self.totalHeight)



'''
the main function manages the operations between 
the structure and structure manager class all

'''

def main():
    print("python main function")


    sm = structure_manager()


    Eiffel = structure('Eiffel tower', 100)
    Taj = structure('Taj Mahal', 50)
    Big = structure('Big Ben',45)


    sm.add_structure(Eiffel)
    sm.add_structure(Taj)
    sm.add_structure(Big)

    struct_list = sm.list_structures()



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
