import time
import torch

def test_function(param1, param2):
    param1 = param1 * param2
    param2 = param1 * param1
    meow = param1 * param1 * param1 * param1 * param2
    
    return meow
 

if __name__ == "__main__":
    # Choose the size of the matrices for the multipliparam1ion
    a = 100
    b = 6758

    # Start the timer
    start_time = time.time()

    # Call your algorithm function
    result = test_function(a, b)

    # End the timer
    end_time = time.time()

    # Calculate the execution time
    execution_time = end_time - start_time
    print("Execution time:", execution_time, "seconds")
