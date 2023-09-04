import requests


# contains all the function that downloads specific content


def download_recent_version_mods(temp_folder) -> str:
    """
    Downloads the latest version of the mods from the minelabs wesbite
    """

    # Download the mods
    location = "https://minelabs.be/minelabs-content/mods.zip"
    response = requests.get(location)

    with open(temp_folder + "recent_mods.zip", "wb") as file:
        file.write(response.content)

    print("Downloaded mods")

    return temp_folder + "recent_mods.zip"


def download_alpha_release_mods(temp_folder) -> str:
    """
    Downloads the alpha version of the mods from the GitHub repository
    """

    # Download the mods
    location = "https://github.com/ScicraftLearn/Minelabs/releases/download/alpha-1.0.0/files.zip"
    response = requests.get(location)

    with open(temp_folder + "alpha_mods.zip", "wb") as file:
        file.write(response.content)

    print("Downloaded mods")

    return temp_folder + "alpha_mods.zip"


def download_recent_version_fabric(temp_folder) -> str:
    """
    Downloads the latest version of fabric from the minelabs wesbite
    :return:
    """

    # Download the fabric installer
    location = "https://maven.fabricmc.net/net/fabricmc/fabric-installer/0.11.2/fabric-installer-0.11.2.jar"
    response = requests.get(location)

    with open(temp_folder + "fabric.jar", "wb") as file:
        file.write(response.content)

    print("Downloaded fabric")

    return temp_folder + "fabric.jar"
