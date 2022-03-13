# from shape import Shape

# class NewClass(Shape):
#     print('i am from somewehere else ')

# n = NewClass()
# print(n.get_color())

##############################################################
############### Without Super Function ###############################

# class Parent:
#     def __init__(self) -> None:
#         print("Parent __init__",)

# class Child(Parent):
#     def __init__(self) -> None:
#         print('Child __init__')

# obj = Child()

                    #############################

# class Parent:
#     def __init__(self, name) -> None:
#         print("Parent __init__", name)

# class Child(Parent):
#     def __init__(self) -> None:
#         print('Child __init__')
#         Parent.__init__(self, "ahmad")

# obj = Child()

#######################################################################
################### With Super Function ###############################

# class Parent:
#     def __init__(self, name) -> None:
#         print("Parent __init__",name)

# class Child(Parent):
#     def __init__(self) -> None:
#         super().__init__('ahmad') 
# obj = Child()

#######################################################################

# class Parent:
#     def __init__(self, name) -> None:
#         print("Parent __init__",name)

# class Parent2:
#     def __init__(self, name) -> None:
#         print("Parent __init__",name)

# class Child(Parent, Parent2):
#     def __init__(self) -> None:
#         super().__init__('ahmad') 

# obj = Child()
# print(Child.__mro__)

#######################################################################

# class Salery:
#     def __init__(self, pay, reward):
#         self.pay = pay
#         self.reward = reward
    
#     def annual_salery(self):
#         return(self.pay*12) + self.reward

# class Employee:
#     def __init__(self, name, position, pay, reward):
#         self.name = name
#         self.position = position
#         self.f_salery = Salery(pay,reward)

#     def final_salery(self):
#         return(self.f_salery.annual_salery())

# obj = Employee('ahmad', 'tech guy',1000,100)
# print(obj.final_salery())

#########################################################################

# class Salery:
#     def __init__(self, pay, reward):
#         self.pay = pay
#         self.reward = reward
    
#     def annual_salery(self):
#         return(self.pay*12) + self.reward

# class Employee:
#     def __init__(self, name, position,sal):
#         self.name = name
#         self.position = position
#         self.f_salery = sal

#     def final_salery(self):
#         return(self.f_salery.annual_salery())

# sal = Salery(10000,100)
# emp = Employee('ahmad', 'tech guy',sal)
# print(emp.final_salery())

##########################################################################

# from abc import ABC, abstractmethod

# class ParentShape(ABC):
#     @abstractmethod
#     def area(self):
#         pass

#     @abstractmethod
#     def perimeter(self):
#         pass

# class ChildSquare(ParentShape):
#     def __init__(self,side):
#         self.__side = side
#         super().__init__()

# shap = ParentShape()
# squar = ChildSquare(1)

##############################################################################

# from abc import ABC, abstractmethod

# class ParentShape(ABC):
#     @abstractmethod
#     def area(self):
#         pass

#     @abstractmethod
#     def perimeter(self):
#         pass

# class ChildSquare(ParentShape):
#     def __init__(self,side):
#         self.__side = side
#         super().__init__()

#     def area(self):
#         return self.__side * self.__side

#     def perimeter(self):
#         return 4 * self.__side

# squar = ChildSquare(3)
# print(squar.area())
# print(squar.perimeter())
