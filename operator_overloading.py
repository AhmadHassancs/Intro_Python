# a = 10
# b = 20
# print(a+b)

# c = 'hello '
# d = 'world'
# print(c+d)

# e = [10,11,12]
# f = [1,2,3]
# print(e+f)

##########################################################

# class Pen:
#     def __init__(self, pages) -> None:
#         self.pages = pages
    
#     def __add__(self, other):
#         return self.pages + other.pages

# o1 = Pen(1)
# o2 = Pen(2)

# print(o1+o2)

############################################################

# a = int(input('Please enter the number of pensils you purchased: '))
# b = int(input('Please enter the number of pensils you used: '))

# class Pen:
#     def __init__(self, pensil) -> None:
#         self.pensil = pensil
    
#     def __sub__(self, other):
#         return self.pensil - other.pensil

# o1 = Pen(b)
# o2 = Pen(a)

# print('The Remaining amount of Pensils is: ', (o2 - o1))

############################################################

# a = int(input('Please enter your marks: '))
# b = int(input('Please enter total marks: '))

# class Percentage:
#     def __init__(self, marks) -> None:
#         self.marks = marks
    
#     def __mul__(self, other, per=100):
#         return self.marks * per / other.marks

# o1 = Percentage(a)
# o2 = Percentage(b)

# # o1.__mul__(o2)

# print('You have obtained a percentage of: ', o1.__mul__(o2))

#############################################################

# a = int(input('Please 1st number: '))
# b = int(input('Please 2nd number: '))

# class GreaterThen:
#     def __init__(self, number) -> None:
#         self.number = number
    
#     def __gt__(self, other):
#         return self.number > other.number

# o1 = GreaterThen(a)
# o2 = GreaterThen(b)

# if o1.__gt__(o2) == True:
#     print('1st number is greater then 2nd')
# else:
#     print('2nd number is greater then 1st number')

###########################################################

