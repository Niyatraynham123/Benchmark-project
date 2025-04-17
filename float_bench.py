import time
 
 # Color codes for terminal output
 RED_TEXT = "\x1b[31m"
 GREEN_TEXT = "\x1b[32m"
 YELLOW_TEXT = "\x1b[33m"
 TEXT_RESET = "\x1b[0m"
 
 def perform_benchmark():
     cumulative_time = 0
     base_value = 8.4
     result = 0
  
     # Perform 10^10 additions of double-precision floating-point numbers
     start_time = time.time()
     for _ in range(100000):
         for _ in range(100000):
             result = base_value + base_value
     end_time = time.time()
     cumulative_time += end_time - start_time
 
     
