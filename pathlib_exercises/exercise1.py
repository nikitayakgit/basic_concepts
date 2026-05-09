import pathlib
import shutil

new_dir = pathlib.Path.home() / "my_folder_exercise"
new_dir.mkdir(parents=True, exist_ok=True)

files_to_create = [

    new_dir / "file1.txt",
    new_dir / "file2.txt",
    new_dir / "image.png"

]

for path in files_to_create:
    path.touch()

images_directory = new_dir / "images"
images_directory.mkdir(parents=True, exist_ok=True)

source_image = new_dir / "image.png"
destination_folder = new_dir / "images" / "image.png"
source_image.replace(destination_folder)

file_to_delete = new_dir / "file1.txt"
file_to_delete.unlink()

shutil.rmtree(new_dir)