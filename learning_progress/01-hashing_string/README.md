# MD5 Hash Generator

A simple Python script that takes a string input from the user and computes its **MD5 hash** using Python's built-in `hashlib` library.

---

## How It Works

1. **Import the hashlib library**  
   Python's `hashlib` module provides secure hash and message digest algorithms.  
   ```python
   import hashlib
   ```

2. **Take input from the user**  
   Prompt the user to enter a string to hash.  
   ```python
   string = input("Enter the string: ")
   ```

3. **Encode the string to bytes**  
   Hash functions require bytes, so the input string is converted using `.encode()`.  
   ```python
   encoded_string = string.encode()
   ```

4. **Compute the MD5 hash**  
   Generate the MD5 hash and convert it to a readable hexadecimal string using `.hexdigest()`.  
   ```python
   md5_hash = hashlib.md5(encoded_string).hexdigest()
   ```

5. **Print the result**  
   Display the resulting MD5 hash.  
   ```python
   print("MD5 Hash:", md5_hash)
   ```

---

## Example Usage

```
Enter the string: hello
MD5 Hash: 5d41402abc4b2a76b9719d911017c592
```

---

## Notes

- MD5 is **not recommended for cryptographic security** because it is vulnerable to collisions.  
- This script is primarily for learning, testing, or non-critical applications.

---
