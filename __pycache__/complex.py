#iota a+bi here we represents by j
z = 1 + 2j
print(z)
print(z.real)
print(int(z.imag))

z1 = 1 + 2j
z2 = 1 - 2j
print(z1 + z2)
print(z1 - z2)
print(z1 * z2)

#alsomdo by using  complex 
z = complex(1, 3)
print(z)


#boolean operator
a = True
print(type(a))


age = 17
is_adult = age>= 18
print(is_adult)

#bool is a subclass of int
print(True==0)
print(False==1)
print(True+True)
print(int(True))
print(int(False))
print(bool(1))
print(bool(0))

#every boolean is an integer

print(isinstance(True, int))

#every int is not boolean
print(isinstance(1, bool))

a = 105
print(a.bit_length())
print(True.bit_length()) #1 bit required to indicate
print(False.bit_length()) #1 bit required to indicate

#logical operator

#has adhaar_card And age >=18 -->Dl
has_adhaar = True
age = 17
print(has_adhaar and age >=18)

# has_adhaar 0r has Dl--> club
has_adhaar = True
has_Dl = False
print(has_adhaar or has_Dl)


x = 5
y = 10
print(x>0 and y>0)
print(x>7 and y>7)

print(x>7 or y>7)

age = 25
income = 25000
print(age<12 or income>12223732)

print(age>12 or not(income>23453535))

#boolean operatro precedence
result = (True and False) and (False and not(True or False))
print(result)
 
age = 25
income = 30000
credit_score = 700
is_eligible = (age>=18 and age<=65) and (income>=25000 or credit_score>=650 )
print(is_eligible)
