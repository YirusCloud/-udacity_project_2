import os

def find_files(suffix, path):
    for file_name in os.listdir('Downloads' + path):
        if os.path.join('Downloads' + path, file_name).endswith(suffix):
            return True
         
    return None  

print(find_files('.c', '/testdir/subdir4'))
print(find_files('.c', '/testdir'))
print(find_files('.gitkeep', '/testdir/subdir4')) 

