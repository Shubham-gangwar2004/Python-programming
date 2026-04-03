# string is a sequence of characters enclosed within quotes
#charcters incluldes Letter, Number, Spcial Smybols, whitespace characters and Unicode characters

str1 = 'jkbwjfb mnwef jjbwdjwb4 423'
print("\U0001F622")     # Unicode = \U0001F622


language = "pyhton"
print(language[4])

name1 = "pyhton"
name2 = "pyhton"

print(name1 == name2)  # Boolean


#Song = "Juda hoke bhi tu mujh mein kahin baaqi hai \n Palkon mein ban ke aansoon tu chali aati hai \n Juda hoke bhi tu mujh mein kahin baaqi hai \n Palkon mein ban ke aansoon tu chali aati hai"
#print(Song)

Song1 = '''Juda hoke bhi tu mujh mein kahin baaqi hai
Palkon mein ban ke aansoon tu chali aati hai
Juda hoke bhi tu mujh mein kahin baaqi hai
Palkon mein ban ke aansoon tu chali aati hai'''   #or maye be used double quotes three times

print(Song1)




print("hel\"p")
print("hel\np")
print("hel\\np")
print("hel\tp")



#srting concatenation


a = 1 
b = 2 
print(a + b)


a = "1"
b = "2"
print(a + b)


first_name = "Shubham"
last_name = "Gangwar"
print(first_name + " " + last_name)




age = 21
#message = "my age is" + " " + str(age)
message = "my age is " + str(age)
print(message)




city = "bareilly"
temp = 75
weather_report = "the temperature in " + city + " is " + str(temp) + " degree"
print(weather_report)

weather_report = f"The temperature in {city} is {temp} degree"
print(weather_report)
print(f"The temperature in {city} is {temp} degree")


a = "shubh"
res = a * 3
print(res)


star = "*"                         # ******
print(star*5)                       #******
print((star * 5 + "\n") * 5)

# pypythonthon
print("py" *2 + "thon" *2)


# len

a = "length"
#print(len(a))  
length = len(a)
print(length)


#compariosn
msg = "shubham"
res = len(msg) >= 8
print(res)



print("shubh" == "shubh")
print("shubh" == "Shubh")
print("shubh" == "shashi")
print("shubh" != "shashi")


print("a" > "b")
print("a" < "b")
print("a" > "A")
  



  # String Indexing and slicing
txt = "python"
#print(txt[len(txt)])  will give error due the out of range
#print(txt[6]) 
print(txt[len(txt) - 1])
print(txt[len(txt) - 2])

# Slicing
# string[start:end:step]
# start - inclusive
# end - exclusive

txt = "python programming"
slice = txt[0:5]  # n is exclusive so it cant be count
slice = txt[0:6]
slice = txt[:6]
print(slice)
slice = txt[7:18]

slice = txt[7:]
print(slice)

print(txt[0:6:2])

txt = "dasmathansda"
slice = txt[0:13:2]
print(slice)