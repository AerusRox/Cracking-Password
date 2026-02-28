import crypt

password = input("Enter password: ")

# Create salted SHA-512 hash
hashed = crypt.crypt(password, crypt.mksalt(crypt.METHOD_SHA512))

with open("hashes.txt", "w") as f:
    f.write(hashed)

print("\nHash saved to hashes.txt")
print("Hash:", hashed)
