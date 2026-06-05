binary_num = 0b10
print(binary_num)

# Bitwise operator..........
x = 10
y = 6
#And operator
bitwise_and = x & y
print(f"bitwise of {x} and {y} = {bitwise_and}")
#Or operator
bitwise_or = x | y
print(f"bitwise of {x} and {y} = {bitwise_or}")
#Xor operator
bitwise_xor = x ^ y
print(f"bitwise of {x} and {y} = {bitwise_xor}")
#left shift operator

left_shift = x << 1
print(f"left_shift of {x} = {left_shift}")

# just checking the binary to num
print(0b10100)

#right shift operator
right_shift = x >> 1
print(f"right_shift of {x} = {right_shift}")
print(0b101)

#returns lasrgest intger less than or equal to the exact division
print(10//3)  #3
print(10.0//3) #3.0
print(-10//3) #-4
print(10//-3) #-4

#assignment operators

#swapping

# x = int(input("enetr the number: "))
# y = int(input("enetr the number: "))
# x,y = y,x   #swapping
# print(x,y)

z = 3
z = z+5
print(z)

s = 4
s += 5
print(s) 

msg = "hello"
msg += " wrold"
print(msg)

#float

sallary = 10.2
msg = 10.0
print(sallary + msg)

a = 10.2 
print(type(a))

a = float("2")
print(a)

print(float("2"))

#print(float("shu")) it gives ingError due to str
a = 1.5e3
b = 1500.0
print(a==b)  


#format specifier
pi = 3.14
print(f"{pi:.3f}") #3.14 it gives string and also contiue with 3 digits
print(round(pi, 3)) #3.14 it gives float
