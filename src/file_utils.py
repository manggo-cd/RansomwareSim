import os

def find_files(directory: str, extensions: tuple = ('.txt', '.docx', '.pdf', '.jpg', '.png')) -> list:
    """
    Recursively find all files in the given directory with the specified extensions.

    Args:
        directory (str): The directory to search within.
        extensions (tuple): A tuple of file extensions to include.

    Returns:
        list: A list of file paths that match the extensions.
    """
    files_list = []
    # Walk through the directory tree
    for root, dirs, files in os.walk(directory):
        for file in files:
            # Check if the file ends with any of the specified extensions (case-insensitive)
            if file.lower().endswith(extensions):
                files_list.append(os.path.join(root, file))
    return files_list
