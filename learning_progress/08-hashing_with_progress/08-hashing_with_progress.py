import hashlib,time

def hash_(str):
    return hashlib.md5(str.encode()).hexdigest()

count =0
start = time.time()
filename = input("Enter the name of input file : ")
opfile = input("Enter the name of the output file : ")
with open(filename, "r", encoding="latin-1", errors="ignore") as f:
    with open (opfile , "w") as fw:
        for line in f:
            hash_val = hash_(line.strip())
            fw.write(line.strip()  + ":" + hash_val+"\n")
            count +=1 
            
            if (count%100000==0):
                elapsed_time = time.time()-start
                speed = count / elapsed_time 
                print(f"Processed {count:,} lines in {elapsed_time:.2f}s ({speed:,.0f} hashes/sec)")
end = time.time()
print(f"Finished in {end - start:.2f} seconds")
