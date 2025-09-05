# MD5 Wordlist to DBM Storage

This project demonstrates how to hash words from a wordlist using MD5 and store the results in a disk-backed key-value database using Python's built-in `dbm` module.  
It also provides a simple lookup function to check if a hash exists in the database and retrieve the corresponding word.

## How It Works

1. The user provides a wordlist (e.g., `rockyou.txt`) and a filename for the database.  
2. Each word in the wordlist is hashed with MD5.  
3. The MD5 hash is stored as the key in the `dbm` database, and the original word is stored as the value.  
4. The user can later enter a hash value to look it up in the database.  

## Menu Options

- **Option 1:** Process the wordlist, hash all entries, and store them in the DBM file.  
- **Option 2:** Lookup a given MD5 hash in the database.  
- **Option 3:** Exit the program.  

## Performance Notes

This implementation is **extremely slow and impractical** for large wordlists like `rockyou.txt` (14+ million entries).  
The reason is that the program opens and closes the `dbm` database file for **every single word** being processed.  
This results in millions of expensive file operations, which makes the process take an unreasonably long time.  

On a modern machine, processing a large wordlist this way may take hours or even longer.  
For practical rainbow table generation or large dataset handling, this approach is not recommended.

## Why It Is Impractical

- **Inefficient storage:** Each database transaction involves opening and closing the DBM file.  
- **Excessive runtime:** Millions of words cause millions of disk operations.  
- **Better alternatives exist:**  
  - Keep the DBM file open during the entire wordlist processing.  
  - Use more efficient key-value stores like `sqlite`, `lmdb`, or `rocksdb`.  
  - Consider memory-mapped data structures for high performance.  

## Educational Value

Despite being impractical for real-world use, this project is useful for:  
- Learning how DBM databases work in Python.  
- Understanding the basics of rainbow table-like storage.  
- Demonstrating why naive approaches do not scale well.  

## Result
- Painfully slow , didnt have enough patience to sit through the process.
