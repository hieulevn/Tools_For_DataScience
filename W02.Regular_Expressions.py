#From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
#Received: from prod.collab.uhi.ac.uk ([194.35.219.182])
#To: source@collab.sakaiproject.org
'''x="From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008"
print(x)
space1=x.find(" ",0,len(x))
space2=x.find(" ",space1+1,len(x))
email=x[space1+1:space2]
print(email)'''

'''import re
fopen=open("mbox-short.txt")
for line in fopen:
    line=line.rstrip()
    if re.search("^From:",line):
        print(line)'''

import re
x='From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
y=re.findall('[0-9]+',x)
z=re.findall('\S+@\S+',x)
z2=re.findall('From (\S+@\S+)',x)
print(y)
print(z)
print(z2)