import dbm

def putt(num , name):
    with dbm.open("hi","c") as dbw:
        dbw[str(num)] = name
        print("stored ",num , name)
        
def check(num):
    with dbm.open("hi","r") as db:
        key = str(num)
        if key in db:
            print(f"[=] {num} → {db[key].decode()}")
            
if __name__ == "__main__":
    putt(101, "Alice")
    putt(202, "Bob")
    putt(303, "Charlie")
    putt(404, "Diana")
    putt(505, "Eve")

    chck(303)
    chck(101)
    chck(505)
