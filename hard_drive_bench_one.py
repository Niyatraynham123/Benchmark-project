import os
 import time
 
 # ANSI escape sequences for text color
 COLOR_RED = "\x1b[31m"
 COLOR_GREEN = "\x1b[32m"
 COLOR_YELLOW = "\x1b[33m"
 COLOR_RESET = "\x1b[0m"
 
 def perform_disk_io_benchmark():
     file_size_bytes = 1_000_000_000  # 1 billion bytes
     chunk_size = 100  # bytes
     elapsed_time = 0  # seconds
 
     # Write 1 billion bytes to a file, in chunks of 100 bytes each
     file_name = "benchmarkFile.txt"
     with open(file_name, "wb") as file:
         start_time = time.time()
         buffer = b'A' * chunk_size
         for _ in range(file_size_bytes // chunk_size):
             file.write(buffer)
         end_time = time.time()
         elapsed_time += end_time - start_time
