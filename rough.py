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


x = True
print(type(x))


name1 = "shubh"
name2 = "Shubh"
print(name1==name2)

a = "\\User\\Vipul\\Documnet"
print(a)

age = 22
message = "my age is " +  str(age) 
print(message)

temp = 89
city = "bareilly"
#message = "the temperture in " + str(city) + " is " + str(temp)
#print(message)

print(f"the temperture in {city} is {temp} degree)")

name = "shubh"

print(f"first charcter of {name} is {name[0]}")


star = "*"
#(star*5)
#(star*5)+"\n"
print((star*5 +"\n")*5)
print("py"*2 + "thon"*2)



print(len("pyhton"))
print(ord("s"))
name = "shubhm"
print(name[len(name) -1])

print(name[-1])
print(name[5])

name = "shubham gangwar"
print(name[::2])
print(name[::-2])

txt = "shubham gangwar"
print(txt.upper())

name = " shubh is shubh , i am shubh"
print(name.count("shubh"))

age = 22
name = "shubh"
message = "hello, my name is {} and i am {} year old".format(name,age)
print(message)
name = "shubh"
message = "hello, %s" % name
print(message)


s = "hello"
print(s[1:])
print("M" + s[1:])
t = "     poython programmin SKILLS    "
print(t.strip().title().replace("Skills","Expertise"))

s = "Python Programming language"

print(s[::2])
print(s[::-1])
print(s[-20:-9])

text = "python is easy to learn"
message = text[0] + text[7] + text[10] + text[15] + text[18]
print(message)

#palindrome check
word = "radar"
print(word==word[::-1])

 

text = "mississippi"
print(text.count("i"))
print(text.count("s"))
print(text.count("p"))

a = 0b100000
print(a)
print(type(a))

a = 10_000_000
print(a)

a =1000
print(bin(a))

a = 10
b = 6
print(f"additon of {a} and {b} : {a+b}")
print(f"subtraction of {a} and {b} : {a -b}")
print(f"multiplcatio of {a} and {b} : {a*b}")
print(f"divided of {a} and {b} : {a/b}")
print(f"divided of {a} and {b} : {a//b}")
print(f"module of  {a} and  {b} : {a%b}")
print(f"negotation of {b} : {-b} ")
print(f"power of {a} and {b} : {a**b}")
print(f"abs value {b} and {a} : {abs(b-a)}")
bitwise_and = a & b
print(f"bitwise of {a} and {b} : {bitwise_and}")
bitwise_or = a | b
print(f"bitwise of {a} | {b}: {bitwise_or}")
bitwise_xor = a ^ b
print(f"bitwise of {a} ^ {b}: {bitwise_xor}")


# when we have to swap no.


# x = int(input("enter the no.: "))
# y = int(input("enetr the no.: "))
# temp = x
# x = y
# y = temp
# x , y = y , x
# print(x , y)
salary = 11
salary **=2
print(salary)
a = 7
print(float(a))

electron_mass = 9.11e-31
print(f"the mass of electron is {electron_mass}")
pi = 3.14151616
print(f"the valuse of pi : {pi:.2f}")
print(round(pi, 3 ))

a = 1+2j
print(float(a.real))
print(int(a.real))
print(a.imag)
a = complex(2,3)
print(a.real)
print(a.imag)

has_adhar = True
age = 18
print(has_adhar and age >=18)

has_dl = True
has_adhar = False
print(has_dl or has_adhar)


injury = True
print(not injury)

working_age = 21
is_eligible = 60>=age>=18



# age = int(input("enter the age: "))
# if age>=18:
#     print("you are an adult")
# print("you are nit adult")

temp = 9 #int(input("enter the temp: "))
is_raining = True #bool(input("leave empty if not raining else type anything"))
if (temp<=10 and is_raining):
    print("wear a jacket")

word = "radar"
print(word==word[::-1])

age = 19
password = "vjgnvyyv" #(input("Enter the pass: "))
if age>=18:
    if len(password)>=8:
        print("valid")
    else:
        print("not valid")


else:
    print("you are kid")


x = 12 #int(input("Enter the no.: "))
if x % 2==0:
    print("even")
else:
    print("odd")
