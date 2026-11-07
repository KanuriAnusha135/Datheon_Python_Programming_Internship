
import os
import shutil
from pathlib import Path

# File extension categories
FILE_TYPES = {
    ".pdf": "Documents",
    ".doc": "Documents",
    ".docx": "Documents",
    ".txt": "Documents",
    ".jpg": "Images",
    ".jpeg": "Images",
    ".png": "Images",
    ".gif": "Images",
    ".mp4": "Videos",
    ".mkv": "Videos",
    ".mp3": "Audio",
    ".wav": "Audio",
    ".zip": "Archives",
    ".rar": "Archives",
    ".py": "Code",
    ".html": "Code",
    ".css": "Code"
}


def get_unique_path(destination):
    """Avoid overwriting files with the same name."""
    destination = Path(destination)

    if not destination.exists():
        return destination

    counter = 1

    while True:
        new_name = (
            f"{destination.stem}_{counter}"
            f"{destination.suffix}"
        )
        new_path = destination.with_name(new_name)

        if not new_path.exists():
            return new_path

        counter += 1


def organize_files(folder_path):
    folder = Path(folder_path)

    if not folder.exists() or not folder.is_dir():
        print("Error: Invalid folder path!")
        return

    moved_count = 0
    skipped_count = 0

    for file in folder.iterdir():

        if not file.is_file():
            continue

        category = FILE_TYPES.get(
            file.suffix.lower(),
            "Others"
        )

        destination_folder = folder / category

        try:
            destination_folder.mkdir(
                exist_ok=True
            )

            destination = get_unique_path(
                destination_folder / file.name
            )

            shutil.move(
                str(file),
                str(destination)
            )

            print(f"Moved: {file.name} -> {category}")
            moved_count += 1

        except PermissionError:
            print(f"Permission denied: {file.name}")
            skipped_count += 1

        except OSError as error:
            print(f"Could not move {file.name}: {error}")
            skipped_count += 1

    print("\n===== ORGANIZATION SUMMARY =====")
    print("Files moved:", moved_count)
    print("Files skipped:", skipped_count)
    print("Organization completed!")


if __name__ == "__main__":
    folder = input(
        "Enter folder path to organize: "
    ).strip().strip('"')

    organize_files(folder)