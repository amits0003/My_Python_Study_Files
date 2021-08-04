
'''this  program uses Regular expressions'''

import re

line = input("Enter a line: ")

match_obj = re.match( r'[a-e]', line, re.M|re.I )
search_obj = re.search(r'[a-e]', line, re.M|re.I )
if match_obj:
    print("matches found : ", match_obj.group())
elif search_obj:
    print("Search found, searched keyword : ", search_obj.group() )
else:
    print("No Match")

c_ob = re.search(r'[ab+]', line)

print(c_ob.group())


#-------------------------------------------------------------------------------------------------------------------------------------------
# import re
#  
# line = "Cats are smarter than dogs"
#  
# matchObj = re.match( r'(.*) are (.*?) .*', line, re.M|re.I)
# res1 = matchObj.group()
# res2 = matchObj.group(1)
# res3 = matchObj.group(2)
# if matchObj:
#    print ("matchObj.group() : ", res1)
#    print ("matchObj.group(1) : ", res2)
#    print ("matchObj.group(2) : ", res3)
# else:
#    print ("No match!!")
#     