import hashlib
import multiprocessing as mp
import time

def line_hash(line):
    word = line.strip()
    return word + ":" + hashlib.md5(word.encode()).hexdigest()
    
def process_(lines):
    return [line_hash(line) for line in lines]

def chunks(file , size):
    chunk = []
    for item in file:
        chunk.append(item)
        if len(chunk)==size:
            yield chunk
            chunk = []
    if chunk:
            yield chunk

filename = input("Enter the name of input file : ")
opfile = input("Enter the name of the output file : ")

start = time.time()
cpu_count = mp.cpu_count()

with open(filename, "r", encoding="latin-1", errors="ignore") as f:
    with open(opfile , "w") as fw:
        with mp.Pool(cpu_count) as pool:
            for results in pool.imap(process_,chunks(f,10000)):
                fw.write("\n".join(results) + "\n")
        
end = time.time()
print(f"time taken : {end -start:.2f} seconds")

