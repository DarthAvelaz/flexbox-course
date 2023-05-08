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