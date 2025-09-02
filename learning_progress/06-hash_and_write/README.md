# MD5 Hash File to File Example in Python

This Python script reads a text file line by line, computes the MD5 hash of each line, and writes the results to an output file in the format `original_line:hash`.
---

## How It Works

1. **Import hashlib**
   The `hashlib` module provides secure hash functions, including MD5.

2. **Define a hashing function**
   `hash_()` takes a string, encodes it to bytes, and returns its MD5 hash as a hexadecimal string.

3. **Input file names**
   The user is prompted for the input file (`filename`) and output file (`opfile`).

4. **Read input and write output**
   The script reads each line from the input file, computes the MD5 hash of the stripped line, and writes it to the output file in the format `original_line:hash`.
---

## Notes

* MD5 is not secure for cryptographic purposes but is useful for learning, testing, or checksums.
* The script preserves line order and writes each original line with its hash.
* Ensure the input file exists in the working directory or provide the full path.
