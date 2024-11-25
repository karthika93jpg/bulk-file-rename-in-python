import os
import glob

def list_files(directory, extension=None):
    if extension:
        return glob.glob(os.path.join(directory, f"*.{extension}"))
    else:
        return glob.glob(os.path.join(directory, "*"))

def rename_files(files, new_name_pattern):
    for index, file_path in enumerate(files):
        directory, old_file_name = os.path.split(file_path)
        file_extension = old_file_name.split('.')[-1]
        new_file_name = f"{new_name_pattern}_{index + 1}.{file_extension}"
        new_file_path = os.path.join(directory, new_file_name)
        os.rename(file_path, new_file_path)
        print(f"Renamed: {old_file_name} -> {new_file_name}")

def main():
    directory = input("Enter the directory path: ")
    extension = input("Enter file extension to filter (leave blank for all files): ")
        new_name_pattern = input("Enter the new name pattern: ")

    files = list_files(directory, extension)
    rename_files(files, new_name_pattern)
    print("Bulk renaming completed.")

if __name__ == "__main__":
    main()
    