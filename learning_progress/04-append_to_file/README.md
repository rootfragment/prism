# Append to File Example in Python
---
This Python script demonstrates how to append content to an existing file using a context manager (with statement). It safely adds new lines without overwriting existing content.
---

## How It Works

1. **Open the file in append mode**
   The `with open("output.txt", "a") as f:` statement opens `output.txt` in append mode (`"a"`). If the file doesn't exist, it will be created. Existing content is preserved.

2. **Append content**
   The `f.write()` method adds the given string to the end of the file. `\n` ensures the new content starts on a new line.

3. **Automatic file closing**
   Using `with` ensures the file is automatically closed after appending, even if an error occurs.

---
## Notes

* Use append mode (`"a"`) to add content without overwriting the file.
* Replace `output.txt` with any file path to append to a different file.
