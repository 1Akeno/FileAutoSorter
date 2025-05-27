import os
import shutil

home_dir = os.path.expanduser('~')

desktop_path = os.path.join(home_dir, "Desktop")
downloads_path = os.path.join(home_dir, "Downloads")

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
}

main_organized_directory = os.path.join(desktop_path, "Sorted_Files")
os.makedirs(main_organized_directory, exist_ok=True)

def sort_files_in_directory(source_path, organized_base_path, rules_map):
    try:
        items_to_process = os.listdir(source_path)
    except FileNotFoundError:
        return

    for item in items_to_process:
        full_source_item_path = os.path.join(source_path, item)

        if os.path.isfile(full_source_item_path):
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
                    except Exception:
                        pass 
            else:
                pass 
        else:
            pass 

sort_files_in_directory(desktop_path, main_organized_directory, file_type_destinations)
sort_files_in_directory(downloads_path, main_organized_directory, file_type_destinations)