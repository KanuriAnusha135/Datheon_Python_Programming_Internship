
import os
import shutil

# Folder to organize
source_folder = "TestFiles"

# File categories
file_types = {
    "Images": [".jpg", ".jpeg", ".png", ".gif"],
    "Documents": [".pdf", ".txt", ".docx"],
    "Videos": [".mp4", ".mkv", ".avi"],
    "Audio": [".mp3", ".wav"],
    "Archives": [".zip", ".rar"]
}

# Check whether folder exists
if not os.path.exists(source_folder):
    os.makedirs(source_folder)

print("===== AUTOMATED FILE ORGANIZER =====")

# Read all files
for filename in os.listdir(source_folder):

    file_path = os.path.join(source_folder, filename)

    if os.path.isfile(file_path):

        extension = os.path.splitext(filename)[1].lower()

        category = "Others"

        # Find file category
        for folder, extensions in file_types.items():
            if extension in extensions:
                category = folder
                break

        # Create destination folder
        destination_folder = os.path.join(
            source_folder, category
        )

        os.makedirs(destination_folder, exist_ok=True)

        # Move file
        destination_path = os.path.join(
            destination_folder, filename
        )

        shutil.move(file_path, destination_path)

        print(filename, "moved to", category)

print("\nFile organization completed!")