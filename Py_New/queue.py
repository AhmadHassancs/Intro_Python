# uses FIFO rule

# from queue import Queue

# fifo_list = Queue()

# # inser values in a queue

# fifo_list.put('ahmad')
# fifo_list.put('hassan')
# fifo_list.put('khan')

# fifo_list.get()

################# Deque ##############################

# uses LIFO rule

from collections import deque

my_deque = deque()

my_deque.append('ahmad')
my_deque.append('hassan')
my_deque.append('khan')

print(my_deque)