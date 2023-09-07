import os
import shutil
from urllib.parse import urlparse

import requests

import src.logic.utils as utils


# contains all the function that downloads specific content

def download_mod(mod, location, temp_folder) -> str:
    """
    Downloads the mod and returns the path to the zip file
    :param mod: The mod to download
    :param location: The location of the mod to download
    :param temp_folder: The path to the temporary folder
    :return: The path to the downloaded zip file
    """

    response = requests.get(location)

    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Extract the file name from the URL
        parsed_url = urlparse(location)
        file_name = parsed_url.path.split('/')[-1]
        path = f"{temp_folder}{file_name}"
        # Save the file with the extracted name
        with open(path, 'wb') as file:
            file.write(response.content)

        return path

    return None


def download_mods(mods, version, temp_folder) -> dict:
    """
    Downloads the mods for the specified version and returns the path to the zip file
    :param mods: The mods to download
    :param version: The version of the release of the mods to download
    :param temp_folder: The path to the temporary folder
    :return: The path to the downloaded zip file
    """
    all_mods = utils.get_all_mods(version)

    downloaded_mods = {}

    for mod in all_mods:
        if mod in mods:
            m = download_mod(mod, all_mods[mod], temp_folder)
            if m is not None:
                downloaded_mods[mod] = m

    return downloaded_mods


def download_map(map, location, temp_folder) -> str:
    """
    Downloads the map and returns the path to the zip file
    :param map: The map to download
    :param location: The location of the map to download
    :param temp_folder: The path to the temporary folder
    :return: The path to the downloaded zip file
    """

    # TODO: uncomment this after fix
    # Commented out because the maps are not hosted on the internet
    # response = requests.get(location)
    #
    # path = f"{temp_folder}{map}.zip"
    #
    # with open(path, "wb") as file:
    #     file.write(response.content)

    # TODO: remove this after fix
    path = os.path.dirname(os.path.realpath(__file__)).replace("src\\logic", location)
    world = location.split("/")[-1]
    if not os.path.exists(f"{temp_folder}{world}"):
        shutil.copy(utils.get_data_file_path(path), f"{temp_folder}{world}")
    path = f"{temp_folder}{world}"
    # remove till here

    return path


def download_maps(maps, version, temp_folder) -> dict:
    """
    Downloads the maps for the specified version and returns the path to the zip file
    :param maps: The maps to download
    :param version: The version of the release of the maps to download
    :param temp_folder: The path to the temporary folder
    :return: The path to the downloaded zip file
    """
    all_maps = utils.get_all_maps(version)

    downloaded_maps = {}

    for map in all_maps:
        if map in maps:
            downloaded_maps[map] = download_map(map, all_maps[map], temp_folder)

    return downloaded_maps


def download_fabric_installer(version, temp_folder) -> str:
    """
    Downloads the fabric installer from the fabric website
    :param version: The version of the fabric installer to download
    :param temp_folder: The path to the temporary folder
    :return: The path to the downloaded zip file
    """

    response = requests.get(utils.get_fabric_installer(version))

    path = f"{temp_folder}fabric_installer.zip"

    with open(path, "wb") as file:
        file.write(response.content)

    return path
