import os
import shutil

# --- Existing path functions (keeping them for robustness) ---
def get_desktop_path_with_onedrive_compatibility():
    """
    Attempts to find the Desktop path, handling potential OneDrive redirection.
    """
    home_dir = os.path.expanduser('~')
    onedrive_desktop_path = os.path.join(home_dir, 'OneDrive', 'Desktop')
    if os.path.exists(onedrive_desktop_path):
        return onedrive_desktop_path
    standard_desktop_path = os.path.join(home_dir, 'Desktop')
    return standard_desktop_path

def get_downloads_path_with_onedrive_compatibility():
    """
    Attempts to find the Downloads path, handling potential OneDrive redirection.
    """
    home_dir = os.path.expanduser('~')
    onedrive_downloads_path = os.path.join(home_dir, 'OneDrive', 'Downloads')
    if os.path.exists(onedrive_downloads_path):
        return onedrive_downloads_path
    standard_downloads_path = os.path.join(home_dir, 'Downloads')
    return standard_downloads_path

# --- Get the actual paths ---
desktop_path = get_desktop_path_with_onedrive_compatibility()
downloads_path = get_downloads_path_with_onedrive_compatibility()

# --- MODIFIED: Added Steam shortcuts and compressed files ---
file_type_destinations = {
    '.jpg': 'Images',
    '.png': 'Images',
    '.jpeg': 'Images',
    '.gif': 'Images',
    '.bmp': 'Images',
    '.tiff': 'Images',
    '.webp': 'Images',
    '.svg': 'Images',
    '.ico': 'Images',

    '.lnk': 'Shortcuts',
    '.url': 'Shortcuts', # General internet shortcuts
    '.website': 'Shortcuts', # Some browser shortcuts

    # Steam game shortcuts (these are typically .url files, but sometimes .url is too generic)
    # Steam often creates .url files on the desktop that link to steam://rungameid/<ID>
    # If you find .url is too broad, you might need a more specific check,
    # but for now, they'll go to 'Shortcuts' with other .url files.
    # Note: True Steam game shortcuts *inside* Steam's own folder often have no extension.

    '.mp4': 'Videos',
    '.mov': 'Videos',
    '.avi': 'Videos',
    '.mkv': 'Videos',
    '.webm': 'Videos',
    '.flv': 'Videos',
    '.wmv': 'Videos',

    '.pdf': 'Documents',
    '.doc': 'Documents',
    '.docx': 'Documents',
    '.txt': 'Documents',
    '.rtf': 'Documents',
    '.odt': 'Documents',
    '.xls': 'Documents',
    '.xlsx': 'Documents',
    '.csv': 'Documents',
    '.ppt': 'Documents',
    '.pptx': 'Documents',
    '.epub': 'Documents',
    '.md': 'Documents',
    '.log': 'Documents',

    # New additions for compressed files
    '.zip': 'Compressed',
    '.rar': 'Compressed',
    '.7z': 'Compressed',
    '.tar': 'Compressed', # Tar archives
    '.gz': 'Compressed',  # Gzip compressed files
    '.bz2': 'Compressed', # Bzip2 compressed files
    '.xz': 'Compressed',  # XZ compressed files
}

main_organized_directory = os.path.join(desktop_path, "Sorted_Files")
os.makedirs(main_organized_directory, exist_ok=True)

def sort_files_in_directory(source_path, organized_base_path, rules_map):
    try:
        items_to_process = os.listdir(source_path)
    except FileNotFoundError:
        print(f"Directory not found: {source_path}")
        return

    for item in items_to_process:
        full_source_item_path = os.path.join(source_path, item)

        if os.path.isdir(full_source_item_path):
            continue

        basename, extension = os.path.splitext(item)
        lowercase_extension = extension.lower()

        if lowercase_extension in rules_map:
            target_subfolder_name = rules_map[lowercase_extension]
            full_destination_folder_path = os.path.join(organized_base_path, target_subfolder_name)

            os.makedirs(full_destination_folder_path, exist_ok=True)

            final_destination_file_path = os.path.join(full_destination_folder_path, item)

            if not os.path.exists(final_destination_file_path):
                try:
                    shutil.move(full_source_item_path, final_destination_file_path)
                except Exception as e:
                    print(f"Error moving {item}: {e}")
            else:
                print(f"Skipped: {item} (already exists in destination)")

print(f"Sorting files from Desktop: {desktop_path}")
sort_files_in_directory(desktop_path, main_organized_directory, file_type_destinations)

print(f"Sorting files from Downloads: {downloads_path}")
sort_files_in_directory(downloads_path, main_organized_directory, file_type_destinations)

print("File sorting complete!")