print('Python ==>>>>')
"""
#
# Numeric types
num1 = 10  # int
num2 = 3.14  # float
num3 = 2 + 3j  # complex

print(num1, type(num1))  # Output: 10 <class 'int'>
print(num2, type(num2))  # Output: 3.14 <class 'float'>
print(num3, type(num3))  # Output: (2+3j) <class 'complex'>


"""


"""

#
# String
message = 'Hello, World!'

print(message, type(message))  # Output: Hello, World! <class 'str'>

# multi line string
multiline_str = " This is line one \
this is line two \
this is line three"

print(multiline_str)


"""


"""


#
# Boolean
is_valid = True

print(is_valid, type(is_valid))  # Output: True <class 'bool'>


"""


"""

#
# List
numbers = [1, 2, 3, 4, 5]
names = ["Alice", "Bob", "Charlie"]

print(numbers, type(numbers))  # Output: [1, 2, 3, 4, 5] <class 'list'>
print(names, type(names))  # Output: ['Alice', 'Bob', 'Charlie'] <class 'list'>

#more one list latter


"""


"""

#
# Tuple
coordinates = (3.14, -2.5)

print(coordinates, type(coordinates))  # Output: (3.14, -2.5) <class 'tuple'>


#
# Dictionary or Object
student = {"name": "Pri", "grade": "A"}

print(student, type(student))  # Output: {'name': 'Pri', 'grade': 'A'} <class 'dict'>


"""


"""


#
# let's check variable types
string_var = "string"
print(type(string_var)) # <class 'str'>


boolean_var = True
print(type(boolean_var)) # <class 'bool'>


list_var = [1,2] # list or array
print(type(list_var)) # <class 'list'>


tuple_var = (1,2) # tuple or immutable array
print(type(tuple_var)) # <class 'tuple'>


dictonary_var = {} # dictonary or object
print(type(dictonary_var)) # <class 'dict'>


"""


#
# Buildin methods => len()

# len() - This function returns the length 
#or the count of the elements contained within 
#the structure it is applied on. 
#This may be a string, array, list,
#tuple, dictionary or any sequence.

dictonary_var = {
  "key_1": "value_1"
}
print()




"""


#
# This program calculates the square of a number

# Take user input
number = int(input("Enter a number: "))

# Calculate square
square = number ** 2

# Display the result
print("The square of", number, "is", square)


"""


'''
one_to_ten = range(1,11) 
print(one_to_ten,type(one_to_ten))

# Example of a for loop using range
for num in one_to_ten:
    print(num)


#
# Control Flow - if statement

x = 10

if x > 0:
    print("Positive number")
elif x < 0:
    print("Negative number")
else:
    print("Zero")



#
# Loops


# for loop - iterate over a list
fruits = ["apple", "banana", "cherry"]

for fruit in fruits:
  print(fruit)



# while loop - print numbers from 1 to 5
count = 1

while count <= 5:
    print(count)
    count += 1

'''

'''
#
# condition with loop
for index, item in enumerate([1,2]):
  print("Value",item)
  print("index",index)

else: # runs when loop succeed . If the loop breaks, the else part would not run
  print('List were empty')

'''




#
# Function

'''
def printHello():
  print("Hello")
  print(len("Hello")) # gives length of the str
  return "return value" # by default it return None
print(printHello())


def greet(name):
  print("Hello, " + name + "!")

# Call the function
greet("Pri")

# functions and arguments

#1. Positional Arguments
def add_numbers(a, b):
    return a + b

result = add_numbers(3, 5)
print(result)  # Output: 8


#2. Default Arguments
def power(base, exponent=2):
    return base ** exponent

result1 = power(2)      # Uses default exponent (2)
result2 = power(3, 3)   # Uses provided exponent (3)
print(result1)  # Output: 4
print(result2)  # Output: 27



#3. Keyword Arguments
def greet(name, greeting):
    return f"{greeting}, {name}!"

message = greet(greeting="Hello", name="John")
print(message)  # Output: "Hello, John!"


#4. Variable-Length Arguments:
#Sometimes, you may not know in advance 
#how many arguments will be passed to a function.
#Python allows you to handle variable-length arguments 
#using *args and **kwargs.
'''
'''
# *args: Collects positional arguments into a tuple
def sum_all(*args):
  print('args -->', args)
  total = 0
  for num in args:
    total += num
    return total

result = sum_all(1, 2, 3, 4, 5)
print(result)  # Output: 15

# **kwargs: Collects keyword arguments into a dictionary
def print_details(**kwargs):
  print('kwargs -->', kwargs)
  for key, value in kwargs.items():
        print(f"{key}: {value}")

print_details(name="John", age=30, city="New York")
# Output:
# name: John
# age: 30
# city: New York

# Make list out of arguments
def store_arguments_in_list(*args):
    arguments_list = list(args)
    return arguments_list

result_list = store_arguments_in_list(1, "hello", True, 3.14)
print(result_list)  # Output: [1, 'hello', True, 3.14]





'''















# Higher-order functions
'''
# Lambda function
add = lambda x, y: x + y
print(add(3, 5))  # Output: 8
'''

'''

# map() function
# Takes a function and itarate over the given list

def square(x):
  return x ** 2
  
numbers = [1, 2, 3, 4]

squared_numbers = map(square, numbers)
print('list from map')
print(list(squared_numbers))  # Output: [1, 4, 9, 16]


'''


'''

# filter() function
def filter_adults(x):
  return x>=18
  
ages = [25, 4, 8, 18, 30, 15, 40]

adults = filter(filter_adults, ages)
print('list from filter')  # Output: [25, 18, 30, 40]
print(list(adults))  # Output: [25, 18, 30, 40]


nums = [1,2,3,5,7,8,,6,4]
def filter_nums(num):
  return num < 7
  
filtered_nums = filter(filter_nums, nums)
num_list = list(filtered_nums)
print(num_list)


arr = [
  {
    "id": 1,
    "key": "obj_1"
  },
  {
    "id": 2,
    "key": "obj_2"
  },
  {
    "id": 3,
    "key": "obj_3"
  },
]
def filter_arr(obj):
  return obj["id"] < 3
filtered_arr = filter(filter_arr, arr)

arr_list = list(filtered_arr)
print(arr_list)


'''

'''

# reduce() function
from functools import reduce
numbers = [1, 2, 3, 4, 5]
sum_of_numbers = reduce(lambda x, y: x + y, numbers)
print(sum_of_numbers)  # Output: 15



'''







# print everything that is present in a module

# import math 
# print(dir(math))



# File Handling and I/O in Python.

'''
file = open("../text-file.txt", "r")  # Open file for reading
file_content = file.read()  # Read the entire file content

file = open("../text-file.txt", "w") # Open file for writing
# "w" write new data and remove the previous data
file.write("Line added by python")  # Write data to the file
file.close()  # Close the file

print(file_content)

file = open("../text-file.txt", "a")  # Open file for appending
file.write("\nThis is a new line.")  # Append data to the file
file.close()  # Close the file

'''




'''
'''
# More on Dictionary

# Creating a dictionary
'''
person = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

print("person ==> ",person)
print('person.items,() ==> ',person.items())

for key, value in person.items():
  print('key:value =>',key, value)

'''

'''
# Accessing dictionary elements
print(person["name"])  # Output: "John"
print(person.get("age"))  # Output: 30

# Modifying dictionary elements
person["age"] = 31
print(person)   # Output: {'name': 'John', 'age': 31, 'city': 'New York'}

# Dictionary methods
person["occupation"] = "Engineer"
print(person
# Output: {'name': 'John', 'age': 31, 'city': 'New York', 'occupation': 'Engineer'}

del person["city"]
print(person)         
# Output: {'name': 'John', 'age': 31, 'occupation': 'Engineer'}

'''



'''
# Concant dictionary - dictionary.update(newDictionary)
languages = {
  'first_lang': 'Javascript'
}

python = { 'second_lang': 'Python' }

languages.update(python)

print(languages) # {'first_lang': 'Javascript', 'second_lang': 'Python'}

'''




# OOPs in python 
# Class in python
'''
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

# In the above example,
#We define a class called Person with 
#two attributes (name and age) and a method (greet).

#The __init__ method is a special method 
#called the constructor, which initializes the 
#attributes of the class.



# Object Creation from class
person1 = Person("Alice", 25)
person2 = Person("Jhon", 30)

print(person1.name)
print(person1.greet())




# Class Inheritance (Subclassing)
# Inheritance allows you to create a new class (subclass)
#that inherits attributes and methods from an existing class (superclass).
#The subclass can add new attributes and methods or override existing ones.

## see  Student class taking another parent class ( Person )
# as it is using one parent class it also calls single inheritance
# there is multiple inheritance as well,
# where a class takes multiple parent class

class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)
        self.student_id = student_id

    def study(self):
        print(f"{self.name} with student id : {self.student_id} is studying.")

student = Student('Jhon',20,1)
print(student.name)
print(student.study())
'''

'''
# Example of a sub class
class Person:
  def __init__(self,name):
    self.name = name
    print('name in super class:',self.name)
    
p = Person('pri')

class Student(Person):
  def __init__(self):
    super().__init__('student name')
    print('name in sub class:',self.name)
  
    
stu = Student()

'''



'''

# What is __init__ and self ?

#__init__
# __init__ is a special method in Python, 
#often referred to as the "constructor" method. 
#It is automatically called when an object (instance) of a class is created.
#The purpose of __init__ is to initialize the attributes (state) of the newly created object.


#self
#self: The self parameter is a reference to the instance
#of the class that is being created.
#It is automatically passed to the __init__ method
#and other instance methods in Python.
#By convention, it is named self, but you can use any valid variable name.
#It allows you to access and set the attributes of the instance within the method.

#name, age, ...: These are the parameters that you can pass 
#when creating an instance of the class.

#These values will be used to initialize the attributes of the object.


#example
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

# Creating instances of the Person class
person1 = Person("Alice", 30)
person2 = Person("Bob", 25)

# Accessing the attributes of the instances
print(person1.name)  # Output: "Alice"
print(person2.age)   # Output: 25


'''


'''

#Polymorphism
#Polymorphism allows objects of different
#classes to be treated as interchangeable,
#as long as they implement the same methods.
#This enables code reusability and flexibility.

def perform_greeting(param):
    param.greet()

person = Person("Charlie", 40)
student = Student("Dave", 21, "S12345")

perform_greeting(person)   # Output: Hello, my name is Charlie and I am 40 years old.
perform_greeting(student)  # Output: Hello, my name is Dave and I am 21 years old.

'''


'''

# public and private variable

class DummyClass:
  def __init__(self):
    self.publicVariable = 'Public value'
    self.__privateVariable = 'Private value'


dummyClass = DummyClass()

#publicVariable can be accessed
print( dummyClass.publicVariable)

#privateVariable can not be accessed
#print( dummyClass.privateVariable)

# way to access private variable # it also call name mangling
print(dummyClass._DummyClass__privateVariable)


'''

'''

# class methods 

class Calculate:
  def __init__(self, num):
    self.num = num
    
  def add(self, n):   # method
   self.num = self.num + n
   
  @staticmethod 
  def add_static(obj, n):   # static method
    obj.num = obj.num + n
    return obj.num 
   
  
calc = Calculate(5)

print('calc.num => ',calc.num)


# calling normal method
calc.add(5)
print('after calc.add(5) => ',calc.num)


# calling static method
calc.add_static(calc, 5)
print('after calc.add_static(obj, 5) => ',calc.num)


# 2nd way of calling static method
Calculate.add_static(calc, 5)
print('after Calculate.add_static(obj, 5) => ',calc.num)



# Normal method vs static method

# Python automatically pass instance argument
#while calling a method, that we can access as self
#so calc.add(calc) is same as calc.add()

# In case of static method instance
#not get passed, we can pass it manually to use it


'''





# More on list
# Creating a swallow copy of list
'''
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9]
newNums1 = nums[:]
newNums2 = nums[-3:]
newNums3 = nums[3:]
newNums4 = nums[:-3]
newNums5 = nums[:3]
newNums6 = nums[3:6] # Represents start and end . 
print(newNums1)
print(newNums2)
print(newNums3)
print(newNums4)
print(newNums5)
print(newNums6)
print(len(nums)) # returns length



# Filtering
even_number =  list(filter(num % 2 == 0, nums))

print(even_number)
'''


'''

# Methods on list

# append - adds an element to the end of the list.
fruits = ['apple', 'banana', 'cherry']
fruits.append('date')
print(fruits)  # Output: ['apple', 'banana', 'cherry', 'date']


# extend - extends the list by appending elements at end
numbers = [1, 2, 3]
more_numbers = [4, 5, 6]
numbers.extend(more_numbers)
print(numbers)  # Output: [1, 2, 3, 4, 5, 6]


# insert - inserts an element at a specified position in the list.
numbers = [1, 2, 3, 4]
specificIndex = 2
numbers.insert(specificIndex, 5)
print(numbers)  # Output: [1, 2, 5, 3, 4]


# remove - removes the first occurrence of the specified element from the list.
fruits2 = ['mango', 'banana', 'lemon', 'orange']
fruits2.remove('banana')
print(fruits2)  # Output: ['mango', 'lemon', 'orange']


# pop - removes and returns the element 
#at the specified index. If no index is provided,
#it removes and returns the last element.

numbers = [1, 2, 3, 4, 5]
popped_element = numbers.pop(2)
print(popped_element)  # Output: 3
print(numbers)  # Output: [1, 2, 4, 5]


# count - returns the number of occurrences of the specified element in the list.
numbers = [1, 2, 3, 2, 4, 2, 5]
count = numbers.count(2)
print(count)  # Output: 3



# sort - sorts the list in ascending order. 
#If the list contains elements of different types, 
#it will raise a TypeError

numbers = [3, 1, 4, 1, 5, 9, 2, 6]
numbers.sort()
print(numbers)  # Output: [1, 1, 2, 3, 4, 5, 6, 9]


# reverse - reverses the order of the elements in the list.
fruits = ['apple', 'banana', 'cherry', 'date']
fruits.reverse()
print(fruits)  # Output: ['date', 'cherry', 'banana', 'apple']


'''





'''

# More on tuple - immutable collection of items. 
#Tuples are similar to lists, 
#but they cannot be modified once created.

my_tuple = (10, 20, 30)
print(my_tuple[1])  # Output: 20


# len - returns the number of items in the tuple.
fruits = ('apple', 'banana', 'cherry')
length = len(fruits)
print(length)  # Output: 3


# index - returns the index of the first occurrence of the specified element in the tuple
tuple1 = (1,3,5,6,7,9)
index = tuple1.index(3)
print('index -->',index)  # Output: 1


# Tuple unpacking allows you to assign the elements of a tuple to individual variables.
point = (3, 4)
x, y = point
print(x)  # Output: 3
print(y)  # Output: 4


# Tuples can be compared using comparison
#operators (<, <=, >, >=, ==, !=), and they are compared
#element-wise from left to right.

tuple1 = (1, 2, 3)
tuple2 = (1, 2, 4)
print(tuple1 < tuple2)  # Output: True


'''



'''


# Sets
my_set = {1, 2, 2, 3, 3, 3}
print(my_set)       # Output: {1, 2, 3}

# Set operations
set1 = {1, 2, 3}
set2 = {3, 4, 5}

union_set = set1 | set2           # Union
intersection_set = set1 & set2    # Intersection
difference_set = set1 - set2      # Difference
symmetric_difference_set = set1 ^ set2  # Symmetric Difference

print(union_set)                 # Output: {1, 2, 3, 4, 5}
print(intersection_set)          # Output: {3}
print(difference_set)            # Output: {1, 2}
print(symmetric_difference_set)  # Output: {1, 2, 4, 5}

'''


# Modules and Packages

#my_package/
#   __init__.py
#   my_module.py
#    my_subpackage/
#       __init__.py
#        my_submodule.py
'''

# File: my_module.py
def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


# Using the package
from my_package.my_module import add

result = add(3, 5)
print(result)  # Output: 8

'''

# magic method
'''
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} (age: {self.age})"

# Creating a Person object
person = Person("John", 30)

# Calling the __str__() method on the object and storing the returned string
person_string = str(person)

# Using the returned string
print(f"Person details: {person_string}")
print(person.__dict__)
print(person)


'''

# Python testing

'''

import unittest

def add(a, b):
    return a + b

class TestMathOperations(unittest.TestCase):

    def test_add_positive_numbers(self):
        result = add(3, 5)
        self.assertEqual(result, 8)

    def test_add_negative_numbers(self):
        result = add(-3, -5)
        self.assertEqual(result, -8)

if __name__ == "__main__":
    unittest.main()


'''

# F string 
'''
variable1 = "Apple"
variable2 = 160.98996
f_string = f"This is a f-string {variable2:.2f} rs per kg"
print(f_string)
'''



# doc string

def square(n):
  '''It takes n as number and return square of n .
  This string will show up when you do func.__doc__ .
  Write this just after func name before func body .'''
  return n ** 2

#print(square(5))
#print(square.__doc__)






#Exception Handling
'''
try:
  num = input("Get square => ")
  print( int(num) ** 2 )
except Exception as e:
  print('Error => ',e)
  print('Invalid input')

print('Some important lines of code')

'''


# Operators
'''
# comparison operator

a = 8
b = 8

print( a == b) # true # checks for values
print( a is b) # true # checks for memory location

'''



# Decorators
#Decorators are functions that modify the behavior of other functions.
#They are a powerful tool for extending the functionality
#of existing functions or methods without modifying their code directly.

'''

def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")

say_hello()
#my_decorator(say_hello)() # Another way to call decorator

#Output
#Something is happening before the function is called.
#Hello!
#Something is happening after the function is called.


'''



# Getter and setter in python


#In Python, getter and setter methods are used
# to control the access and modification of class attributes.
# These methods allow you to define custom behavior
# when getting (reading) and setting (writing) the values of object attributes.
# Using getters and setters can help enforce
# data encapsulation and maintain class integrity.

#Example
'''
class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    # Getter method for 'name' attribute
    def get_name(self):
        return self._name

    # Setter method for 'name' attribute
    def set_name(self, name):
        self._name = name

    # Getter method for 'age' attribute
    def get_age(self):
        return self._age

    # Setter method for 'age' attribute
    def set_age(self, age):
        if age >= 0:
            self._age = age
        else:
            print("Age cannot be negative!")

# Create an instance of the Person class
person1 = Person("Alice", 30)

# Accessing attributes using getter methods
print("Name:", person1.get_name())  # Output: Name: Alice
print("Age:", person1.get_age())    # Output: Age: 30

# Using setter methods to modify attributes
person1.set_name("Bob")
person1.set_age(25)

# Accessing modified attributes using getter methods
print("Name:", person1.get_name())  # Output: Name: Bob
print("Age:", person1.get_age())    # Output: Age: 25

# Trying to set a negative age (will be prevented by the setter method)
person1.set_age(-5)                 # Output: Age cannot be negative!
print("Age:", person1.get_age())    # Output: Age: 25 (age remains unchanged)

'''

# Getter and setter with @property

# Instead of using explicit getter and setter methods,
# you can use the @property decorator in Python.
# The @property decorator allows you to define a method as a property getter,
# which can be accessed like an attribute but is computed on-the-fly.
# When you try to access the property,
# the decorated method will be called automatically.


#Example
'''
class Person:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value >= 0:
            self._age = value
        else:
            print("Age cannot be negative!")

# Create an instance of the Person class
person1 = Person("Alice", 30)

# Accessing attributes using properties (getter)
print("Name:", person1.name)  # Output: Name: Alice
print("Age:", person1.age)    # Output: Age: 30

# Using properties to modify attributes (setter)
person1.name = "Bob"
person1.age = 25

# Accessing modified attributes using properties (getter)
print("Name:", person1.name)  # Output: Name: Bob
print("Age:", person1.age)    # Output: Age: 25

# Trying to set a negative age (will be prevented by the setter property)
person1.age = -5              # Output: Age cannot be negative!
print("Age:", person1.age)    # Output: Age: 25 (age remains unchanged)

'''
#As you can see, we use the @property decorator above
# each getter method, and the @<property_name>.
# setter decorator above each setter method.
# This creates a property for the respective attribute,
# allowing us to access and modify it like a regular attribute,
# while still benefiting from the validation provided by the setter methods.


'''


# class variable vs instance/obj variable


class Employee:
  companyName = 'Apple' # class variable # common variable for all intances
  
  def __init__(self,name):
    self.name = name # instance variable # every instance has their own unique one
    

pri = Employee('pri')
pinki = Employee('pinki')
rinki = Employee('rinki')

print('pri.name => ', pri.name , ' from ', pri.companyName)
print('pinki.name => ', pinki.name, ' from ', pinki.companyName)

# changing class variable's value for a particular instance
rinki.companyName = 'Apple India'

print('rinki.name => ', rinki.name, ' from ', rinki.companyName)


'''



'''
# Time Module
import time

print(time.strftime("%x, %X, %y, %Y"))

'''





'''

# Commandline utility

# curl https://images.pexels.com/photos/674010/pexels-photo-674010.jpeg  --output wing.png 

'''



'''


# walrus operator
#The walrus operator allows you to assign a value 
# to a variable as part of an expression

#print(a:=8)

'''





'''

# shutil it use to manupulate file folder
# we can use os module as well
import shutil

shutil.copy("file-1.py","main.py")

'''





'''
# to make http request

import requests 

response = requests.get('https://google.com')

print(response.text)

# use bs4 module to beautify html

'''





'''
# generater in python
# it create value  on the fly . which is good for less memory

 #A generator is a special type of iterator 
#that generates values on-the-fly 
#rather than creating an entire sequence 
#and storing it in memory. Generators are defined 
#using functions with the yield keyword,
#which allows them to pause their execution 
#and save their state to resume later.
#This makes them memory-efficient and suitable 
#for handling large data sets or infinite sequences.

#they are lazy and run only when get an next()
def my_generator():
  for i in range(5):
    print('i=>',i)
    yield i
    
gen = my_generator()

print(next(gen))
print(next(gen))
print(next(gen))


'''



'''

# function caching

import functools
import time


@functools.lru_cache(maxsize=None)
def func(n):
  time.sleep(3)
  return n * 5

# This function will take an argument
# and get called after certain time

print('After 3 second ',func(5))
print('After 3 second',func(10))
print('After 3 second',func(15))

# This function will get called immediately
# because it has seen the argument values
print('After 3 second ',func(5))
print('After 3 second',func(10))
print('After 3 second',func(15))

#This function will take time again
# because the value is unseen to that function
print('After 3 second',func(20))


'''




'''

# AsyncIO

import asyncio
import time

async def  func1():
  await asyncio.sleep(1)
  print(f"func1 ran after 1 sec")
  return "func1 ran after 1 sec"
  
async def  func2():
  await asyncio.sleep(2)
  print(f"func2 ran after 2 sec")
  return "func2 ran after 2 sec"
  
async def  func3():
  await asyncio.sleep(3)
  print(f"func3 ran after 3 sec")
  return "func3 ran after 3 sec"



async def main():
  allValues = await asyncio.gather(
    func1(),
    func2(),
    func3(),
  )
  print('all returned values', allValues)

asyncio.run(main())

# Every function running simanantiously


'''

# multithreading

import time
import threading


def func(seconds):
  print(f"sleeping for {seconds} seconds")
  time.sleep(seconds)
  print(f"sleep complete for {seconds} seconds")
  
'''
#normal way # it will call functions
# one by one, once a funtion is done next will start
func(1)
func(2)
func(3)
func(4)
'''


'''

#threads
t1 = threading.Thread(target=func, args=[1])
t2 = threading.Thread(target=func, args=[2])
t3 = threading.Thread(target=func, args=[3])

#It will start all at once, as soon as it sees start
t1.start()
t2.start()
t3.start()

# use join to wait for another tofinish
t2.join()

'''

arr=['value 1','value 2', 'value 3']
tuple=('value 1','value 2', 'value 3')
obj={
  "key_1": "value 1",
  "key_2": "value 2",
  "key3": "value 3",
}

# one star
print('*arr =>',*arr )
print('*tuple =>', *tuple)
print('*obj =>', *obj)



# two star - to get all arguments


def func1(arg):
  print('arg', arg)
  print('**arg', **arg)
  
func1(name="value_1")


'''

# two star as keyword arguments
def func2(x, y):
  return x + y


print(func2(y=' val-y', x='val-x'))

#it is the equivalent of
values = {'x': 'val-x', 'y': ' val-y'}
print(func2(**values))

'''
