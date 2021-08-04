
tup_a = ("1", 2, )
tup_b = (2, )
list_a = [1, 2, 3, 4, 5]
list_b = [6, 7, 8, 9]

print('original list: ', list_a)

def cloneList(list_i):
    temp_list_a = []
    temp_list_a = temp_list_a.extend(list_i)

    return temp_list_a


print("Extended List type 1: ", cloneList(list_b))

print("Extended List type 2: ", list_a)

# temp_list_b = list_a
# temp_list_b.extend(list_b[len(list_b):] )
#
# print( "Extended List type 2: " , list_a )