# contains all the functions that installs that executes/install all the downloaded files
import os
import subprocess

import src.logic.utils as utils


def install_fabric(fabric_jar, version) -> None:
    """
    Installs fabric
    :param fabric_jar: The location of the fabric installer
    :param version: The version of the release
    """

    # Enclose the path with spaces in double quotes
    fabric_jar = f'"{fabric_jar}"'

    minecraft_version = utils.get_minecraft_version(version)

    # Install fabric
    command = f'java -jar {fabric_jar} client -mcversion {minecraft_version}'
    try:
        subprocess.run(command, shell=True, check=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")


def install_mod(mod, path, jar) -> None:
    """
    Installs the mod
    :param mod: The name of the mod to install
    :param path: The path to the mod to install
    :param jar: The jar file to install the mod to
    """

    utils.move_contents(path, f"{utils.get_mods_folder()}/{jar}")


def install_mods(mods, temp_folder) -> None:
    """
    Installs the mods
    :param mods: The mods to install
    :param temp_folder: The path to the temporary folder
    """

    for mod in mods:
        path = mods[mod]
        if '.zip' in path:

            jars = utils.extract_zip(path, temp_folder)
            for jar in jars:
                install_mod(jar, temp_folder + jar, jar)
        elif '.jar' in path:
            install_mod(mod, path, path.replace('\\', '/').split('/')[-1])


def install_map(map, path, root) -> None:
    """
    Installs the map
    :param map: The name of the map to install
    :param path: The path to the map to install
    """

    utils.move_contents(path, f"{utils.get_saves_folder()}/{root}")


def install_maps(maps, temp_folder) -> None:
    """
    Installs the maps
    :param maps: The maps to install
    :param temp_folder: The path to the temporary folder
    """
    for map in maps:
        path = maps[map]

        map_folder = utils.extract_zip(path, temp_folder)
        root = map_folder[0].split('/', 1)[0]
        install_map(map, temp_folder + root, root)
