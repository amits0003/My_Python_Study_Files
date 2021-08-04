import gc

before = gc.get_objects()
list_B = []
list_A = []
with open('sample_file.txt', 'w') as file:
    for i, v in enumerate(before):
        list_B.append(v)
        list_A.append(i)
    for i_ in enumerate(list_A):
        print(i_)
        file.write(str(i_))
    for i__ in enumerate(list_B):
        file.write(str(i__))