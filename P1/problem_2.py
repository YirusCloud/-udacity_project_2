import os

    if os.path.isfile(path):
        file = path
        if file.endswith('.' + suffix):
            return file
        return ''

    # create a list of file and subdirectories names in the given directory
    listOfFile = os.listdir(path)
    pathFiles = list()

    # Iterate over all the elements
    for element in listOfFile:
        # create path
        fullPath = os.path.join(path, element)
        # If element is a directory then find the files in this directory
        if os.path.isdir(fullPath):
            pathFiles = pathFiles + find_files(suffix, fullPath)
        else:
            if element.endswith('.' + suffix):
                pathFiles.append(fullPath)

    return pathFiles


path = './testdir'

# Get the list of all files in directory tree at given path

# Normal case

# existing file in subdirectorie
print("find_files('c',path): ")
pathFiles = find_files('c', path)

# Print the files
for elem in pathFiles:
    print(elem)

print ("****************")

# existing file in the folder directory and subdirectories
print("find_files('h',path): ")
pathFiles = find_files('h', path)


for elem in pathFiles:
    print(elem)

print ("****************")

# EDGE CASES:

# no existing file
print("find_files('pdf',path): ")
pathFiles = find_files('pdf', path)
print(pathFiles)

print ("****************")

# empty string
print("find_files('',path): ")
pathFiles = find_files('', path)
print(pathFiles)

# the path argument is a file that matches the extension
print("find_files('c','./testdir/t1.c'): ")
pathFiles = find_files('c','./testdir/t1.c')
print(pathFiles)

# the path argument is a file that does not match the extension
print("find_files('h','./testdir/t1.c'): ")
pathFiles = find_files('h','./testdir/t1.c')
print(pathFiles)

