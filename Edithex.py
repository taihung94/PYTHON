import os
import binascii

search_start = b'\x3B\x05'
search_end = b'\x75\x1E'
replace_value = b'\x90\x90\x90\x90\x90\x90\x90\x90'

# Change directory to the path where your files are located
os.chdir('C:/Users/Administrator/Desktop/3EXEsmood')

# Loop through all files in the directory
for filename in os.listdir('.'):
    if filename.endswith('.exe') or filename.endswith('.dll'):
        # Open the file in binary mode
        with open(filename, 'rb') as f:
            # Read the file contents into a bytes object
            file_contents = f.read()
        
        # Initialize a variable to track the current position in the file
        i = 0
        modified = False
        
        # Loop through the file contents searching for the hex pattern
        while i < len(file_contents):
            if file_contents[i:i+2] == search_start:
                j = i + 2
                while j < len(file_contents):
                    if file_contents[j:j+2] == search_end:
                        # Replace the hex pattern with the replacement value
                        file_contents = file_contents[:i] + replace_value + file_contents[j+2:]
                        modified = True
                        break
                    j += 1
                if modified:
                    break
            i += 1
        
        # Write the modified file contents back to the file if any changes were made
        if modified:
            with open(filename, 'wb') as f:
                f.write(file_contents)
