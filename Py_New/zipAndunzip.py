# for i in zip([1,2,3],['a','b','c']):
#     print(i)

# for item in zip([10,11,12,13]):
#     print(item)

# for i in zip([1,2,3],['a','b','c'],[10,11,12,13]):
#     print(i)

# x = set(zip([1,2,3],['a','b','c']))
# print(x)

# unziping values

# unzip = zip([10,20,30],['x','y','z'],['@','#','$'])
# a,b,c = zip(*unzip)
# print(a,b,c)

#################################################################
############### EVALUATE PYTHON EXPRESSION ######################

# z = eval('10**2')
# print(z)
# # 100

# print(eval('sum([1,1,1,1,1])'))
# # 5

# i = 5
# print(eval('i*5'))
# # 25

# a= 5
# b = 2
# print(eval('a + b',{'a':a,'b':b}))
# # 7


# a= 5
# b = 2
# print(eval('a - b',{'a':a,'b':b}))
# # 3

# a= 5
# b = 2
# print(eval('a * b',{'a':a,'b':b}))
# # 10

######################################################################
################ MEMORYVIEW FUNCTION #################################

# x = b'hello world'
# print(type(x))

# new = memoryview(x)
# print(type(new))
# print(new)

# printing the original data

# print(new.obj)

# ASCII values of the bytes object that we created

# print(new.tolist())


z = bytearray('python is crazzy','utf-8')
print(type(z))

y = memoryview(z)
print(y)
# memory location

print(y[2])
# ASCII code

print(chr(y[2]))
# specific character at that index