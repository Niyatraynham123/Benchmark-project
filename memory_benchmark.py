import numpy as np
 import time
 
 # Console color codes for output
 RED_TEXT = "\x1b[31m"
 GREEN_TEXT = "\x1b[32m"
 YELLOW_TEXT = "\x1b[33m"
 RESET_TEXT = "\x1b[0m"
 
 def execute_memory_benchmark():
     array_size = 5_000_000_0  # Size of the NumPy array
     array_operations_time = 0  # To track the total time for operations
     
     # Initialize a large NumPy array with zeros
     large_array = np.zeros(array_size, dtype=np.int64)
     temporary_value_holder = 0  # To read array values into
 
     operation_start_time = time.time()
 
     # Populate the array with sequential values
     for index in range(array_size):
         large_array[index] = index
 
     # Iterate over the array to simulate read operations
     for index in range(array_size):
         temporary_value_holder = large_array[index]
