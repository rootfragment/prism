# Simple DBM Key-Value Store Example

This project demonstrates how to use Python's built-in `dbm` module to create a persistent key-value store.  
It stores numeric identifiers as keys and corresponding names as values.  
The database is backed by a file on disk, allowing data to persist across program runs.

## What is DBM?

`dbm` is a standard Python module that provides a dictionary-like interface backed by disk files.  
It works similarly to Python dictionaries, but instead of storing data only in memory, it stores them in a database file.  
This allows persistence between program executions.

## Features of This Program

- Store numeric IDs as string keys in a DBM database.  
- Associate each key with a human-readable name.  
- Retrieve values by their numeric keys.  
- Data is persistent in a file named `hi` (created automatically).  
- Simple API with two functions: `putt` and `chck`.  

## Functions

### `putt(num, name)`
- Takes a number (`num`) and a string (`name`).  
- Stores them in the DBM database with the number converted to a string as the key.  
- Prints a confirmation message that the entry has been stored.  

### `chck(num)`
- Takes a number (`num`).  
- Converts it to a string and checks if it exists as a key in the DBM database.  
- If found, prints the mapping from number to stored name.  
- If not found, no output is shown.  


## Why Use DBM?

- **Persistence**: Unlike a normal dictionary, data is stored on disk.  
- **Efficiency**: Lookups are fast and constant time on average.  
- **Simplicity**: Provides a very simple key-value API.  
- **No dependencies**: Included with Python by default.  

## File Structure

- `main.py` → Contains the program code with functions `putt` and `chck`.  
- `hi` → The DBM database file created automatically by the program.  
- `README.md` → Documentation for the project.  

## Use Cases

- Demonstrating how to use `dbm` in Python.  
- Learning about disk-backed dictionaries.  
- Storing small key-value datasets persistently.  
- Quick experiments with databases without installing external libraries.  

## Limitations

- Keys and values must be bytes (in this program, numbers are converted to strings and names are stored as strings).  
- The database format may differ across operating systems (e.g., `dbm`, `gdbm`, `ndbm`).  
- Not suitable for very large or complex datasets.  
