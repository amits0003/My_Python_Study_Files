#5.2 Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. 
#Once 'done' is entered, print out the largest and smallest of the numbers. If the user enters 
#anything other than a valid number catch it with a try/except and put out an appropriate message 
#and ignore the number. Enter 7, 2, #bob, 10, and 4 and match the output below.

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
        print("Invalid input")
        continue        

for i in input_array:
    if i > converted_value:
        converted_value = i
        largest_value = converted_value
print("Maximum is", largest_value)
for i in input_array:
    if i < converted_value:
        converted_value = i
        smallest_value = converted_value
print("Minimum is", smallest_value)

            
