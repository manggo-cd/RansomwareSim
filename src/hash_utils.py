import hashlib

def compute_sha256(file_path: str) -> str:
    """
    Compute the SHA-256 hash for the file at the specified path.

    Args:
        file_path (str): The path to the file.

    Returns:
        str: The hexadecimal SHA-256 hash of the file.
    """
    sha256_hash = hashlib.sha256()
    # Read the file in binary mode in chunks to handle large files
    with open(file_path, "rb") as f: #rb is read binary mode aka raw bytes instead of text
        for byte_block in iter(lambda: f.read(4096), b""):
            sha256_hash.update(byte_block)
    # Return the hash in hexadecimal format
    return sha256_hash.hexdigest()


# 	iter(lambda: f.read(4096), b""):
# 	•	lambda: f.read(4096):
# This anonymous function reads up to 4096 bytes from the file each time it is called.
# 	•	4096:
# This is the chunk size (in bytes). Reading in chunks of 4096 bytes is efficient because:
# 	•	It prevents your program from loading the entire file into memory at once, which is especially useful for large files.
# 	•	4096 is a common block size in many systems.
# 	•	b"":
# This is an empty byte string. It serves as the sentinel value: when f.read(4096) returns b"", it means the end of the file has been reached.
# 	•	iter(..., b""):
# This creates an iterator that keeps calling the lambda function until it returns b"". Each time, the result is assigned to the variable byte_block.
# 	•	for byte_block in ...:
# 	•	byte_block:
# In each iteration, byte_block is a chunk of data (up to 4096 bytes) that was read from the file.
# 	•	sha256_hash.update(byte_block):
# This line feeds the chunk of bytes into the SHA-256 hash object. The update() method processes the chunk and combines it with any previous data to build the overall hash.