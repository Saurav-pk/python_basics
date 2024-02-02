# print("hello world")
#------------------------Variables------------------------------
#String
# first_name = "saurav"
# print(type(first_name))
# last_name = "dev"
# print(first_name+" "+last_name)

#Integer
# age = 22
# print(age+1)
# print(type(age))
# print("your age is: "+str(age))

#Float
# height = 170.5
# print(type(height))
# print("your height is: "+str(height)+"cm")

#Boolean
# human = True
# print(type(human))
# print("Are you a human :"+str(human))
# print(human)

#---------------------------------Multiple assignment-----------------------
# name, age, human = "saurav", 22, True
# print("name is "+name+" age is "+str(age))
# print("Are you a human :"+str(human))

# TEN = ten = Ten = 10
# print(TEN)
# print(ten)
# print(Ten)

#----------------------------------String methods------------------------------
# name = "saurav PK"
# first_name = "saurav"
# age = "22"
# print(len(name))
# print(name.find("r"))
# print(name.capitalize())
# print(name.upper())
# print(name.lower())
# print(name.isdigit())
# print(age.isdigit())
# print(name.isalpha())
# print(first_name.isalpha())
# print(name.count("a"))
# print(name.replace("a","o"))
# print(first_name*3)

#-----------------------------Type casting-------------------------------
# x = 1
# y = 2.0
# z = 3
# x = str(x)
# y = int(y)
# z = float(z)
#
# print(x+" is string")
# print(y)
# print(z)

#-----------------------------User input------------------------------------

# name = input("what is your name?: ")
# print("Hello "+name)

# age = int(input("what is your age?: "))
# age = age + 1
# print("You are "+str(age)+" years old")

#-----------------------------Math module--------------------------------
# import math
# pi = -3.14
# x = 1
# y = 2
# z = 3
#
# print(round(pi))
# print(math.ceil(pi))
# print(math.floor(pi))
# print(abs(pi))
# print(pow(pi, 2))
# print(math.sqrt(9))
# print(max(x, y, z))
# print(min(x, y, z))

#--------------------------------String slicing---------------------------
# indexing[]
#[start:stop:step]

# name = "Bro Python Code"
# first_name = name[:3]
# print(first_name)
# last_name = name[11:]
# print(last_name)
# middle_name = name[4:10]
# print(middle_name)
# funky_name = name[::2]
# print(funky_name)
# reversed_name = name[::-1]
# print(reversed_name)

# website1 = "http://google.com"
# website2 = "http://wikipedia.com"
# slice = slice(7,-4)
# print(website1[slice])
# print(website2[slice])

#--------------------------------if, else if, else-----------------------------------
# age = int(input("How old are you?: "))
# if age == 100:
#     print("You are a century old!")
# elif age >= 18:
#     print("You are an adult!")
# elif age < 0:
#     print("You have,t been born yet!")
# else:
#     print("You are a child!")

#----------------------------------Logical operators---------------------------------
# temp = int(input("What is the temperature outside?: "))

# if temp >= 0 and temp <= 30:
#     print("The temperature is good today!")
#     print("go outside!")
# elif temp < 0 or temp > 30:
#     print("The temperature is bad today!")
#     print("Stay inside!")

# if not temp >= 0 and temp <= 30:
#     print("The temperature is bad today!")
#     print("Stay inside!")
# elif not temp < 0 or temp > 30:
#     print("The temperature is good today!")
#     print("go outside!")

#---------------------------While loop---------------------------------
# name = None
# while not  name:
#     name = input("Enter your name: ")
# print("Hello "+name)

#--------------------------------For loop-------------------------------
# for i in range(10):
#     print(i+1)
# for i in range(50, 100+1,2):
#     print(i)
# for i in "Bro code":
#     print(i)

# import time
# for seconds in range(10,0,-1):
#     print(seconds)
#     time.sleep(1)
# print("Happy New Year!")

#----------------------------------Nested loops-----------------------------------------
# rows = int(input("How many rows?: "))
# column = int(input("How many columns?: "))
# symbol = input("Enter a symbol to use: ")
# for i in range(rows):
#     for j in range(column):
#         print(symbol, end="")
#     print()

#----------------------------------Loop control statements----------------------------------
# while True:
#     name = input("Enter your name: ")
#     if name != "":
#         break

# phoneNo = "123-456-7890"
# for i in phoneNo:
#     if i == "-":
#         continue
#     print(i, end="")

# for i in range(1,10):
#     if i == 5:
#         pass #place hoder
#     else:
#         print(i)

#-----------------------------List---------------------------------
# food = ["pizza", "hamburger", "hotdog", "spaghetti", "pudding"]
# print(food)
# food[0] = "sushi"
# food.remove("hotdog")
# food.pop()
# food.append("biriyani")
# food.insert(1,"cake")
# food.sort()
# for i in food:
#     print(i)
# food.clear()
# print(food)

#----------------------------------2D List---------------------------------
# drink = ["coffee", "soda", "tea"]
# dinner = ["pizza", "hamburger", "hot dog"]
# dessert = ["cake", "ice cream"]
# food = [drink, dinner, dessert]
# print(food)
# print(food[0])
# print(food[1][2])

#----------------------------------Tuples-----------------------------------
#   collection which is ordered and unchangeable
#   used to group together related data

# student = ("Bro", 21, "male", "Bro")
# print(student.count("Bro"))
# print(student.index(21))
# for x in student:
#     print(x)
# if "Bro" in student:
#     print("Bro is here!")

#--------------------------------------set------------------------------------
#   collection which is unordered, unindexed
#   No duplicate values
# utensils = {"fork", "spoon", "spoon", "knife"}
# dishes = {"bowl", "plate", "cup", "knife"}
#
# utensils.add("mixer")
# for i in utensils:
#     print(i)
# utensils.remove("fork")
# print(utensils)
# # dishes.update(utensils)
# print(dishes)
# dinner_table = dishes.union(utensils)
# print(dinner_table)
# print(utensils.difference(dishes))
# print(utensils.intersection(dishes))

#-------------------------------dictionary-----------------------------
#   a changeable, unordered collection of unique key:value pairs
#   Fast because they use hashing, allow us to access values quickly

# capitals = {'USA':'Washington DC',
#             'India':'New Delhi',
#             'China':'Beijing',
#             'Russia':'Moscow'}
# print(capitals.keys())
# print(capitals.values())
# print(capitals.items())
# capitals.update({'Germany':'Berlin'})
# capitals.update({'USA':'Las Vegas'})
# capitals.pop('China')
# for key, value in capitals.items():
#     print(key, value)
# capitals.clear()

#-----------------------------------functions---------------------------------
# def hello(name,name1):
#     print("hello "+name+" "+name1)
#     print("have a nice day!")
# name = "bro"
# second_name = "code"
# hello(name, second_name)

#---------------------------------------return statements-----------------------
def multiply(num1, num2):
    return num1 * num2
print(multiply(5, 10))