txt = "python programming"
slice = txt[::-2]
print(slice)

#conversion of letter form string
print(txt.upper())
print(txt.lower())
print(txt.title())
print(txt.capitalize())

#method to remove space form string
a = "   shubh gangwar   "
msg = a.strip()
print(msg)
print(a.lstrip())
print(a.rstrip())


##method to find the character is exit or not in string
#string.find(subsring, start, end)
#1 txt.find()
txt = "Python is amazing, Python is fun"
#idx = txt.find("python")
#print(idx)
print(txt.find("Python"))
print(txt.find("fun"))
print(txt.find("is"))
print(txt.find(","))
print(txt.find("is",19))
print(txt.find("Python",19))

## how much time repeat
#string.count(subsring, start, end)
print(txt.count("Python"))
#print(txt.index("shubh"))

print(txt.find("shubh"))

#Replaced string
# txt.replaced(old,new,count)

txt = "hello wrold"
print(txt.replace("wrold" , "pyhton"))

txt = "apple apple apple"
print(txt.replace("apple" , "banana" , 2))

#method to check alphabet, numeric
#example
text1 = "shubh"
text2 = "shubh2"
print(text1.isalpha())
print(text2.isalpha())

print(text1.isalnum())
print(text2.isalnum())

text1 = "234"
text2 = "2python"
print(text1.isdigit())
print(text2.isdigit())
#islower(), islower()

#to check space
txt = "   "
print(txt.isspace())


#startswitn and endwith
#example
text = "python is amazing"
print(text.startswith("python")) #true
print(text.endswith("fun")) #false
print(text.endswith("is", 0, 9))  #also check from here to there

#method to split 
#example
text ="apple,banana,oranges,grapes" #collection
print(text.split(","))
text = "python is fun to learn"
print(text.split())

#convert a list into a string
#example
li = ['apple', 'banana', 'oranges', 'grapes']
print(",".join(li))
print("|".join(li))

# .format() method
name = "shubham"
msg = ("my name is {}".format(name))
print(msg)
msg = "my name is {} and my age is {}".format(name,23)
print(msg)

print("my name is {0} and my age is {1}".format(name,23))

print("my name is {p1} and my age is {p2}".format(p1=name,p2=25)) #here we use parameters
print("my name is {p1} and my age is {p2}".format(p1="rahul",p2=25))



#old style formatting with %operator
#"string with format specifier" % values
#example
name = "shubh"
message = "hello, %s!" % name
print(message)

age = 24
message = "hello, i am %d years old" % age  # %d, %s they are format specaier like %s is used for string and %d is used for integer
print(message)


name = "shubh"
age = 24
message = "hello, my name is %s and i am %d year old" %(name,age)
print(message)

pi = 3.1234
print("pi ronded to 2 decimal places: %f" %pi)




