# MD5 File Hashing with Progress Logging in Python

This Python script reads a text file line by line, computes the MD5 hash of each line, writes the results to an output file, and logs progress every 100,000 lines. It also measures total execution time.
---

## How It Works

1. **Import modules**

   * `hashlib` for computing MD5 hashes
   * `time` for measuring execution time

2. **Define hashing function**
   `hash_()` encodes a string to bytes and returns its MD5 hash as a hexadecimal string.

3. **Initialize counters and start time**
   `count` tracks processed lines, and `start` records the start time.

4. **Read input file and write output file**
   Each line is stripped, hashed, and written to the output file in `original_line:hash` format.

5. **Progress logging**
   Every 100,000 lines, the script prints processed lines, elapsed time, and processing speed (hashes/sec).

6. **Total execution time**
   After processing all lines, the script prints the total time taken.

---
## Notes

* MD5 is not secure for cryptographic purposes but useful for learning, testing, or checksums.
* Using `latin-1` encoding with `errors="ignore"` allows the script to handle files with mixed or invalid characters.
* Processing speed depends on file size and system performance.
---

## Result
* No change from 33 seconds average
