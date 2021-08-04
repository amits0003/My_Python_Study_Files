from builtins import *

def check_for_duplicates(list_of_Elements):
    if len(list_of_Elements) == len(set(list_of_Elements)):
        return False
    else:
        return True

list_Elements = ['ok','ok','notok',1,2,3,4]

temp = set(list_Elements)
print(temp)

result = check_for_duplicates(list_Elements)

if result:
    print("Duplicates Noted")
else:
    print("duplicates not noted")