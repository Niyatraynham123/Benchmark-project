import os
 import time
 
 # Text color codes for console output
 RED_TEXT = "\x1b[31m"
 GREEN_TEXT = "\x1b[32m"
 YELLOW_TEXT = "\x1b[33m"
 RESET_TEXT = "\x1b[0m"
 
 def run_file_io_benchmark():
     file_target_size = 1_000_000_000  # Target size of the file in bytes
     write_read_chunk_size = 10_000  # Size of each write/read operation in bytes
     total_operation_time = 0  # To accumulate the time taken for operations
 
     # File name for the benchmarking process
     benchmark_file = "benchmarkFileOneBillionBytes.txt"
