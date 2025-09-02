import hashlib,time

def hash_(str):
    return hashlib.md5(str.encode()).hexdigest()
    
start = time.time()
filename = input("Enter the name of input file : ")
opfile = input("Enter the name of the output file : ")
with open(filename, "r", encoding="latin-1", errors="ignore") as f:
    with open (opfile , "w") as fw:
        for line in f:
            hash_val = hash_(line.strip())
            fw.write(line.strip()  + ":" + hash_val+"\n")
            
            
end = time.time()
print(f"Finished in {end - start:.2f} seconds")
