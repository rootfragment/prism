import hashlib
def hash(str):
    return hashlib.md5(str.encode()).hexdigest()

with open("test.txt" , "r") as f :
    for line in f:
        hash(line)
        print(hash(line))
        
