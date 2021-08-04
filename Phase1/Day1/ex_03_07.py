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
        for i in input_array:
            if i > converted_value:
                converted_value = i
                largest_value = converted_value
        for i in input_array:
            if i < converted_value:
                converted_value = i
                smallest_value = converted_value
    except ValueError or AttributeError or NameError as e:
        print("Invalid input : ", e)
        continue

print("Maximum value is", largest_value)
print("Minimum value is", smallest_value)

# calculating maximum and minimum through max and min operator
lar_val = max(input_array)
small_val = min(input_array)

print("New Max (through new way): ", lar_val)
print("New Min: (through new way)", small_val)
