import os
import shutil
from urllib.parse import urlparse

import requests

import src.logic.utils as utils
import src.logic.config as config
import enum
from typing import Optional

class PathURL(enum.Enum):
    empty = 0
    path = 1
    url = 2
"""
This file contains all the function that will be used for downloading content like
    - mods
    - maps
    - fabric installer
"""


def parse_path(location) -> str:
    """
    Parse the given relatice Path to the data for mods/maps, and replace all the separators with the right ones
    :param location: The relative path to the right file
    :return: The correct path, corrected for the relative position of this script
    """
    return os.path.join(config.rel_data_dir, location.replace('/', os.path.sep).replace("\\", os.path.sep))


def is_path(location) -> bool:
    """
    Check if the path given exists
    :param location: The relative path to the location that needs to be searched
    :return: A bool if the path exists
    """
    try:
        path = parse_path(location)
        return os.path.isdir(path) or os.path.exists(path)
    except ValueError:
        return False


def is_url(location) -> bool:
    """
    Check if the given URL can be a real URL
    :param location: The URL that needs to be checked
    :return: A bool is the URL seems legit
    """
    try:
        result = urlparse(location)
        return all([result.scheme, result.netloc])
    except ValueError:
        return False


def is_url_or_path(location) -> PathURL:
    """
    Check if the location is a Path or a URL
    :param location: The location that needs to be checked
    """
    if is_url(location):
        return PathURL.url
    elif is_path(location):
        return PathURL.path
    else:
        return PathURL.empty


def get_file(location, destination) -> Optional[str]:
    """
    Get the file and place it in the destination folder, download or copy it; whatever
    :param location: The location (Path/URL) of the file that needs to be copied
    :param destination: The path to the destination folder
    :return: optional string to the new destination location, if the file has been copied else None
    """
    path_or_url = is_url_or_path(location)
    if path_or_url == PathURL.url:
        print("URL: ", location)
        return download_file(location, destination)
    elif path_or_url == PathURL.path:
        print("Path: ", location)
        return copy_file(location, destination)
    elif path_or_url == PathURL.empty:
        return None
    Warning("This should never happen!")
    return None


def download_file(location, destination) -> Optional[str]:
    """
    Downloads the file and returns the path to the file
    :param location: The location of the file to download
    :param destination: The path to the destination folder
    :return: optional string to the new destination location, if the file has been downloaded else None
    """
    response = requests.get(location)
    # Extract the file name from the URL and make the new file path
    path = os.path.join(destination, urlparse(location).path.split('/')[-1])
    # Check if the request was successful (status code 200)
    if response.status_code == 200:
        # Save the file with the extracted name
        with open(path, 'wb') as file:
            file.write(response.content)
    # maybe it was still ni cache, just check wether it exists
    return path if os.path.exists(path) else None


def copy_file(location, destination) -> Optional[str]:
    """
    Downloads the mod and returns the path to the copied file
    :param location: The location of the file to copy
    :param destination: The path to the destination folder
    :return: optional string to the new destination location, if the file has been copied else None
    """
    path = parse_path(location)
    dest_file = os.path.join(destination, path.split(os.path.sep)[-1])
    if not os.path.exists(dest_file):
        shutil.copy(utils.get_data_file_path(path), dest_file)
    return dest_file if os.path.exists(dest_file) else None


def download_mods(mods, version, temp_folder) -> (bool, dict | str):
    """
    Downloads the mods for the specified version and returns the path to the zip file
    :param mods: The mods to download
    :param version: The version of the release of the mods to download
    :param temp_folder: The path to the temporary folder
    :return: a bool that indicates that the download went successful and a dict or string with the paths or error message.
    """
    try:
        all_mods = utils.get_all_mods(version)

        downloaded_mods = {}

        for mod in all_mods:
            if mod in mods:
                # download the mod
                m = get_file(all_mods[mod], temp_folder)

                # If something went wrong, the mod will not be added to the downloaded mods
                if m is not None:
                    downloaded_mods[mod] = m

        return True, downloaded_mods

    except Exception as error:
        return False, error


def download_maps(maps, version, temp_folder) -> (bool, dict | str):
    """
    Downloads the maps for the specified version and returns the path to the zip file
    :param maps: The maps to download
    :param version: The version of the release of the maps to download
    :param temp_folder: The path to the temporary folder
    :return: a bool that indicates that the download went successful and a dict or string with the paths or error message.
    """

    try:
        all_maps = utils.get_all_maps(version)

        downloaded_maps = {}

        for map in all_maps:
            if map in maps:

                # download the map
                m = get_file(all_maps[map], temp_folder)

                # If something went wrong, the downloaded map cannot be added.
                if m is not None:
                    downloaded_maps[map] = m

        return True, downloaded_maps

    except Exception as error:
        return False, error


def download_fabric_installer(version, temp_folder) -> str | None:
    """
    Downloads the fabric installer from the fabric website
    :param version: The version of the fabric installer to download
    :param temp_folder: The path to the temporary folder
    :return: The path to the downloaded zip file or None if the request failed.
    """

    response = requests.get(utils.get_fabric_installer(version))

    if response.status_code == 200:

        path = f"{temp_folder}fabric_installer.zip"

        with open(path, "wb") as file:
            file.write(response.content)

        return path

    return None
