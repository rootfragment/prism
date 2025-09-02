import hashlib

    string = input("Enter the string :")
    encoded_string = string.encode()
    md5_hash = hashlib.md5(encoded_string).hexdigest()
    print(md5_hash)
