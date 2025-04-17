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
