import operator
from functools import reduce

"""
dynamic_reducer([1,2,3], '+') # 6
dynamic_reducer([1,2,3], '-') # -4
dynamic_reducer([1,2,3], '*') # 6
dynamic_reducer([1,2,3], '/') # 
"""

def dynamic_reducer(collection, op):
    operators = {
        "+": operator.add,
        "-": operator.sub,
        "*": operator.mul,
        "/": operator.truediv,
    }

    return reduce((lambda total, element:
                   operators[op](total, element)), collection)

# total = flexible_counter([1,2,3], '/') #
0.1666666666666

print(dynamic_reducer([1,2,3], '+'))
print(dynamic_reducer([1,2,3], '-'))
print(dynamic_reducer([1,2,3], '*'))
print(dynamic_reducer([1,2,3], '/'))
#print (total)
