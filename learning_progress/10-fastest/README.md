# High-Performance MD5 File Hasher in Python

This Python script demonstrates a highly optimized approach to hashing lines of a text file using MD5. It leverages multiprocessing and buffered writing for maximum speed while stripping unnecessary commands to deliver a pure and streamlined experience.
---

## Features and Highlights

* **Maximum Python Speed:** This program is stripped to essentials for the fastest possible performance in Python.
* **Multiprocessing:** Utilizes all available CPU cores to parallelize MD5 hashing.
* **Buffered Writing:** Writes results in batches for efficiency, reducing I/O overhead.
* **Pure Experience:** Minimal code and no unnecessary operations provide a clean and focused hashing experience.
* **Robust Handling:** Reads files in `latin-1` encoding and ignores errors to handle diverse file content.
---
## Notes

* MD5 is **not recommended for cryptographic security**, but this script is ideal for learning, testing, or large-scale hash precomputation.
* Adjust `lines_per_write` or chunk size according to system memory for optimal performance.
* The program aims to deliver the **fastest Python-based MD5 hashing experience** while remaining simple and effective.

---
## Result

* This algorithm hashes the whole of `rockyou.txt` in 4.08 seconds.
* Runtime decreased by ~0.49% a very small improvement.
