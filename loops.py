#while loop 
# code block to be executed


x = 1
while (x<=5):
    print("Hello world", x)
    x +=1
    if x ==5:
        break

x  = 1
while True:
    print("OK")
    x +=1
    if x==5:
        break

x = 1
while x<=10:
    print(x)
    x+=1
    if x==7:
        break

x = 10
while x>=1:
    print(x)
    x -=1


# For loop
# for variable in sequence:
#     code block (loop body)

fruits = ["apple", "mango", "banana"]
for x in fruits:
    print(x) 


fruits = ["apple", "mango", "banana"] 
print(fruits[0] + fruits[1])

x = "apple"
for a in x:
    print(a)


#Range built in function
#range (stop)
#range (start, stop exclusive not counted)
#rang (starts, stop, step)
for i in range(5):
    print(i)
    
for i in range(1,5,2):
    print("hello world", i)
    
for i in range(10,0,-1):
    print(i)

for i in range(2,21,2):
    print(i)


num = 2
for i in range(1,11):
    print(num,"x",i,"=", num*i)

print(list(range(10)))

 
fruits =['apple', 'banana', 'mango']
for i in fruits:
    print(i)

fruits =['apple', 'banana', 'mango']
for i in range(3):
    print(fruits[i])

fruits =['apple', 'banana', 'mango']
for i in range(len(fruits)):
    print(fruits[i])

fruits =['apple', 'banana', 'mango']
for i in range(len(fruits)-1, 0, -1):
    print(fruits[i])

fruits =['apple', 'banana', 'mango']
for i in range(len(fruits)-1, -1, -1):
    print(fruits[i])


#enumerate

fruits =['apple', 'banana', 'mango']
print(list(enumerate(fruits)))

for index, fruit in enumerate(fruits):
    print(fruits[index])

#break ---> immediately exits the loop, regardless of the loop condition


for num in range(10):
    if num==5:
        break
    print(num)

# continue ---> skips the current iteration and moves to the next one.

for num in range(10):
    if num==5:
        continue
    print(num)

# Pass ---> a do-nothing placeholder. the loops does nothing  when pass is hit.

for num in range(10):
    if num==5:
        pass
    print(num)

# num = int(input("enter yiur:" ))
# if num%2==0:
#     print("even")
# else:
#     print("odd")

a = 11 #int(input("Enter your num: "))
for num in range(a):
    if num%2==0:
        print(num, "even")
    else:
        print(num, "odd")

for num in range(1,11):
    if num%2==0:
        print(num, "even")
    else:
        print(num, "odd")

x = int(input("Enter your num: "))
count = 0
for i in range(1,x+1):
    if x%i==0:
        count+=1
if count==2:
    print("Prime")
else:
    print("Not prime")
