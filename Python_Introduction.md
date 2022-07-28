# Python
Python is one of the most popular and versatile programming languages
![image](https://user-images.githubusercontent.com/110176257/181594597-132d3469-13b0-4d91-9c3a-61b7fa3197a5.png)

It has many applications, as seen on the image above it is very powerful for dealing with data but is also used for general automation and software development.

## Python introduction
### python variables
a variable in python allows for data storage, like a container, the following is an example of code with no variables
```
print("name is maiks")
```
this code will simply return what is inside the quotation marks when it runs, or in the next example:
```
print(3+6)
```
the code will return the value of 3+6 which is 9.
But there is no way to refer to this data later on in the code and you would need to write it all out again every time.
When using a variable, this data is stored in a container which is the varaible, and can be called upon at any time.
```
name = "maiks"
age = 20
salary = 13.37
```
in the code above, three different types of data are stored in three seperate variables. The name variable is storing a string, which is a series of characters. The age variable is storing a integer, which is a whole number. And the salary variable is storing a float, which is a number with decimal places. There is also a fourth data type used by variables which is boolean true or false values represented by 1 and 0 respectively.
This can be demonstrated by adding "type" whenever we go to print the variable. 
```
print(name)
```
this will return "maiks"
```
print(type(name))
```
this will return "string" because it is the type of data that is stored in the name variable

### Taking user input
User input is used on most software and wesbsites, for example when you need to put your address for a package, then it is displayed back to you to make sure it is the correct details. To do this in Python, we must the built in input() function.
For example:
```
name = input()
print name
```
when executed, this code will wait for the user to input something into the terminal, and then print whatever the input was. A more functional example can be seen here:
```
print("hello, what is your name?")
name = input()
print("your name is: ")
print name
```
this code asks for the name of the user, then it waits for the user to input the data before the rest of the code runs, and then displays the inputted data back to the user.

## Example code
This block of code utilises all of the features mentioned in this introduction, it also includes comments for clarity.

```

# create variables for first_name, last_name, age, address, salary
# introduction

print("hello user")

# asks for first name and allows user to input

firstname = input("please enter your first name: ") 

# asks for last name and allows user to input
 
lastname = input("please enter your last name: ")

# asks for age and waits for input
# the int() prefix limits the variable to integers

age = int(input("what is your age? ")) 

# asks user for address and waits for input

address = input("please enter your address ") 


# the float() prefix limits the variable to decimal numbers only
# asks user for salary
 
salary = float(input("what is your salary? ")) 

# asks what course and waits for input

course = input("what course are you taking? ")

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
```
