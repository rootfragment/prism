# MD5 File Hashing Example in Python

This Python script reads a file line by line, computes the MD5 hash of each line, and prints it to the console using Python's `hashlib` module.
---

## How It Works

1. **Import hashlib**
   The `hashlib` module provides secure hash algorithms, including MD5.

2. **Define a hashing function**
   The `hash()` function takes a string, encodes it to bytes, and returns the MD5 hash as a hexadecimal string.

3. **Open the file in read mode**
   Using `with open("test.txt", "r") as f:` ensures the file is properly closed after reading.

4. **Iterate over each line**
   The script reads the file line by line. For each line, it computes the MD5 hash and prints it.

---
## Notes

* MD5 is not recommended for cryptographic security due to vulnerabilities, but it is useful for learning and simple hashing tasks.
* This script can be adapted for any text file to compute line-by-line hashes.
