# contains all the functions that installs that executes/install all the downloaded files
import os
import shutil
import zipfile


def create_temporary_folder() -> str:
    """
    Creates a temporary folder in the same directory as the installer
    """

    # Get the temp folder location
    temp_folder = os.path.dirname(os.path.realpath(__file__)) + "\\temp\\"

    # Check if the temp folder exists and create it if it doesn't
    if not os.path.exists(temp_folder):
        os.makedirs(temp_folder)

    print("Created temporary folder")

    return temp_folder


def delete_temporary_folder(temp_folder) -> None:
    """
    Deletes the temporary folder
    """

    # Delete the temp folder
    shutil.rmtree(temp_folder)

    print("Deleted temporary folder")


def install_fabric(fabric_jar, minecraft_version) -> None:
    """
    Installs fabric
    """

    # Enclose the path with spaces in double quotes
    fabric_jar = f'"{fabric_jar}"'

    # Install fabric
    command = f'java -jar {fabric_jar} client -mcversion {minecraft_version}'
    os.system(command)

    print("Installed fabric")


def extract_zip(zip_file, temp_folder) -> list[str]:
    """
    Extracts the zip file to the temp folder
    """

    # List of extracted files
    extracted_files = []

    # Extract the zip file
    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        zip_ref.extractall(temp_folder)
        extracted_files = zip_ref.namelist()

    print("Extracted zip file")

    return extracted_files


def move_files(files, temp_folder, target_folder):
    """
    Moves a list of files from the temp_folder to the target_folder.
    If the target folder does not exist, it will be created.
    """
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)

    for file in files:
        source = os.path.join(temp_folder, file)
        destination = os.path.join(target_folder, file)
        shutil.move(source, destination)


def move_mods(mods, temp_folder):
    """
    Moves the mods to the Minecraft mods folder.
    """
    minecraft_mods_folder = os.path.join(os.getenv("APPDATA"), ".minecraft", "mods")
    move_files(mods, temp_folder, minecraft_mods_folder)

    print("Moved mods")


def move_maps(maps, temp_folder):
    """
    Moves the maps to the Minecraft saves folder.
    """

    maps = set([map_.split('/', 1)[0] for map_ in maps])

    minecraft_saves_folder = os.path.join(os.getenv("APPDATA"), ".minecraft", "saves")
    move_files(maps, temp_folder, minecraft_saves_folder)

    print("Moved maps")
