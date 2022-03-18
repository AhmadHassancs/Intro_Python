# names = ['ahmad','hassan','ibrar','ibrahim']

# new_var = enumerate(names)
# # print(type(new_var))
# # print(new_var)

# # for i in new_var:
# #     print(i)

# # print(list(new_var))

# for i, j in enumerate(names):
#     print(i,j)

#########################################################
################## EXEC FUNCTION ########################

# exec("print('this is crazzy')")

# crazzy = '''
# x= 10
# y = 20
# print('The sum of x and y is: ',x+y)

# '''
# exec(crazzy)

##########################################################

# x = input('Enter something: ')
# # Enter something: [print(i ** 2) for i in [10,20,30]]

# exec(x)
# # 100
# # 400
# # 900

###########################################################

# from math import *
# code = '''
# x= sqrt(16)
# print(x)
# '''
# exec(code, {'sqrt':sqrt})
# # 4.0

###########################################################
################### *args #################################

# def add(*args):
#     result=0
#     for i in args:
#         result = result+i
#     print(result)

# add(10,20,20)
# add(1,2,3,4,5,6)

# def another(**kwargs):
#     print(kwargs)

# another(name = 'Ahmad', designation = 'Programmer', age = 23)

##############################################################

# def crazzy(**kwargs):
#     for i,j in kwargs.items():
#         print('{} is equal to {}'.format(i,j))

# crazzy(name = 'ahmad',age = 23, designation = 'programmer')

################################################################
############## ETERATOR CLASS ##################################

# class Incrementing:
#     def __iter__(self):
#         self.count = 0
#         return self
    
#     def __next__(self):
#         x = self.count
#         self.count = self.count + 1
#         return x