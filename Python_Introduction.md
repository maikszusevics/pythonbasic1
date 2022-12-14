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


# Data types and Operators
## Two types of operators
### Arithmetic
- ` + - * / `
- `+` adds two operands (var) together
- `-` subtracts two operands (var) 
- `*` multiplies two operands together
- `/` divides two operands



### Comparison Operators
- `>` greater than `a > b`
- `<` less than 
- `==` equals
- `!=` 
- `>=` 
- `<=`

```
a = 4
b = 2
print(a>b)# true
print(a<b)# false
print(a==b)# false
print(a!=b)# true

print(a * b) # 8
```

### functions
```greeting = "hello world!"

# what options are available in python's built in library

# if we wanted to check if the letters are in string
print(greeting.isalpha()) # true or false (no numbers no spaces)

# is it in lowercase or uppercase

print(greeting.islower())  # is it all lowercase (boolean)
print(greeting.isdigit())   # is it only numbers (boolean)
print(greeting.endswith("!"))   # does it end with !
print(greeting.startswith("joe")) # does it start with joe 
```
#### strings concatenation casting
- String indexing 
- `Hello World`
- index in python starts with 0 

- hello world!
- 01234567891011

```
greeting = "Hello World!"
        #   01234567891011
print(len(greeting))
# slicing
print(greeting[-5])
print(greeting[:5])

# print only world in print statement using slicing

print(greeting[6:11])

# print 4th letter from left to right
# print 7th letter from right to left
# print 6th letter from left to right

print(greeting[3])
print(greeting[-7])
print(greeting[6])
```
#### more methods

```
examplestring = "jame                                           "
print(len(examplestring)) #length is 47 because spaces

# strip()
print(len(examplestring.strip())) #length is 4 because strip

# welcome user with their name and welcome messages - name & message must start with capital
example_text = "heres some texT With a lot of text"
print(example_text.count("text"))

# find a method to bring the statement in capital/small letters then first letter capital

print(example_text.capitalize()) #capitalises first letter
print(example_text.swapcase()) #swaps lowercase/capital
print(example_text.lower()) # prints in all lowercase

# how to replace text within a string

print(example_text.replace("some", "this")) # replaces "some" with "this"
```
