import time
 
 # Terminal color codes
 COLOR_CODE_RED = "\x1b[31m"
 COLOR_CODE_GREEN = "\x1b[32m"
 COLOR_CODE_YELLOW = "\x1b[33m"
 COLOR_CODE_RESET = "\x1b[0m"
 
 def execute_benchmark():
     accumulated_time = 0
     test_value = 7
     calculation_result = 0

     # Execute 10^10 additions of integer constants
     beginning_time = time.time()
     for _ in range(100000):
         for _ in range(100000):
             calculation_result = test_value + test_value
     completion_time = time.time()
     accumulated_time += completion_time - beginning_time

     # Perform 5 × 10^9 multiplications of integer constants
     beginning_time = time.time()
     for _ in range(100000):
         for _ in range(50000):
             calculation_result = test_value * test_value
     completion_time = time.time()
     accumulated_time += completion_time - beginning_time

     # Conduct 2 × 10^9 divisions of integer constants
     beginning_time = time.time()
     for _ in range(100000):
         for _ in range(20000):
             calculation_result = test_value // test_value
     completion_time = time.time()
     accumulated_time += completion_time - beginning_time
 
      # Output the benchmark results with color coding
     print(COLOR_CODE_YELLOW + "Benchmark 1:" + COLOR_CODE_RESET)
     print(COLOR_CODE_GREEN + "32-bit Integer Operation Benchmark" + COLOR_CODE_RESET)
     print(COLOR_CODE_RED + "Involving additions, multiplications, and divisions took:", accumulated_time, "seconds" + COLOR_CODE_RESET)
 
 if __name__ == "__main__":
     execute_benchmark()
