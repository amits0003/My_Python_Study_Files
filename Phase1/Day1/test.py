input_array = []
smallest_value = -1
largest_value = -1
while True:
        input_value = input("Enter the Number: ")
        if input_value == 'done':
            break
        try:
            converted_value = int(input_value)
            input_array.append(converted_value)
        except:
            print("invalid data")
            continue        
        #print(input_value)

for i in input_array:
    if i > converted_value:
            converted_value = i
            largest_value = converted_value
print("largest number = ", largest_value)
for i in input_array:
    if i < converted_value:
            converted_value = i
            smallest_value = converted_value
print("smallest number = ", smallest_value)
    
print(input_array)
