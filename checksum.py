import hashlib

print('Filame:')
file_name = input()
print('Original md5:')
original_md5 = input()
print('Original sha256:')
original_sha256 = input()

with open(file_name, 'rb') as file_to_check:
    data = file_to_check.read()    
    md5_returned = hashlib.md5(data).hexdigest()
if original_md5 == md5_returned:
    print("MD5 OK")
else:
    print("MD5 NOK")

with open(file_name, 'rb') as file_to_check:
    data = file_to_check.read()    
    ha256_returned = hashlib.sha256(data).hexdigest()
if original_sha256 == ha256_returned:
    print("sha256 OK")
else:
    print("sha256 NOK")