#'''this program is showing use of CGI in Python '''

import cgi, cgitb

#''' Create instance of Field Storage'''
form = cgi.FieldStorage()

#'''Get Data From Fields'''

first_name = form.getvalue('first_name')
last_name = form.getvalue('last_name')

submit_value = form.getvalue('Submit')
if submit_value == "Submit":
    print ('Content-type:text/html\r\n\r\n')
    print ("<html>")
    print ('<head>')
    print ("<title> First CGI Program </title>")
    print ("</head>")
    print ("<body>")
    print ("<h2>Hello %s %s </h2>" % (first_name, last_name))
    print ("</body>")
    print ("</html>")
