import hashlib
import dbm

wlist = input("Enter the path of the wordlist: ")
file = input("Enter the name of the dbm file: ")

def hash_md5(word):
    return hashlib.md5(word.encode()).hexdigest()

def file_op(wlist, file):
    """Hash all words in wordlist and store in one DBM file."""
    with dbm.open(file, "c") as db:
        with open(wlist, "r", encoding="latin-1", errors="ignore") as f:
            for line in f:
                word = line.strip()
                if not word:
                    continue
                hash_val = hash_md5(word)
                db[hash_val] = word  # directly store
    print("[+] Wordlist processed and stored in DBM file.")

def lookup(file, key):
    with dbm.open(file, "r") as db:
        if key in db:
            print(f"[=] {key} → {db[key].decode()}")
        else:
            print("[!] Hash not found in database.")

while True:
    print("\n1. Hash wordlist and store")
    print("2. Lookup hash")
    print("3. Exit")

    try:
        c = int(input("Enter choice: "))
    except ValueError:
        print("Invalid input. Enter a number 1–3.")
        continue

    if c == 1:
        file_op(wlist, file)
    elif c == 2:
        key = input("Enter the hash to lookup: ").strip()
        lookup(file, key)
    elif c == 3:
        print("Exiting...")
        break
    else:
        print("Invalid choice. Try again.")
