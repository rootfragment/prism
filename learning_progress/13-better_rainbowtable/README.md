# Optimized MD5 Wordlist to DBM Storage

This project is an **improved version** of the earlier DBM-based hash storage program.  
Previously, the program was extremely **slow and impractical** because it opened and closed the database file for **every single word** in the wordlist.  
That meant millions of unnecessary disk operations when processing large wordlists like `rockyou.txt`.

In this updated version, the performance problem is solved by keeping the **DBM file open during the entire wordlist processing**.  
This reduces file I/O overhead drastically and makes the program much more usable.

---

## How It Works

1. The user provides a wordlist (e.g., `rockyou.txt`) and a filename for the database.  
2. Each word in the wordlist is hashed using MD5.  
3. The hash is stored as the **key** in the DBM database, and the original word is stored as the **value**.  
4. The user can later look up any MD5 hash and retrieve the matching word if it exists.  

---

## Menu Options

- **Option 1:** Process the wordlist, hash all entries, and store them in the DBM file.  
- **Option 2:** Lookup a given MD5 hash in the database.  
- **Option 3:** Exit the program.  

---

## Improvements Over Previous Version

- **Before:**  
  - The DBM file was opened and closed inside the loop for every word.  
  - This resulted in millions of open/close operations.  
  - Processing large wordlists could take hours or even longer.  

- **Now:**  
  - The DBM file is opened **once** per operation (`file_op`).  
  - All word hashes are written in a single session.  
  - Significantly faster and more practical.  

This update demonstrates how a small change in resource management can have a huge effect on performance.

---

## Notes

- This program is still for **educational purposes only**.  
- MD5 is cryptographically broken and not secure for real-world security applications.  
- The project is mainly useful for understanding how databases can be used for rainbow table–style lookups and how design choices affect performance.  

---
