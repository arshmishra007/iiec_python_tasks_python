#!/usr/bin/python3.6
import cgi
import subprocess
print("content-type: text/html")
print()
mydata = cgi.FieldStorage()
myx=mydata.getvalue("command")
name=mydata.getvalue("myname")
passw=mydata.getvalue("pass")
if(name=='arsh' and passw=='arsh1234'):
  output=subprocess.getstatusoutput('sudo'+' '+myx)
  status=output[0]
  out=output[1]
  print(status)
  print(out)
else:
  print("Not the correct user")
