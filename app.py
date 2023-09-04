from src.download import *
from src.installer import *

if __name__ == '__main__':

    maps_folder = 'maps/DEMO_WORLD.zip'

    temp_folder = create_temporary_folder()
    mods_zip = download_alpha_release_mods(temp_folder)
    fabric_jar = download_recent_version_fabric(temp_folder)
    install_fabric(fabric_jar, "1.19.2")
    mods = extract_zip(mods_zip, temp_folder)
    maps = extract_zip(maps_folder, temp_folder)
    move_mods(mods, temp_folder)
    move_maps(maps, temp_folder)
    delete_temporary_folder(temp_folder)

