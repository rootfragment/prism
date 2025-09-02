# Read File Example in Python

This Python script demonstrates how to open and read the contents of a file. It uses a context manager (`with` statement) to safely handle the file.


---
## How It Works

1. **Open the file**
   The `with open("test.txt", "r") as file:` statement opens `test.txt` in read mode (`"r"`). Using `with` ensures that the file is properly closed after reading.

2. **Read the contents**
   `file.read()` reads the entire content of the file into the variable `content`.

3. **Print the contents**
   The script prints the content to the console, prefixed with `File contents:`.

---
## Notes

* Using `with` is recommended because it automatically closes the file even if an error occurs.
* Replace `test.txt` with the path to any file you want to read.
