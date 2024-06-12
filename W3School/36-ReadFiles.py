### Python File Open ###

# Open a File on the Server.

'''
To open the file, use the built-in open() function.
The open() function returns a file object, which has a read() method for reading the content of the file:
'''

f = open("./demofile.txt", "r")
print(f.read())

f = open("D:\\myfiles\welcome.txt", "r")
print(f.read()) # If the file is located in a different location, you will have to specify the file path.



# Read Only Parts of the File

'''
By default the read() method returns the whole text, but you can also specify how many characters you want to return.
'''

f = open("demofile.txt", "r")
print(f.read(5))