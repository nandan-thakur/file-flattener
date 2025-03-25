import os
import shutil

def copy_files_from_nested_folders(source_folder, destination_folder):
    # Ensure destination folder exists
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)
    
    # Walk through all directories and files in source folder
    for root, dirs, files in os.walk(source_folder):
        for file in files:
            # Get the full path of the source file
            source_file_path = os.path.join(root, file)
            
            # Copy the file to the destination folder
            try:
                shutil.copy2(source_file_path, destination_folder)
                print(f"Copied: {source_file_path} to {destination_folder}")
            except Exception as e:
                print(f"Error copying {source_file_path}: {e}")

# Example usage
if __name__ == "__main__":
    source = "data"
    destination = "photos"
    
    copy_files_from_nested_folders(source, destination)
