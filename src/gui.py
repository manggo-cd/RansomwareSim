import tkinter as tk
from tkinter import ttk, filedialog, messagebox, simpledialog
import base64
import os
from src.encryption import encrypt_file, decrypt_file
from src.file_utils import find_files
from src.hash_utils import compute_sha256
from Crypto.Random import get_random_bytes

class RansomwareGUI:
    def __init__(self, master):
        self.master = master
        master.title("Ransomware Simulation Tool")
        master.geometry("600x500")
        
        # Label to display selected folder
        self.folder_label = ttk.Label(master, text="No folder selected")
        self.folder_label.pack(pady=10)
        
        # Button to select folder
        self.select_button = ttk.Button(master, text="Select Folder", command=self.select_folder)
        self.select_button.pack(pady=5)
        
        # Text widget to log actions and status messages
        self.log_text = tk.Text(master, height=12, width=70)
        self.log_text.pack(pady=10)
        
        # Buttons for encryption, decryption, and preview
        self.encrypt_button = ttk.Button(master, text="Encrypt Files", command=self.encrypt_files)
        self.encrypt_button.pack(pady=5)
        
        self.decrypt_button = ttk.Button(master, text="Decrypt Files", command=self.decrypt_files)
        self.decrypt_button.pack(pady=5)
        
        self.preview_button = ttk.Button(master, text="Preview File", command=self.preview_file)
        self.preview_button.pack(pady=5)
        
        # Internal storage for folder path, key, and IV
        self.selected_folder = None
        self.key = None
        self.iv = None

    def log(self, message):
        """Log a message to the text widget."""
        self.log_text.insert(tk.END, message + "\n")
        self.log_text.see(tk.END)

    def select_folder(self):
        """Let the user choose a folder containing files to process."""
        folder = filedialog.askdirectory()
        if folder:
            self.selected_folder = folder
            self.folder_label.config(text=f"Selected Folder: {folder}")
            self.log("Folder selected.")

    def encrypt_files(self):
        """Encrypt files in the selected folder and replace their content with a ransom note."""
        if not self.selected_folder:
            messagebox.showerror("Error", "No folder selected!")
            return
        
        # Generate a random AES key and IV
        self.key = get_random_bytes(16)
        self.iv = get_random_bytes(16)
        key_b64 = base64.b64encode(self.key).decode()
        iv_b64 = base64.b64encode(self.iv).decode()
        self.log(f"Encryption key (Base64): {key_b64}")
        self.log(f"IV (Base64): {iv_b64}")

        # Find all target files in the folder
        files = find_files(self.selected_folder)
        for file in files:
            original_hash = compute_sha256(file)
            self.log(f"Original hash for {file}: {original_hash}")
            try:
                encrypt_file(file, self.key, self.iv)
                self.log(f"Encrypted: {file}")
            except Exception as e:
                self.log(f"Error encrypting {file}: {e}")
        self.log("*** Encryption complete. Keep your key and IV safe! ***")

    def decrypt_files(self):
        """Decrypt files in the selected folder."""
        if not self.selected_folder:
            messagebox.showerror("Error", "No folder selected!")
            return
        
        # Prompt user for key and IV (Base64 encoded)
        key_b64 = simpledialog.askstring("Input", "Enter the encryption key (Base64):", parent=self.master)
        iv_b64 = simpledialog.askstring("Input", "Enter the IV (Base64):", parent=self.master)
        try:
            key = base64.b64decode(key_b64)
            iv = base64.b64decode(iv_b64)
        except Exception as e:
            messagebox.showerror("Error", f"Invalid key/IV format: {e}")
            return

        files = find_files(self.selected_folder)
        for file in files:
            try:
                decrypt_file(file, key, iv)
                self.log(f"Decrypted: {file}")
                new_hash = compute_sha256(file)
                self.log(f"New hash for {file}: {new_hash}")
            except Exception as e:
                self.log(f"Error decrypting {file}: {e}")
        self.log("*** Decryption complete. ***")
    
    def preview_file(self):
        """Simulate opening an encrypted file by displaying its content in a popup."""
        if not self.selected_folder:
            messagebox.showerror("Error", "No folder selected!")
            return

        # Let the user select a file from the folder
        file_path = filedialog.askopenfilename(initialdir=self.selected_folder)
        if not file_path:
            return

        try:
            # Open the file and read a portion of it (or all if small)
            with open(file_path, 'r') as file:
                content = file.read(1000)  # Read first 1000 characters
        except Exception as e:
            content = f"Error reading file: {e}"

        # Display the file content in a popup
        messagebox.showinfo("File Preview", content)

# ---------------------- LOAD THE CUSTOM THEME AND RUN THE GUI ----------------------
if __name__ == "__main__":
    # Create the main Tkinter window
    root = tk.Tk()

    # Determine the absolute path of the project root (one level up from src)
    script_dir = os.path.dirname(os.path.abspath(__file__))  # .../RansomwareSim/src
    project_root = os.path.join(script_dir, '..')            # .../RansomwareSim

    # Path to the forest-light folder in the project root
    theme_dir = os.path.join(project_root, 'forest-light')
    # Full path to the forest-light.tcl file
    tcl_file = os.path.join(theme_dir, 'forest-light.tcl')

    # Load the custom Forest Light theme
    root.tk.call('source', tcl_file)
    # Apply the theme to ttk widgets (assumes the theme is named 'forest-light')
    ttk.Style().theme_use('forest-light')

    # Create and run the GUI
    app = RansomwareGUI(root)
    root.mainloop()