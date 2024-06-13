### Python Delete File ###

# Delete a File

'''
To delete a file, you must import the OS module, and run its os.remove() function.
'''

import os
os.remove("demofile.txt") # Remove the file "demofile.txt".



# Check if File exist

'''
To avoid getting an error, you might want to check if the file exists before you try to delete it
'''

import os
if os.path.exists("demofile.txt"):
    os.remove("demofile.txt")
else:
    print("The file does not exist") # Check if file exists, then delete it.



# Delete Folder

'''
To delete an entire folder, use the os.rmdir() method
'''

import os
os.rmdir("myfolder") # Remove the folder "myfolder".



# Note: You can only remove empty folders.