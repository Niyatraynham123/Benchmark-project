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
 
     # Writing 1 billion bytes to the file in chunks of 10,000 bytes
     with open(benchmark_file, "wb") as file:
         start_time = time.time()
         buffer = b'B' * write_read_chunk_size  # Change 'A' to 'B' for a slight variation
         total_bytes_written = 0
 
         while total_bytes_written < file_target_size:
             file.write(buffer)
             total_bytes_written += write_read_chunk_size
 
         end_time = time.time()
         total_operation_time += end_time - start_time
