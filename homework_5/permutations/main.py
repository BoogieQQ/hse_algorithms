import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from tracer.main import trace_recursion

@trace_recursion
def permutations(arr):
    if len(arr) == 0:
        return [[]]
    
    res = []
    for index, elem in enumerate(arr):
        subarr = arr[:index] + arr[index+1:] 
        res.extend([[elem] + perm for perm in permutations(subarr)])
    
    return res
