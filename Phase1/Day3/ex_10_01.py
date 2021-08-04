'''10.2 Write a program to read through the mbox-short.txt and figure out the distribution by hour of the day 
for each of the messages. You can pull the hour out from the 'From ' line by finding the time and then splitting the string a second time using a colon.
From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Once you have accumulated the counts for each hour, print out the counts, sorted by hour as shown below.'''

#file_name = input("Enter the filename : ")

#file_open = open(file_name,'r')

file_open = open('mbox-short.txt','r')
hours_list = []
hour_dict = {}
for line in file_open:
    if line.startswith('From'):
        if line.startswith("From:"):
            continue
        temp_list = line.split()
        temp_list.reverse()
        hour_word = temp_list[1].split(":")[0]
        hours_list.append(hour_word)
        hours_list.sort(reverse=False)
 
for hours in hours_list:
    hour_dict[hours] = hour_dict.get(hours, 0) + 1
  
for key, value in hour_dict.items():
    print(key,value)