import hashlib

def hash_(str):
    return hashlib.md5(str.encode()).hexdigest()
    
filename = input("Enter the name of input file : ")
opfile = input("Enter the name of the output file : ")
with open (filename, "r") as f :
    with open (opfile , "w") as fw:
        for line in f:
            hash_val = hash_(line.strip())
            fw.write(line.strip()  + ":" + hash_val+"\n")
            
