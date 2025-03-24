from src.file_utils import find_files
from src.hash_utils import compute_sha256
from src.encryption import encrypt_file, decrypt_file
from Crypto.Random import get_random_bytes
import base64

# Specify your test folder (make sure it has some dummy files)
test_directory = "./test_files"

# List all files in the test directory
files = find_files(test_directory)
print("Found files:", files)

# For each file, compute and print its original SHA-256 hash
for file in files:
    original_hash = compute_sha256(file)
    print(f"Original hash for {file}: {original_hash}")

# Generate a random key and IV for AES encryption
key = get_random_bytes(16)
iv = get_random_bytes(16)
print("Encryption key (Base64):", base64.b64encode(key).decode())
print("IV (Base64):", base64.b64encode(iv).decode())

# Encrypt each file, then decrypt it and verify the hash
for file in files:
    encrypt_file(file, key, iv)
    print(f"Encrypted {file}")
    # Decrypt the file back
    decrypt_file(file, key, iv)
    print(f"Decrypted {file}")
    # Recompute hash to verify integrity
    new_hash = compute_sha256(file)
    print(f"New hash for {file}: {new_hash}")
    if original_hash == new_hash:
        print(f"SUCCESS: {file} was restored exactly.")
    else:
        print(f"ERROR: {file} does not match the original.")