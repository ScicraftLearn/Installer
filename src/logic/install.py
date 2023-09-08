import subprocess

import src.logic.utils as utils

"""
This file contains all the functions for installing content like:
    - mods
    - maps
    - fabric
"""


def install_mod(path, jar) -> None:
    """
    Installs the mod
    :param path: The path to the mod to install
    :param jar: The jar file to install the mod to
    """

    # Moves the jar of the mod from his current positions to the mods folder of Minecraft
    utils.move_contents(path, f"{utils.get_mods_folder()}/{jar}")


def install_mods(mods, temp_folder) -> (bool, str):
    """
    Installs the mods
    :param mods: The mods to install
    :param temp_folder: The path to the temporary folder
    :return (bool, string): bool indicates if the mods are successfully installed, the string shows the installation message.
    """

    try:
        for mod in mods:
            path = mods[mod]

            # If it is a zip extension, then it means that multiple mods are zipped
            if '.zip' in path:
                # We extract all the mods from the zip file
                jars = utils.extract_zip(path, temp_folder)
                # Installing the mods
                for jar in jars:
                    install_mod(temp_folder + jar, jar)
            # A jar extension is a mod, so we install it
            elif '.jar' in path:
                jar = path.replace('\\', '/').split('/')[-1]
                install_mod(path, jar)

        return True, "Mods successfully installed!"

    except Exception as error:
        return False, error


def install_map(path, root) -> None:
    """
    Installs the map
    :param path: The path to the map to install
    :param root: The root folder of the map
    """

    # We only neet to move the root folder, to the Minecraft saves folder,
    # because all the content in it will be automatically moved with it.
    utils.move_contents(path, f"{utils.get_saves_folder()}/{root}")


def install_maps(maps, temp_folder) -> (bool, str):
    """
    Installs the maps
    :param maps: The maps to install
    :param temp_folder: The path to the temporary folder
    :return (bool, string): bool indicates if the maps are successfully installed, the string shows the installation message.
    """
    try:
        for map in maps:
            path = maps[map]

            # Extracting the map from the zip file/
            map_folder = utils.extract_zip(path, temp_folder)

            # Retrieving the root folder
            root = map_folder[0].split('/', 1)[0]

            # Installing the map
            install_map(temp_folder + root, root)

        return True, "Maps successfully installed!"

    except Exception as error:
        return False, error


def install_fabric(fabric_jar, version) -> (bool, str):
    """
    Installs fabric
    :param fabric_jar: The location of the fabric installer
    :param version: The version of the release
    :return (bool, string): bool indicates if fabric is successfully installed, the string shows the installation message.
    """

    # Enclose the path with spaces in double quotes
    fabric_jar = f'"{fabric_jar}"'

    # Get the minecraft version for the release version
    minecraft_version = utils.get_minecraft_version(version)

    # Install fabric
    command = f'java -jar {fabric_jar} client -mcversion {minecraft_version}'
    try:
        subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        return True, "Fabric successfully installed!"
    except subprocess.CalledProcessError as error:
        return False, error
