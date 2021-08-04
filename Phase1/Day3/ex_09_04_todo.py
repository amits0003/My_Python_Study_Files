'''9.4 Write a program to read through the mbox-short.txt and
figure out who has sent the greatest number of mail messages. The program looks for 'From ' lines and takes the second word of those lines
as the person who sent the mail. The program creates a Python dictionary that maps the sender's mail address to a count of the number of times
they appear in the file. After the dictionary is produced, the program reads through the dictionary using a maximum loop to find the most prolific committer.
'''
from builtins import *
from turtledemo.clock import wochentag

#file_name = input("Enter the File Name: ")

#file_opened = open(file_name,'r')
file_opened = open('mbox-short.txt','r')
word_dict = {}
temp_list = []
for line in file_opened:
    if line.startswith('From'):
        if line.startswith('From:'):
            continue
        word_list = line.split()
        word_selected = word_list[1]
        word_dict[word_selected] = word_dict.get(word_selected, 0) + 1
        temp_list.append(word_selected)

highest_word = None
highest_count = None

for key, value in word_dict.items():
    if highest_count is None or value > highest_count:
        highest_word = key
        highest_count = value

print(highest_word,highest_count)
