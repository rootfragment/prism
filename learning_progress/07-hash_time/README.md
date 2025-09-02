# MD5 File Hashing with Timing in Python

This Python script reads a text file line by line, computes the MD5 hash of each line, writes the results to an output file, and measures the total execution time.
---
## How It Works

1. **Import modules**

   * `hashlib` for computing MD5 hashes.
   * `time` for measuring execution time.

2. **Define a hashing function**
   `hash_()` encodes a string to bytes and returns its MD5 hash as a hexadecimal string.

3. **Measure start time**
   `start = time.time()` records the start time.

4. **Read input file and write output file**
   The script reads each line from the input file (`filename`) using `latin-1` encoding and ignoring errors, computes its MD5 hash, and writes it to the output file (`opfile`) in the format `original_line:hash`.

5. **Measure end time and print duration**
   `end = time.time()` calculates the total time, which is printed in seconds.
---

## Notes

* MD5 is not secure for cryptographic purposes but useful for learning and testing.
* Using `latin-1` encoding and ignoring errors ensures the script can handle files with mixed or invalid characters.
* Execution time varies based on file size and system performance.
* Running the program back to back on the same wordlist will drastically improve perfomance as most of the text in wordfile would already be present in the RAM , 
---
## Result
* Algorithm hashed all the words in `rockyou.txt` at **33** seconds average.
* An average of 26.5 seconds was recorded when the program was run back to back on the same wordfile.
---
