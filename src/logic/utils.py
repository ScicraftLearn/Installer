import json
import os
import shutil
import sys
import zipfile


def get_data_file_path(filename):
    """
    Returns the path to the bundled data file, needed for PyInstaller.
    :param filename: The name of the file
    :return: The path to the file
    """
    if getattr(sys, 'frozen', False):
        # Running as a PyInstaller executable.
        data_path = sys._MEIPASS
    else:
        # Running as a regular Python script.
        data_path = os.getcwd()

    return os.path.join(data_path, filename)


def get_config() -> dict:
    """
    Returns the config file as a dictionary
    :return: The config file as a dictionary
    """
    return json.load(open(get_data_file_path("resources/config.json")))


def get_dialogs() -> dict:
    """
    Returns the dialogs file as a dictionary
    :return: The dialogs file as a dictionary
    """
    return json.load(open(get_data_file_path("resources/dialog.json")))


def get_dialog_language() -> str:
    """
    Returns the language for the dialogs based on the system language
    :return: The language for the dialogs based on the system language
    """

    import locale
    system_language = locale.getdefaultlocale()[0].split("_")[0]
    if system_language == "nl":
        return "dutch"
    return "english"


def get_logo(extension) -> str:
    """
    Returns the logo file as a string
    :param extension: The extension of the logo file
    :return: The logo file as a string
    """
    return get_data_file_path(f"resources/images/minelabs-logo.{extension}")


def get_mods_folder() -> str:
    """
    Returns the location of the mods folder
    :return: The location of the mods folder
    """

    # check if mods folder exists
    if not os.path.exists(os.path.join(os.getenv("APPDATA"), ".minecraft", "mods")):
        # create mods folder
        os.makedirs(os.path.join(os.getenv("APPDATA"), ".minecraft", "mods"))

    return os.path.join(os.getenv("APPDATA"), ".minecraft", "mods")


def get_saves_folder() -> str:
    """
    Returns the location of the saves folder
    :return: The location of the saves folder
    """
    return os.path.join(os.getenv("APPDATA"), ".minecraft", "saves")


def extract_zip(zip_file, temp_folder) -> list[str]:
    """
    Extracts the zip file to the temp folder
    """

    # Extract the zip file
    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        zip_ref.extractall(temp_folder)
        extracted_files = zip_ref.namelist()

    return extracted_files


def move_contents(source, destination) -> None:
    """
    Moves the contents of the source folder to the destination folder
    :param source: the source folder of the contents
    :param destination: the destination folder of the contents
    """
    if not os.path.exists(destination):
        shutil.move(source, destination)


def get_fabric_installer(version) -> str:
    """
    Returns the location of the fabric installer
    :param version: The version of the release
    :return: The location of the fabric installer
    """

    config = get_config()

    return config["fabric-installer"][version]


def get_all_mods(version) -> dict:
    """
    Returns all the mods for the specified version
    :param version: The version of the release
    :return: All the mods for the specified version
    """

    config = get_config()

    all_maps = {}

    maps = config["mods"]
    for _map in maps:
        if version in maps[_map]:
            all_maps[_map] = maps[_map][version]

    return all_maps


def get_mod_extension(mod) -> str:
    """
    Returns the extension of the mod
    :param mod: The mod to get the extension of
    :return: The extension of the mod
    """
    config = get_config()
    return config["mod-extensions"][mod]


def get_all_maps(version) -> dict:
    """
    Returns all the maps for the specified version
    :param version: The version of the release
    :return: All the maps for the specified version
    """
    config = get_config()

    all_maps = {}

    maps = config["maps"]
    for _map in maps:
        if version in maps[_map]:
            all_maps[_map] = maps[_map][version]

    return all_maps


def get_minecraft_version(version) -> str:
    """
    Returns the Minecraft version for the specified release
    :param version: The version of the release
    :return: The Minecraft version for the specified release
    """
    config = get_config()

    return config["minecraft-versions"][version]


def get_tree_structure_config() -> dict:
    """
    Returns the tree structure config file as a dictionary
    :return: The tree structure config file as a dictionary
    """
    config = get_config()
    versions = config["versions"]

    structure = {}

    for version in versions:
        structure[version] = {}
        structure[version]["mods"] = list(get_all_mods(version).keys())
        structure[version]["maps"] = list(get_all_maps(version).keys())
        structure[version]["fabric-installer"] = []

    return structure


def create_temporary_folder() -> str:
    """
    Creates a temporary folder in the same directory as the installer
    :return: The path to the temporary folder
    """

    # Get the temp folder location
    temp_folder = os.path.dirname(os.path.realpath(__file__)) + "\\temp\\"

    # Check if the temp folder exists and create it if it doesn't
    if not os.path.exists(temp_folder):
        os.makedirs(temp_folder)

    return temp_folder


def delete_temporary_folder(temp_folder) -> None:
    """
    Deletes the temporary folder
    :param temp_folder: The path to the temporary folder
    """

    # Delete the temp folder
    shutil.rmtree(temp_folder)


def print_progress(text, value):
    progress_length = 20
    filled_length = int(progress_length * value / 100)

    progress_bar = "[" + "=" * filled_length + " " * (progress_length - filled_length) + "]"
    text = ('{: <35}'.format(text))
    formatted_text = f"{text} {progress_bar}  {value}%"

    print(formatted_text)