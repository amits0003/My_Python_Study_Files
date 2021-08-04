#
#
# dict_list = {1: ['1'], 2: ['1', '2'], 3: ['2', '3'], 4: ['3']}
#
# # for index, value in enumerate(dict_list):
# #     print('index', index)
# #     print('value', value)
# #
# # for index , value  in enumerate(dict_list.values()):
# #     for i, v in enumerate(value):
# #         print(i)
# print(dict_list)
# print("Type of array : ", type(dict_list))
#------------------------------------------------------------------------------------#


dict_list_b = { 1 : { "Name" : "Amit",  "Age": 27, "Dept": "Development"},
                2 : { "Name" : "Sumit", "Age": 37, "Dept": "Testing"},
                3 : { "Name" : "Jack",  "Age": 34, "Dept": "Operation"},
                4 : { "Name" : "Rose",  "Age": 54, "Dept": "Finance"},
                5 : { "Name" : "Jill",  "Age": 22, "Dept": "Tax"},
                6 : { "Name" : "Smith", "Age": 54, "Dept": "Housing"},
                7 : { "Name" : "David", "Age": 30, "Dept": "Revenue"}}

#
# print(dict_list_b)
# print("Type of array : ", type(dict_list_b))

for index, value in enumerate(dict_list_b.values()):
    print("index : ", index)
    print("value : ", value)
