import hashlib
import os

password = input("Enter password: ")

# Generate random salt (8 bytes)
salt = os.urandom(8).hex()

# Combine salt + password
hash_value = hashlib.sha256((salt + password).encode()).hexdigest()

# Store in format: salt$hash
with open("hashes.txt", "w") as f:
    f.write(f"{salt}${hash_value}")

print("\nSaved to hashes.txt")
print("Salt:", salt)
print("Hash:", hash_value)
