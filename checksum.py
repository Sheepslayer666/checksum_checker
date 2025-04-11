import hashlib

file_name = input("Filename: ")
original_md5 = input("Original md5:")
original_sha256 = input("Original sha256: ")

with open(file_name, 'rb') as file_to_check:
    data = file_to_check.read()    
    md5_returned = hashlib.md5(data).hexdigest()
if original_md5 == md5_returned:
    print("MD5 OK")
else:
    print("MD5 not okay")

with open(file_name, 'rb') as file_to_check:
    data = file_to_check.read()    
    sha256_returned = hashlib.sha256(data).hexdigest()
if original_sha256 == sha256_returned:
    print("sha256 OK")
else:
    print("sha256 not okay")