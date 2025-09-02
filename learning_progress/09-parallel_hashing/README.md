# MD5 File Hashing with Multiprocessing in Python

This Python script demonstrates how to use multiprocessing to compute MD5 hashes of lines in a large text file efficiently. It reads an input file, hashes each line in parallel, and writes the results to an output file.
---
## How It Works

1. **Import modules**

   * `hashlib` for computing MD5 hashes
   * `multiprocessing` to parallelize processing
   * `time` for measuring execution time

2. **Define helper functions**

   * `line_hash(line)`: Returns `line:MD5_hash` for a single line.
   * `process_(lines)`: Computes hashes for a list of lines.
   * `chunks(file, size)`: Splits the file into chunks of specified size for parallel processing.

3. **Read input and open output file**
   The script uses `latin-1` encoding and ignores errors to handle mixed or invalid characters.

4. **Parallel processing**
   The script creates a multiprocessing pool equal to the number of CPU cores. Chunks of 10,000 lines are processed in parallel, and the results are written to the output file.

5. **Measure total time**
   The total time taken for processing is printed at the end.
---

## Notes

* Multiprocessing speeds up hashing significantly for large files.
* MD5 is not recommended for cryptographic security but is useful for learning and testing.
* Adjust the chunk size for optimal performance based on system resources.
---
## Result 
* The algorithm hashed all words in `rockyou.txt` in 5.9 seconds.
* Runtime decreased by ~83%.
