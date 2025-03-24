# Ransomware Simulation Tool

A Python-based ransomware simulation tool that demonstrates file encryption and decryption using AES encryption, SHA-256 file integrity checks, and a custom Tkinter GUI styled with the Forest Light theme. **This project is for educational and demonstration purposes only.**

---

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [How It Works](#how-it-works)
- [License](#license)

---

## Overview

This project simulates ransomware behavior by:
- Encrypting files in a selected folder using AES (CBC mode).
- Replacing the original file content with a ransom note.
- Saving the actual encrypted data as a backup (with a `.encrypted` extension).
- Allowing decryption by reading the backup file and restoring the original content.
- Verifying file integrity using SHA-256 hashes.
- Providing a user-friendly GUI built with Tkinter, featuring a custom Forest Light theme.

---

## Features

- **File Encryption & Decryption**: Securely encrypt files and restore them using AES encryption.
- **Ransom Note Simulation**: Original file contents are replaced with a ransom note.
- **Backup Creation**: Encrypted data is saved in a backup file to allow restoration.
- **File Integrity Verification**: Uses SHA-256 hashing to verify that decrypted files match their original contents.
- **Custom GUI with Theme**: A Tkinter-based GUI styled with the Forest Light theme.
- **File Preview Popup**: A feature to preview file contents (e.g., the ransom note).

---

## Technologies Used

- **Python 3.x**
- **Tkinter** (with Tcl/Tk 8.6) for the GUI
- **PyCryptodome** for AES encryption/decryption
- **hashlib** for SHA-256 hash computation
- **Tcl/Tk** for applying the custom Forest Light theme

---

---

## Installation

### Prerequisites

- Python 3.x (Ensure you are using a version with Tcl/Tk 8.6 – consider installing from [python.org](https://www.python.org/downloads/mac-osx/) if needed)
- Git (optional, for cloning the repository)
- Virtual Environment (venv)

### Steps

1. **Clone the Repository** (or download it as a ZIP):
   ```bash
   git clone https://github.com/yourusername/RansomwareSim.git
   cd RansomwareSim

2. **Create a Virtual Environment:**
    ```bash
    python3 -m venv venv

3. **Activate the Virtual Environment:**
    •	On macOS/Linux:
    ```bash
    source venv/bin/activate

    •	On Windows:
    ```bash
    venv\Scripts\activate

4.	**Install Dependencies:**
    ```bash
    pip install pycryptodome

5. **Ensure Tcl/Tk 8.6+ is Installed:**
    Run the following to check:
    ```bash
    python3 -c "import tkinter; print(tkinter.TkVersion)"

    If the version is less than 8.6, install a newer Python version from python.org.

## Usage

### Running the GUI

```bash
python3 -m src.gui
```

### Inside the GUI

- **Select Folder**:  
  Choose the folder containing the files you want to encrypt.

- **Encrypt Files**:  
  - Each file is:
    - Hashed using SHA-256
    - Encrypted using AES (CBC mode) with a random key and IV
    - Encrypted content is saved to `<filename>.encrypted`
    - Original file is overwritten with a ransom note

- **Decrypt Files**:  
  - Prompts for the Base64-encoded key and IV
  - Decrypts the corresponding `.encrypted` file
  - Restores the original file content
  - Verifies the integrity by comparing SHA-256 hashes

- **Preview File**:  
  - Opens a popup displaying the contents of a file
  - Helpful for inspecting the ransom note or checking restored files

---

## How It Works

### Encryption Flow

1. **Read File**: Loads the file in binary mode.
2. **Encrypt Data**: Uses AES (CBC mode) with a 16-byte key and IV.
3. **Save Encrypted Backup**: Stores encrypted data as `<filename>.encrypted`.
4. **Overwrite Original File**: Replaces the original content with a ransom note.

### Decryption Flow

1. **Prompt for Key & IV**: User enters the Base64-encoded AES key and IV.
2. **Read Backup File**: Loads encrypted data from the `.encrypted` file.
3. **Decrypt Data**: Decrypts the backup using the key and IV.
4. **Restore Original File**: Writes decrypted content to the original file, replacing the ransom note.

### Integrity Check

- A SHA-256 hash of the file is calculated before encryption.
- After decryption, a new SHA-256 hash is computed.
- If the two hashes match, the file has been restored correctly.

---

## Theme Integration

- The GUI uses a custom **Forest Light** theme for a modern aesthetic.
- Theme files are located in the `forest-light/` folder.
- It includes:
  - `forest-light.tcl`
  - PNG assets like `accent-button.png`, `toggle-on.png`, etc.
- The theme is loaded dynamically in `gui.py` using:
  ```python
  root.tk.call('source', 'forest-light/forest-light.tcl')
  ttk.Style().theme_use('forest-light')
  ```

---

## License

This project is licensed under the **MIT License**.  
You are free to use, modify, and distribute this project, provided the license file is included.

---

## Disclaimer

⚠️ This project is strictly for **educational and demonstrative purposes**.  
Do **not** use it maliciously or on any system or data that you do not own or have explicit permission to test on. Misuse of this software may violate laws or ethical guidelines.
