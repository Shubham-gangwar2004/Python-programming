a = 9
b = 5
print(a+b)


a = 9
b = 3
print(a-b)

city = "bareilly"
temp = 45
#message = the temperature in bareilly is 45 degree
message = "the temperature in " + str(city) + " is " + str(temp) + " degree"
print(message)
message = f"the temperature in {city} is {temp} degree"
print(message)
 
#name = don't worry about it.
name = 'don\'t worry about it'
print(name)
name = 'don\n''t worry about it'
print(name)
name = 'don\'t\nworry about it'
print(name)
name = 'dont w\norry about it'
print(name)

a = "C:\\Users\\shubh\\OneDrive\\Documents\\Custom Office Templates" 
print(a)
age = 22
meassage = "i am " + str(age) + " year old"
print(meassage)
message = f"i am {age} year old"
print(meassage)

name = "vipul"
print(f"first letter of {name} is {name[0]} ")

#this is curly a barce : { print it
print(f"this is curly a barce : {{")

a = "*"
print((a * 5 + "\n" ) *6)
#pytpytthonthon
print("pyt"*2 + "thon"*2)

name = "shubham gangwar"
print(name[3])
print(name[8])
print(len(name))
print(name[-3 : 7])
print(name[3 : 7])

print(name[::2])

print(name[::-1])


name = "shubham gangwar"
print(name.upper())
print(name.lower())
print(name.title())
print(name.capitalize())

name = "   this is the end     "
print(name.strip())
print(name.lstrip())
print(name.rstrip())

name = "my name is shubh"
print(name.find("shubh"))
name = "python is amazing, python is good"
print(name.find("python"))
print(name.find(","))
print(name.find("is", 19))
print(name.count("python"))