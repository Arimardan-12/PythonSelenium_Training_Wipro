"""
Write a decorator called @execution_time that:
1. Measures the execution time of a function
2. Prints the function name and execution time
3. Apply this decorator to a function that calculates the factorial of a number using recursion			"""

import time

def execution_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()          # start time
        result = func(*args, **kwargs)    # function execution
        end_time = time.time()            # end time

        print(f"Function '{func.__name__}' executed in {end_time - start_time:.6f} seconds")
        return result
    return wrapper
#using the decorator

@execution_time
def sample_function():
    total = 0
    for i in range(1, 1000000):
        total += i
    return total


sample_function()