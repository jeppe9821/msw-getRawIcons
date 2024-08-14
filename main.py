import os;
import shutil;

def find_png_files(root_dir, filename="info.iconRaw") -> list:
    matching_files = []
    
    # Traverse the directory tree
    for dirpath, _, filenames in os.walk(root_dir):
        for file in filenames:
            if filename in file:
                # If a matching file is found, add the full path to the list
                full_path = os.path.join(dirpath, file)
                matching_files.append(full_path)
                print("Found raw icon at: ", full_path)

                split = dirpath.split("\\")
                itemId = split[len(split) - 1]

                shutil.copy(full_path, "C:/Projekt/Maplestory/Sprites/output/" + itemId + ".png")
    
    return matching_files

def run() -> None:
    
    matching_files:list = find_png_files("C:/Projekt/Maplestory/Sprites/Character.wz")

    pass

run()