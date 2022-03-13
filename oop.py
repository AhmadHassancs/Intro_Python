# class my_class():
#     print('I am from class')

##########################################################

# a = input("Please enter your name: ")
# class my_class(a):
#     if a == 'ahmad':
#         print('Welcome!')
#     else:
#         print('Sorry')

##########################################################

# class crazzy:
#     def my_method(self):
#         print('I am from a methos inside a function!!!')

# st = crazzy()
# st.my_method()

###########################################################

# class student:
#     def __init__(self):
#         self.name = 'hassan'
#         self.age = 23
#         self.marks = 80

# st = student()
# print(st.name)
# print(st.age)
# print(st.marks)

###########################################################

# class student:
#     def __init__(self):
#         self.name = 'hassan'
#         self.age = 23
#         self.marks = 80
    
#     def talk(self):
#         print('Name: ', self.name)
#         print('Age: ', self.age)
#         print('Marks: ', self.marks)


# st = student()
# # print(st.talk())

# st.name = 'ahmad'
# print(st.name)

# st1 = student()
# print(st1.name)

###########################################################

# n = input('Please Enter your name: ')
# a = int(input('Please Enter your age: '))
# m = int(input('Please Enter your marks: '))

# class my_class:
#     def __init__(self, name, age, marks):
#         self.name = name
#         self.age = age
#         self.marks = marks


#     def display(self):
#         print('Your name is: ', self.name)
#         print(f'You are {self.age} years old')
#         print(f'You got {self.marks} marks')


# o = my_class(n,a,m)
# o.display()

############################################################

# class my_class:
#     def __init__(self, name, age, *marks):
#         self.name = name
#         self.age = age
#         self.marks = marks


#     def display(self):
#         print('Your name is: ', self.name)
#         print(f'You are {self.age} years old')
#         print('Your marks:', self.marks)


# o = my_class("Hassan", 23, 100,101,102)
# o.display()

############################################################

# class my_class:
#     def __init__(self, name, age, **marks):
#         self.name = name
#         self.age = age
#         self.marks = marks


#     def display(self):
#         print('Your name is: ', self.name)
#         print(f'You are {self.age} years old')
#         print(f'Your marks: ',self.marks )


# o = my_class(name = 'Ahmad', age = 23, math = 80, science = 89, english =78)
# o.display()

#############################################################

# class Weight:
#     def __init__(self):
#         self.weight = 73

# w = Weight()
# print(w.weight)

# w = Weight()
# w.weight = 80  # I can change the value of the object
# print(w.weight)

###############################################################

# class Weight:
#     def __init__(self):
#         self.weight = 73
#         self.__new_weight = 89 # using __ to make a variable private

# w = Weight()
# print(w.weight)

# w.__new_weight = 100 # I cannot print the value of __new_weight but I can still modify it
# print(w.__new_weight)

################################################################

# class Weight:
#     def __init__(self):
#         self.weight = 73
#         self.__new_weight = 89 # using __ to make a variable private
    
#     def get_new_weight(self): # using this method, we can print the value of a privete variable
#         return self.__new_weight

# w = Weight()
# print(w.weight)
# print(w.get_new_weight())

#################################################################

# class Weight:
#     def __init__(self):
#         self.weight = 73
#         self.__new_weight = 89 # using __ to make a variable private
    
#     def get_new_weight(self): # using this method, we can print the value of a privete variable
#         return self.__new_weight
    
#     def set_new_weight(self, new_weight):
#         self.__new_weight = new_weight

# w = Weight()
# print(w.get_new_weight())
# w.set_new_weight(100)
# print(w.get_new_weight())

####################################################################

# class PublicPrivateMethods:
#     def __init__(self):
#         self.x = 10
#         self._y = 20
#         self.__z = 30
    
#     def public_method(self):
#         print(self.x)
#         print(self._y)
#         print(self.__z)

#     def __private_method(self): # __ is used to make a method private
#         print('I am from a Private method!!')

# obj = PublicPrivateMethods()
# obj.public_method()
# obj.__private_method()

#####################################################################

# class PublicPrivateMethods:
#     def __init__(self):
#         self.x = 10
#         self._y = 20
#         self.__z = 30
    
#     def public_method(self):
#         print(self.x)
#         print(self._y)
#         print(self.__z)
#         self.__private_method() # we can call a private method inside a public mehtod

#     def __private_method(self): # __ is used to make a method private
#         print('I am from a Private method!!')

# obj = PublicPrivateMethods()
# obj.public_method()

########################################################################

# class Polygon:
#     __width = None
#     __height = None

#     def set_value(self, width, height):
#         self.__width = width
#         self.__height = height

#     def get_width(self):
#         return self.__width
    
#     def get_height(self):
#         return self.__height
    
# class Square(Polygon): # I inherited Polygon in Square
#     def area(self):
#         return self.get_width() * self.get_height()

# obj = Square()
# obj.set_value(8,8)

# print(obj.area())

########################################################################

# class Polygon:
#     __width = None
#     __height = None

#     def set_value(self, width, height):
#         self.__width = width
#         self.__height = height

#     def get_width(self):
#         return self.__width
    
#     def get_height(self):
#         return self.__height
    
# class Square(Polygon): # I inherited Polygon in Square
#     def area(self):
#         return self.get_width() * self.get_height()

# class Triangle(Polygon):
#     def area(self):
#         return self.get_height()*self.get_width()*1/2

# obj = Triangle()
# obj.set_value(10,20)
# print(obj.area())

########################################################################

