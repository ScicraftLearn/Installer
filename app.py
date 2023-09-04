import sys
import os
from src.download import *
from src.installer import *


def get_data_file_path(filename):
    # Determine the path to the bundled data file
    if getattr(sys, 'frozen', False):
        # Running as a PyInstaller executable
        data_path = sys._MEIPASS  # This points to the extraction directory
    else:
        # Running as a regular Python script
        data_path = os.path.dirname(os.path.abspath(__file__))

    # Construct the full path to the data file
    return os.path.join(data_path, filename)


def alpha_version():
    maps_file = 'DEMO_WORLD_alpha.zip'
    maps_folder = get_data_file_path(f'maps/{maps_file}')
    temp_folder = create_temporary_folder()
    mods_zip = download_alpha_release_mods(temp_folder)
    fabric_jar = download_recent_version_fabric(temp_folder)
    install_fabric(fabric_jar, "1.19.2")
    mods = extract_zip(mods_zip, temp_folder)
    maps = extract_zip(maps_folder, temp_folder)
    move_mods(mods, temp_folder)
    move_maps(maps, temp_folder)
    delete_temporary_folder(temp_folder)


def recent_version():
    maps_file = 'DEMO_WORLD_recent.zip'
    maps_folder = get_data_file_path(f'maps/{maps_file}')
    temp_folder = create_temporary_folder()
    mods_zip = download_recent_version_mods(temp_folder)
    fabric_jar = download_recent_version_fabric(temp_folder)
    install_fabric(fabric_jar, "1.19.4")
    mods = extract_zip(mods_zip, temp_folder)
    maps = extract_zip(maps_folder, temp_folder)
    move_mods(mods, temp_folder)
    move_maps(maps, temp_folder)
    delete_temporary_folder(temp_folder)


if __name__ == '__main__':
    alpha_version()
    # recent_version()
