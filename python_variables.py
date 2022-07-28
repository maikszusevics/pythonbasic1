
# # testing the env with pycharm
#
# # var is to help us store data of different types
# name = "maiks 19 + 8" #string
# age = 99 #integer
# salary = 15.5 #float
#
# print(name)
# print(age)
# print(salary)
#
# #types of variable
# print (type(name))
#
# print (type(age))
#
# print (type(salary))
#

# taking user input
# name = input("yourname:")
# print("welcome", name)


# create variables for first_name, last_name, age, address, salary
print("hello user") # introduction
firstname = input("please enter your first name: ") # asks for first name and allows user to input
lastname = input("please enter your last name: ") # asks for last name and allows user to input
age = int(input("what is your age? ")) # asks for age and has to be integer (i would like to add functionality that code wont crash if user inputs letters intead of numbers)
address = input("please enter your address ") # asks user for address and waits for input
salary = float(input("what is your salary? ")) # asks user for salary and allows for decimal points
course = input("what course are you taking? ") # asks what course and waits for input

# prints inputs from user
print("your first name:")
print(firstname)
print("your last name:")
print(lastname)
print("this is your age:")
print(age)
print("this is your address:")
print(address)
print("this is your salary:")
print(salary)
print("the course you are taking is:")
print(course)

# prints the type of each input
print(type(firstname))
print(type(lastname))
print(type(age))
print(type(address))
print(type(salary))
print(type(course))



