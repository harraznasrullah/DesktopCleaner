import os
import shutil # Module to move files

# Get the desktop path
# Note: you can change the path to your desktop path
desktop_path = os.path.expanduser("C:/Users/harra/OneDrive/Desktop")

# List all items on the desktop
items = os.listdir(desktop_path)

# Filter only files using a for loop
files = []
for item in items:
    full_path = os.path.join(desktop_path, item)
    if os.path.isfile(full_path):
        files.append(item)

# Print the files
# print("Files on your desktop:")
# for file in files:
#     print(file)

# Define categories based on file extensions
categories = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documents": [".txt", ".pdf", ".doc", ".docx", ".xlsx", ".pptx"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov"],
    "Music": [".mp3", ".wav", ".aac", ".flac"],
    "Games and Apps": [".url", ".lnk"],
    "Others": []  # For files that don't fit in any category
}

# Create a dictionary to store categorized files
categorized_files = {
    category: [] for category in categories
}

# Categorized the files
for file in files:
    file_extension = os.path.splitext(file)[1].lower()
    found = False
    for category, extensions in categories.items():
        if file_extension in extensions:
            categorized_files[category].append(file)
            found = True
            break
    if not found:
        categorized_files["Others"].append(file)

print("\nCategorized files:")
for category, files in categorized_files.items():
    print(f"{category}:")
    for file in files:
        print(f" {file}")

# Create folders for categories and move files
for category, files in categorized_files.items():
    # Create the folder path
    folder_path = os.path.join(desktop_path, category)
    if not os.path.exists(folder_path):  # Check if folder exists
        os.makedirs(folder_path)  # Create the folder if it doesn't exist

    # Move files into the folder
    for file in files:
        source_path = os.path.join(desktop_path, file)  # Original file path
        destination_path = os.path.join(folder_path, file)  # Destination path
        shutil.move(source_path, destination_path)  # Move the file

print("\nFiles have been organized into folders!")
