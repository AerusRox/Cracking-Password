import hashlib

password = input("Enter password to hash: ")

hashed = hashlib.sha256(password.encode()).hexdigest()

with open("hashes.txt", "w") as f:
    f.write(hashed)

print("Hash saved to hashes.txt")
print("SHA-256:", hashed)
