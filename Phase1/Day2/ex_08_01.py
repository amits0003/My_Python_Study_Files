# 8.4 Open the file romeo.txt and read it line by line. For each line, split the line into a list of words using the
# split() method. The program should build a list of words. For each word on each line check to see if the word is
# already in the list and if not append it to the list. When the program completes, sort and print the resulting
# words in alphabetical order. You can download the sample data at http://www.py4e.com/code3/romeo.txt


# file_name = input("Enter File Name: ")

# file_handle = open(file_name,'r')
file_handle = open('romeo.txt', 'r')

words_list = []
temp_list = []
unique_word_list = []
counter = 0
for line in file_handle:
    # Removing the while spaces and extra lines
    stripped_line = line.strip()

    # making a temporary list after splitting the words
    temp_list = stripped_line.split()

    words_list = words_list + temp_list

# print(words_list)

for word in words_list:
    if word not in unique_word_list:
        unique_word_list.append(word)

unique_word_list.sort()

print(unique_word_list)
