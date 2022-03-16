from collections import namedtuple
from traceback import print_tb
from unicodedata import name

# # namedtuple is light weight object
# # 'tup' is a class

# tup = namedtuple('my_tuple',['x','y','z'])
# # assign values for x,y,z

# # 'new_tup' is an object
# new_tup = tup(1,2,3)
# print(new_tup)

# # returns true if the variable belongs to a certain class
# print(isinstance(new_tup, tuple))
#######################################################

# my = namedtuple('this_tuple',['a','b'])
# new_my = my({'a':[1,2]}, {'b':[3,4]})
# print(new_my[0]['a'][0])
# print(new_my[1]['b'][0])

#######################################################

# # unpacking tuple
# my = namedtuple('this_tuple',['a','b'])
# new_my = my({'a':[1,2]}, {'b':[3,4]})

# x,y = new_my
# print(x,y)
# print(type(x)) # dictionary

###########################################################

# #iterating over an object

# my = namedtuple('this_tuple',['a','b'])
# new_my = my({'a':[1,2]}, {'b':[3,4]})

# for i in new_my:
#     print(i)

###########################################################

# #iterating over an object

# my = namedtuple('this_tuple',['a','b','c','d'])
# new_my = my(100,200,300,400)
# print(type(new_my))
# for i in new_my:
#     print(i)

#############################################################

# new_circle = namedtuple('new_circle',
#                         'center_x,center_y,_radius',
#                         rename=True)

# print(new_circle._fields)