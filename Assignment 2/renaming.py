# Author - Sandeep Dulam
# submission date : 15-11-2024
# python code for renaming multiple files with a defined prefix and current date
# pre-requisite need to few files with different random names in a directory.


# importing external libraries
import os
import datetime


# function to get list of all files in the given directory
def get_files(directory):
    try:
        files = os.listdir(directory)
        return [file for file in files if os.path.isfile(os.path.join(directory, file))]
    except FileNotFoundError:
        print("Directory not found.")
        return []

# fucntion to rename all files in the directory with a prefix and the current date
def rename_files(directory, prefix="Renamed_"):
    files = get_files(directory)
    if not files:
        print("No files found to rename.")
        return
    
    # current datetime stamp 
    current_date = datetime.datetime.now().strftime("%Y%m%d")
    
    for file in files:
        old_file_path = os.path.join(directory, file)
        new_file_name = f"{prefix}_{current_date}_{file}"
        new_file_path = os.path.join(directory, new_file_name)
        
        try:
            os.rename(old_file_path, new_file_path)
            print(f"Renamed {file} to {new_file_name}")
        except Exception as e:
            print(f"Error renaming file {file}: {e}")

# path for the directory
directory_path = r"D:\Scripting\New folder"
rename_files(directory_path)
