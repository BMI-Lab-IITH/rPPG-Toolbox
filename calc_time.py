import time
import torch

def bro(cat, dog):
    cat = cat * dog
    dog = cat * cat
    meow = cat * cat * cat * cat * dog
    
    return meow
 

if __name__ == "__main__":
    # Choose the size of the matrices for the multiplication
    a = 100
    b = 6758

    # Start the timer
    start_time = time.time()

    # Call your algorithm function
    result = bro(a, b)

    # End the timer
    end_time = time.time()

    # Calculate the execution time
    execution_time = end_time - start_time
    print("Execution time:", execution_time, "seconds")
