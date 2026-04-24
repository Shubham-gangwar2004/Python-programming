#s = input()
#print("Hello, " + s)
#txt = "python"
#
# 
# print(txt[6])
a = 2
print(a*3)


star = "*"
print(((star*5) + "\n") *5)

print("shubh" * 2 + "bham" * 2)




print("hello world")

a = 5
b = 10
print(a + b)
 
num = 7
print(num ** 2)



num = 12
if num % 2 == 0:
    print("true")
else:
    print("false")


for i in range(1,11):
    print(i)


a = 20
b = 15
if(a>b):
    print("true")
else:
    print("false")



num  = -5
if num > 0:
    print("postive")
else:
    print("negative")



a = "python"
print(len(a))


num = 4
print(num ** 3)

num = 2
print


city = "bareilly"
temp = 45
msg = "The temperature in " + city  + " is "  + str(temp) + " degree "
print(msg)



a = " shubh"
length = len(a)
print(length)



a = "programmimg"
print(a[len(a) - 1])

a = "shubham gangwar"
b = a[0:]
print(b)
li = ['apple', 'banana', 'oranges', 'grapes']
print(",".join(li))
print("|".join(li))



a = 7
b = 5
if (a>b):
    print(a)
else:
    print(b)



num = 15
if num % 3 == 0:
    print("true")
else:
    print("False")


a = "python"
slice = a[0:6:2]
print(slice)

x = 10
print(type(x))
language = "python"
print(language[2])

poem = "The small book of poems for kindergartens \n and primary schools was published in Tatarstan by the branch \n of the Earth Charter Affiliate in Russia, the Russian Center for"
print(poem)
message = '''The small book of poems for kindergartens
 and primary schools was published in Tatarstan by the 
 branch of the Earth Charter Affiliate in Russia, the Russian Center for'''
print(message)
 
age = 22
message = ("my age is " + str(age))
print(message)

city = "bareilly"
temp = 30
message = "the temperture in " + str(city) + " is " + str(temp) + " degree"
print(message)
print(f"the tempereture in {city} is {temp} degree")


a = "*"
print((a*5 +"\n")*5)
# a = "shubh"
print("shu"*2 + "bh"*2)
name = "shubham"
message = (len(name)<=7)
print(message)
# this is curly: {
print(f"this is curly: {{")


b = "python"
print(b[len(b)-1])

a =" shubham gangwar"
print(a[::-2])
a = " my anme is shubh and i am shubh"
# print(a.find("i",18))
#print(a[1])
print(a.count("java"))
print(a.count("shubh"))
a = "hello this is me"
print(a.startswith("hello"))
print(a.startswith("this"))
print(a.endswith("me"))

a = "shubh shubh shubh"
print(a.replace("shubh","tanya",3))

list = ["apple","shubh","hello"]
print(",".join(list))
a ="apple,shubh,hello"
print(a.split(" "))
name = "shubh"
age = 13
# memoryview = "hello my name is {} and i am {} year old".format(name,age)
print("hello my name is {} and i am {} year old".format(name,age))

name = r"\Users\shubh\OneDrive\Documents\Custom Office Templates"
print(name)

a = "python programming"
print(a[::2])
print(a[::-1])
text = "mississippi"
print(text.count("i"))