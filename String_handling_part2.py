
#1.capitalize()
s="python"
snew =s.capitalize()
print(snew,type(snew))

s="python is an oop lang"
scap=s.capitalize()
print(scap)

s ="python is an oop lang.python is a fun lang"
sc = s.capitalize()
print(sc)

#2.title()

s="python"
snew=s.title()
print(snew)

s="python is an oop lang"
snew =s.title()
print(snew)

s="python is an oop lang.python is a fun lang"
snew=s.title()
print(snew)

#3.upper()

s="python"
print(s.upper())
s="python"
print(s,id(s))
s=s.upper()
print(s,id(s))

#4.lower()
s="PYTHON"
print(s,id(s))
s=s.lower()
print(s,id(s))

s="PYthon"
print(s,id(s))
s=s.lower()
print(s,id(s))

#5.swapcase()

s="pyThOn"
print(s,id(s))
s=s.swapcase()
print(s,id(s))

s="PYTHON is A oop LANG"
print(s,id(s))
s=s.swapcase()
print(s,id(s))

#6.islower()

s="python"
print(s.islower())

s="python is a oop lang"
print(s.islower())

s=s.upper()
print(s.islower())

s="Python"
print(s.islower())
s="1234"
print(s.islower())
s="@#$%^"
print(s.islower())

#7.isupper()

s="PYTHON"
s=s.isupper()
print(s)

s="Python"
print(s.isupper())

s="@#$%"
print(s.isupper())

s="1234"
print(s.isupper())

#8.isspace()

s=""
print(s.isspace())
s="12 34"
print(s.isspace())
s="python is an oop lang"
print(s.isspace())
s=""
print(s.isspace())
s='  '
print(s.isspace())

#9. isdigit()

s="1234"
print(s.isdigit())
s="Python1234"
print(s.isdigit())

# 10.isalpha()

s="Aman Kumar"
print(s.isalpha())
s="Amankumar"
print(s.isalpha())
s="Aman123"
print(s.isalpha())

s="aman"
print(s.isalpha())
s="@#$%"
print(s.isalpha())

#11.isalnum()

s="123"
print(s.isalnum())
s="Python123"
print(s.isalnum())
s="Python 123"
print(s.isalnum())

s="12 23"
print(s.isalnum())

# 12.index()

s="PYTHON"
print(s.index("y"))

 File "<input>", line 2, in <module>
ValueError: substring not found

print(s.index("Y"))

print(s.index("S"))
 File "<input>", line 1, in <module>
ValueError: substring not found

print(s.index("P"))

s="MISSISSIPPI"

print(s.index("I"))

for index,val in enumerate(s):
    print(index,'--->',val)

s="ABRAKADABRA"
print(s.index("R"))
 for index,val in enumerate(s):
     print(index,"--->",val)
for index,val in enumerate(s):
    if(val=='B'):
        print(index,"--->",val)
s=set(s)#Set removes duplicates from strings.Set does'nt support index()
print(s)
for index,val in enumerate(s):
    print(index,val)


