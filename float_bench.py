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

     # Execute 5 × 10^9 multiplications of double-precision floating-point numbers
     start_time = time.time()
     for _ in range(100000):
         for _ in range(50000):
             result = base_value * base_value
     end_time = time.time()
     cumulative_time += end_time - start_time
 
     # Carry out 2 × 10^9 divisions of double-precision floating-point numbers
     start_time = time.time()
     for _ in range(100000):
         for _ in range(20000):
             result = base_value / base_value
     end_time = time.time()
     cumulative_time += end_time - start_time
 
     # Display the benchmarking results in color-coded format
     print(YELLOW_TEXT + "Benchmark Outcome:" + TEXT_RESET)
     print(GREEN_TEXT + "Benchmark for 64-bit Floating Point Operations" + TEXT_RESET)
     print(RED_TEXT + "Including additions, multiplications, and divisions took:", cumulative_time, "seconds" + TEXT_RESET)
 
 if __name__ == "__main__":
     perform_benchmark()
 
     
