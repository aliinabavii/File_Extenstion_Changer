import os

def change_file_extension(file_path, new_extension):
    # Split the file path into the base name and the original extension
    base_name, ext = os.path.splitext(file_path)
    
    # Check if the path represents a file
    if os.path.isfile(file_path):
        new_file_path = base_name + new_extension
        os.rename(file_path, new_file_path)
        print(f"File extension changed to '{new_extension}' successfully: {new_file_path}")

    # Check if the path represents a directory
    elif os.path.isdir(file_path):
        for root, _, files in os.walk(file_path):
            for file in files:
                file_path = os.path.join(root, file)
                base_name, ext = os.path.splitext(file_path)
                new_file_path = base_name + new_extension
                os.rename(file_path, new_file_path)
                print(f"File extension changed to '{new_extension}' successfully: {new_file_path}")

    else:
        print("Invalid path provided.")

if __name__ == "__main__":
    while True:
        folder_path = input("Drag and drop a folder here (or type 'q' to quit): ").strip('"')

        if folder_path.lower() == 'q':
            break

        new_extension = input("Enter the new extension (include the dot, e.g., '.py'): ").strip()

        change_file_extension(folder_path, new_extension)