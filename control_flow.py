# age = int(input())
# if age >= 18:
#     print("you are an adult")


# temp = int(input("Enter the temperature: "))
# is_raining = bool(input("Leave Empty if raining esle type anything"))
# if temp < 10 and is_raining:
#     print("wear a jacket")

temp = 5 # int(input("Enter the temperature: "))
is_raining = True #bool(input("Leave Empty if not raining esle type anything"))
if temp < 10 and is_raining:
    print("wear a jacket")


temp = 15
is_snowing = True
if temp > 10:
    print("it is Freezing")
    if is_snowing:
        print("and Dont forget your boots")
print("have a nice day")

temp = 9
is_snowing = True
if temp > 10:
    print("it is Freezing")
    if is_snowing:
        print("and Dont forget your boots")
print("have a nice day")


# score = 32
# if score>33:
#     print("passed")
# else:
#     print("failed")

# a = 6 #int(input("enter a no.: "))
# if a%2==0:
#     print("even")
# else:
#     print("Odd")

# age = 23
# if age>=18:
#     print("you can vote")
# else:
#     print("you cannot vote")


# age = int(input("Enetr the age: "))
# if age>=18:
#     password = input("Enter your password: ")
#     if len(password)>=8:
#         print("valid password")
#     else:
#         print("password  is too short. must be atleast 8 character")
# else:
#     print("you are under age")


# x = int(input("Enetr the num: "))
# if x%2==0:
#     print("even")
# else:
#     print("odd")



# x = int(input("Enter your num: "))
# if x>0:
#     print("it is positive")
# else:
#     if x<0:
#         print("negative")
#     else:
#         print("zero")



# x = int(input("enter the first num: "))
# y = int(input("enter the second num: "))
# if x>y:
#     print("x is greator")
# else:
#     print("y is greator")

# mark = int(input("Enter the num: "))
# if mark>=40:
#     print("pass")
# else:
#     print("fail")

 


# num1 = float(input("Enter you first num: "))
# num2 = float(input("Enter second num: "))
# op = input("Enter your operator (+, -, *, /): ")
# if op=="+":
#     print("Result: ",num1 + num2)
# else:
#     if op=="-":
#         print("Result: ",num1 - num2)
#     else:
#         if op=="*":
#             print("Result: ", num1 * num2)
#         else:
#             if op=="/":
#                 if num2 !=0:
#                     print("Result: ", num1 / num2)
#                 else:
#                     print("cannot divide by zero")
#             else:
#                 print("invalid Operator")


# score = 76
# if score>=90:
#     grade="A"
# elif score>=80:
#     grade="B"
# elif score>=70:
#     grade="C"
# elif score>=60:
#     grade="D"
# elif score>=50:
#     grade="E"
# elif score>=40:
#     grade="F"
# else:
#     grade="fail"    
# print(f"your garde is {grade}")



#1-9 --> positive single dgit number
#>=0 --> zero or neagative
# >9 --> positive

# num = 12
# if 0<num>9:
#     print("positive single dgit number")
# elif num>9:
#     print("positive")
# else:
#     print("zero or negative")



 # independent case so here we dont use elif conditon

# has_fever = True
# has_cough = True
# has_rash = False
# if has_fever:
#     print("Take fever medication")
# if has_cough:
#     print("Take cough syrup")
# if has_rash:
#     print("Aplly anti_itch cream")

# age = float(input("Enter your age: "))
# income = float(input("Enter your Income: "))
# if age >=18:
#     if income<30000:
#         print("low income tax")
#     elif income<50000:
#             print("medium income tax")
#     else:
#         print("high income tax")
# else:
#     print("you are under age")

score = 70 #int(input("Enter your marks: "))
if score>=90:
    print("your garde : O")
elif score>=80:
    print("your grade : A")
elif score>=70:
    print("your grade : B")
elif score>=60:
    print("your grade : C")
elif score>=50:
    print("ypur grade : D")
else: 
    print("your grade : F")

score = 57 #int(input("Enter your marks: "))
if score>=90:
    grade = "O"
  
elif score>=80:
    grade = "A"
elif score>=70:
    grade = "B"
elif score>=60:
    grade = "C"
else:
    grade = "F"
print(f"your grade is {grade}")


num = 0 #int(input("your no.: "))
if 1<=num<=9:
    print("positive single digit no.")
elif num<=0:
    print("Zero or negative")
else:
    print("positve")


has_fever = True
has_cough = True
has_rash = True
if has_fever:
    print("take fever medicine")
if has_cough:
    print("take cough syrup")
if has_rash:
    print("use cream")



age = 23 #int(input("your age: "))
income = 100000 #int(input("your income: "))
if age>=18:
    if income<30000:
        print("low income tax")
    elif 30000<=income>=70000:
        print("medium income tax")
    else:
        print("high income tax")
else:
    print("you are minor so you don't need to pay tax")



# a --> 6,7,8,--> lucky
# else --> unclucky

a = 6 #int(input("enter your num: "))
if a == 6 or a ==7 or a ==9:
    print("Lucky")
else:
    print("unlucky")
 

# important  
a = 7 #int(input("enter your num: "))
li = [6,7,9]
if a in li:
    print('lucky')
else:
    print("unlucky")


age = 20
if age>=18:
    status = "adult"
else:
    status = "minor"
print(status)

#Ternary Opearetor


age = 17 #int(input("your age: "))
status = "adult" if age >=18 else "minor"
print(status)



num = 56 #int(input("enter your num: "))
divisor = 9 #int(input("enter your divisor: "))
# if divisor!=0:
#     print(f"the divident of {num} / {divisor} : {num/divisor}")
# else:
#     print("divisor cant' be zero ")

result = num / divisor if divisor !=0 else "cannot be divide by zero"
print(result)



num1 = 2 #float(input("Enter your num1: "))
num2 = 2 #float(input("Enter your num2: "))
operator = "*" #input("Enter your operator '+, -, *, / : ")
if operator=="+":
    result = num1 + num2
elif operator=="-":
    result = num1 - num2
elif operator=="*":
    result = num1 * num2
elif operator=="/":
    result = num1 / num2
else:
    result = "you dont choose right operator"
print(result)

# num1 = float(input("Enter you first num: "))
# num2 = float(input("Enter second num: "))
# op = input("Enter your operator (+, -, *, /): ")
# if op=="+":
#     print("Result: ",num1 + num2)
# else:
#     if op=="-":
#         print("Result: ",num1 - num2)
#     else:
#         if op=="*":
#             print("Result: ", num1 * num2)
#         else:
#             if op=="/":
#                 if num2 !=0:
#                     print("Result: ", num1 / num2)
#                 else:
#                     print("cannot divide by zero")
#             else:
#                 print("invalid Operator")


#Enter a number (1–7) and print the day
num = 5 # int(input("Enter the num: "))
if num==1:
    print("sun")
elif num==2:
    print("mon")
elif num==3:
    print("tue")
elif num==4:
    print("wed")
elif num==5:
    print("thurs")
elif num==6:
    print("sat")
elif num==7:
    print("sun")
else:
    print(" today is not your day")




num = 56 #int(input("Enter your num: "))
if 50<=num<=74:
    grade = "C"
elif 75<=num<=89:
    grade = "B"
elif num>=90:
    grade = "A"
else:
    grade = "you are fail"
print(f"your grade {grade}")




#Taking input from user
num1 = 4 #float(input("Enter first number: "))
num2 = 5 #float(input("Enter second number: "))
num3 = 6 #float(input("Enter third number: "))


if num1 >= num2 and num1 >= num3:
    largest = num1
elif num2 >= num1 and num2 >= num3:
    largest = num2
else:
    largest = num3


print("The largest number is:", largest)



# correct_username = "admin"
# correct_password = "1234"
# username =  input("Enter your username: ")
# password = input("Enter your password: ")
# if (username == correct_username and password == correct_password):
#     print("Loggin successful")
# elif (username != correct_username):
#     print("Invalid username")
# elif (password != correct_password):
#     print("Invaild password")


# ATM Withdrawal System

# Ask for balance and withdrawal amount.
# Conditions:
# If amount > balance → "Insufficient funds"
# If amount <= 0 → "Invalid amount"
# Else → "Transaction successful"


balance = float(input("Enter yoyr balance: "))
amount = float(input("Enter your amount: "))
if amount > balance:
    print("insufficient balance")
elif amount <= 0:
    print("invalid amount")
else:
    print("transaction successful")
    balance -= amount
    print("Remaining balance:", balance)
  