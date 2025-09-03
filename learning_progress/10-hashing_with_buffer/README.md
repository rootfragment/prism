# MD5 File Hashing with Buffered Multiprocessing in Python

This Python script reads a text file line by line, computes MD5 hashes in parallel using multiprocessing, and writes results to an output file in buffered batches for efficiency.
---

## How It Works

1. **Import modules**

   * `hashlib` for MD5 hashing
   * `multiprocessing` to utilize multiple CPU cores
   * `time` to measure execution duration

2. **Define helper functions**

   * `line_hash(line)`: Computes `line:MD5_hash`.
   * `process_(lines)`: Computes hashes for a list of lines.
   * `chunks(file, size)`: Splits the file into chunks of the given size.

3. **Buffered writing**

   * `buffer` collects processed lines.
   * Writes to file only when `buffer` reaches `lines_per_write` for efficiency.

4. **Multiprocessing**

   * Uses a pool equal to the number of CPU cores.
   * Processes chunks of 10,000 lines in parallel.

5. **Total time measurement**
   Prints the total time taken for processing at the end.

---
## Notes

* Multiprocessing significantly improves performance for large files.
* MD5 is suitable for learning or non-critical tasks but not for cryptographic security.
* Using `latin-1` encoding and ignoring errors ensures robust handling of varied file content.
* Adjust `lines_per_write` or chunk size based on available system memory.

## Result
* This algorithm hashed all words in `rockyou.txt` in  **4.10** seconds.
* Runtime decreased by ~25.5% from parallel hashing.
