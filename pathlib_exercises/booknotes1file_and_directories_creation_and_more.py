import pathlib      # Import the pathlib module to work with file paths
import shutil
path = pathlib.Path("exercise.py") # Create a Path object for the file "exercise.py" in the current directory

home = pathlib.Path.home() # Create a Path object for the home directory

current = pathlib.Path.cwd() / "exercise.py" # Create a Path object for the current working directory

print(path)
print(type(home))
print(current)

#is.absolute() checks whether the path is absolute

#home = pathlib.Path.home()
#home / pathlib.Path("Documents/exercise.py") this would create a path from root to exercise.py

#.resolve() can be used to try to get the absolute path of a file.


#for directory in current.parents:  #showcase .parents ability to list hierarchy
    #print(directory)

#absolute filepaths' top directory can be accessed with .anchor
#.home() can show where we currently are

#take file hello.txt
#path.stem will give you "hello"
#path.suffix will give you ".txt"

#.exists() checks if the file exists and returns True or False
path = pathlib.Path.home() / "hello.txt"
print(path.exists()) # will be false for me since i dont have it

#.is_file() checks if the path is a file; in contrast, .is_dir() checks if the path is a directory. Both return True or False.
path.is_file() # Will return true since hello.txt is a file
path.is_dir() # Will return false since hello.txt is not a directory, but pathlib.Path.home() would be True

#new_dir = pathlib.Path.home() / "new_directory" # Create a new path for a directory called "new_directory" in the home directory
#new_dir.mkdir(exist_ok=True) # Create the directory if it doesn't exist; if it does exist, do nothing

new_dir = pathlib.Path.home() / "python_folder_exercise" / "new_directory" # creates a folder within a folder, which would cause error, unless the line below
new_dir.mkdir(parents=True, exist_ok=True) # in this case exists_ok is optional, but best practice

file_path = new_dir / "file_zero.txt" #create a Path object for the new file in the new directory
file_path.touch() #.touch() actually creates a file from a Path object
folder_path_nested = new_dir / "folder_a" / "folder_b"
folder_path_nested.mkdir(parents=True, exist_ok=True)
extra_folder = new_dir / "folder_c"
extra_folder.mkdir(exist_ok=True)


#for path in new_dir.iterdir():
    #print(path)

#for path in new_dir.glob("folder*"):
    #print(path)


paths = [

    new_dir / "program1.py",
    new_dir / "program2.py",
    new_dir / "folder_a" / "program3.py",
    new_dir / "folder_a" / "folder_b" / "image1.jpg",
    new_dir / "folder_a" / "folder_b" / "image2.jpg",
    new_dir / "folder_c" / "file_one.txt"

]

for path in paths:
    path.touch()

print(list(new_dir.glob("**/*.txt"))) #searches withi current path and subfolders. line below is the same, but more elegant
print(list(new_dir.rglob("*.py")))

source = new_dir / "file_zero.txt"
destination = new_dir / "folder_a" / "file_zero.txt"
source.replace(destination)
print(source.exists()) #false since source is no longer live


source = new_dir / "folder_c"
destination = new_dir / "folder_d"
if not destination.exists():
    source.replace(destination)


#for path in source.iterdir():
#    path.unlink()       #delete the old C folder
#source.rmdir()

#folder_c = source
#shutil.rmtree(folder_c)

#print(source.exists()) #false since source is no longer live
#print(folder_d.exists())


file_path = new_dir / "program1.py"
file_path.unlink() #deletes the file
print(file_path.exists())

file_path = new_dir / "program77.py"
file_path.unlink(missing_ok=True) #since the file is missing, and exception would raise, unless missing ok is provided
print(file_path.exists())

print(destination)


shutil.rmtree(new_dir.parent)