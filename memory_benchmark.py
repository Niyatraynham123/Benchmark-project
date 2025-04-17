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
