# Cracking-Password
Here’s a clean, professional **README description** you can paste into your GitHub project.

---

# 🔐 Password Cracking and Hashing with Salting Techniques

## 📌 Project Overview

This project demonstrates how password hashing works and how weak passwords can be cracked using brute-force and wordlist attacks. It also shows how **salting techniques** improve security by preventing precomputed and rainbow table attacks.

The project integrates Python-based hash generation with **John the Ripper** to simulate real-world password auditing in a controlled lab environment.

> ⚠️ This project is for educational and ethical security testing purposes only.

---

## 🎯 Objectives

* Understand cryptographic hash functions
* Implement SHA-256 hashing in Python
* Apply salting techniques
* Crack weak hashes using John the Ripper
* Analyze the impact of salting on password security

---

## 🛠 Tools & Technologies

* Python 3
* hashlib module
* crypt module
* John the Ripper
* Linux / macOS terminal

---

## 🔎 Key Concepts Covered

### 1️⃣ Hashing

Passwords are converted into fixed-length hashes using SHA-256 or SHA-512. Hashing ensures passwords are not stored in plaintext.

### 2️⃣ Brute-Force & Wordlist Attacks

Using John the Ripper, the project demonstrates how weak passwords can be cracked by:

* Trying common passwords (wordlist attack)
* Trying character combinations (incremental mode)

### 3️⃣ Salting

Salting adds random data to a password before hashing:

```
hash = SHA256(salt + password)
```

This ensures:

* Identical passwords produce different hashes
* Rainbow tables become ineffective
* Each hash must be attacked individually

---

## 📂 Project Structure

```
john_salted_project/
│
├── generate_salted_hash.py
├── generate_unix_hash.py
├── hashes.txt
└── wordlist.txt
```

---

## 🚀 How It Works

1. Generate a salted hash using Python.
2. Save the hash to `hashes.txt`.
3. Run John the Ripper to attempt cracking.
4. Compare results between salted and unsalted hashes.

---

## 📊 Learning Outcomes

After completing this project, you will understand:

* Why fast hashes like SHA-256 are vulnerable
* Why short passwords are easily cracked
* How salting strengthens password storage
* How password cracking tools operate
* Why modern systems use slower hashing algorithms

---

## 🔐 Real-World Security Note

Modern systems use stronger password hashing functions such as:

* bcrypt
* Argon2

These algorithms are intentionally slow and include built-in salting mechanisms to resist brute-force and GPU-based attacks.

---

## ⚖️ Disclaimer

This project is intended for:

* Cybersecurity students
* Ethical hacking labs
* Academic demonstrations

Do not use these techniques on systems without explicit permission.

---


