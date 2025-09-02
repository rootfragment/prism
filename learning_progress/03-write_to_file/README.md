# Write File Example in Python

This Python script demonstrates how to write content to a file using a context manager (`with` statement). It safely handles file creation and writing.

---

## How It Works

1. **Open the file in write mode**
   The `with open("output.txt", "w") as f:` statement opens `output.txt` in write mode (`"w"`). If the file doesn't exist, it will be created. If it exists, it will be overwritten.

2. **Write content to the file**
   The `f.write()` method writes the given strings to the file. `\n` is used to insert a newline.

3. **Automatic file closing**
   Using `with` ensures the file is automatically closed after writing, even if an error occurs.

---

## Notes

* Using `with` is recommended for safe file operations.
* Replace `output.txt` with any file path to write to a different location or file name.
