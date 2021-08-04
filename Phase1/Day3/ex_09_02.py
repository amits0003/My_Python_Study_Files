from builtins import *

def check_duplicates_in_list(list_of_elememts):
    set_of_elements = set()
    
    for elements in list_of_elememts:
        if elements in set_of_elements:
            return True
        else:
            set_of_elements.add(elements)

    return False

def check_duplicates_using_count(listof_element):
    for elements in listof_element:
        if listof_element.count(elements) > 1:
            return True
        return False    
        
list_Elements = ['ok','ok','notok',1,2,3,4]

#result = check_duplicates_in_list(list_Elements)

result = check_duplicates_using_count(list_Elements)
 
if result:
    print("Duplicates Noted")
else:
    print("duplicates not noted")