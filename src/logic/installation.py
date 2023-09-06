import src.logic.download as downloader
import src.logic.install as installer
import src.logic.utils as utils


def run_installer(version, selected_mods, selected_maps):
    print(f"Installing {version} version...")

    # Creates a temporary folder and returns the path
    temp_folder = utils.create_temporary_folder()

    # Downloads the mods and returns the path to the zip file
    mods = downloader.download_mods(
        selected_mods,  # mods to download
        version,                         # version of the mods to download
        temp_folder
    )

    # Downloads the maps and returns the path to the zip file
    maps = downloader.download_maps(
        selected_maps,  # mods to download
        version,  # version of the mods to download
        temp_folder
    )

    # Downloads the fabric installer and returns the path to the zip file
    fabric_installer = downloader.download_fabric_installer(version, temp_folder)

    # installs the mods
    installer.install_mods(mods, temp_folder)

    # installs the maps
    installer.install_maps(maps, temp_folder)

    # installs fabric
    installer.install_fabric(fabric_installer, version)

    # deletes the temporary folder
    utils.delete_temporary_folder(temp_folder)

    print(f"Done installing {version} version of Minelabs!")
