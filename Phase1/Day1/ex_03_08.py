input_array = []

while True:
    input_value = input("Enter the Number")
    if input_value == 'done':
        break

    converted_value = int(input_value)
    input_array.append(converted_value)
    print(input_array)
