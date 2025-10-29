import os

# Enter the path
directory_path = "./../../"

try:
    # All Files list in the directory
    entries = os.listdir(directory_path)

    print(f"Contents of directory '{directory_path}':")
    for entry in entries:
        print(entry)

        #errors

except FileNotFoundError:
    print(f"The directory '{directory_path}' was not found.")
except PermissionError:
    print(f"Permission denied to access '{directory_path}'.")
except Exception as e:
    print(f"An error occurred: {e}") 
