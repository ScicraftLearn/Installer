import src.logic.download as downloader
import src.logic.install as installer
import src.logic.utils as utils


def run_installer(version, selected_mods, selected_maps, install_fabric=True):
    """
    Performs the minelabs installation
    :param version: the minelabs release version
    :param selected_mods: the mods that must be installed
    :param selected_maps: the maps that must be installed
    :param install_fabric: indicates that fabric needs to be installed or not
    :return: return True if the installation went successful otherwise False
    """

    yield f"Start installing {version} version...", 0

    # Calculates the number of steps based on of mods, maps or fabric need to be installed
    number_of_steps = (2 if len(selected_mods) > 0 else 0) + (2 if len(selected_maps) > 0 else 0) + (2 if install_fabric else 0)

    # The installed content
    installed_content = []

    # If no steps, nothing is selected and the installation is done
    if number_of_steps == 0:
        yield "Nothing to install", 100
        return True

    steps_completed = 0

    # Creates a temporary folder and returns the path
    temp_folder = utils.create_temporary_folder()

    # Check if there are mods needed to be installed
    if len(selected_mods) > 0:

        yield "Downloading mods...", round(steps_completed / number_of_steps * 100)

        # Downloads the mods and returns the path to the zip file
        successful, mods = downloader.download_mods(
            selected_mods,  # mods to download
            version,  # version of the mods to download
            temp_folder
        )

        # If mods are successfully downloaded, install them.
        if successful:

            steps_completed += 1

            yield "Mods successfully downloaded", round(steps_completed / number_of_steps * 100)
            yield "Installing mods...", round(steps_completed / number_of_steps * 100)

            # installs the mods
            successful, message = installer.install_mods(mods, temp_folder, installed_content)

            if successful:
                steps_completed += 1
                yield message, round(steps_completed / number_of_steps * 100)

            # if the installation fails, send the error and stop the installation
            else:
                # deletes the installed content
                utils.delete_files(installed_content)
                utils.delete_temporary_folder(temp_folder)
                raise Exception(message)

        # Else yield the error message and stop the installation
        else:
            utils.delete_files(installed_content)
            utils.delete_temporary_folder(temp_folder)
            raise Exception(mods)

    if len(selected_maps) > 0:

        yield "Downloading maps...", round(steps_completed / number_of_steps * 100)

        # Downloads the maps and returns the path to the zip file
        successful, maps = downloader.download_maps(
            selected_maps,  # mods to download
            version,  # version of the mods to download
            temp_folder
        )

        if successful:
            steps_completed += 1

            yield "Maps successfully downloaded", round(steps_completed / number_of_steps * 100)
            yield "Installing maps...", round(steps_completed / number_of_steps * 100)

            # installs the maps
            successful, message = installer.install_maps(maps, temp_folder, installed_content)

            if successful:
                steps_completed += 1
                yield message, round(steps_completed / number_of_steps * 100)

            # if the installation fails, send the error and stop the installation
            else:
                # deletes the installed content
                utils.delete_files(installed_content)
                utils.delete_temporary_folder(temp_folder)
                raise Exception(message)

        # Else yield the error message and stop the installation
        else:
            utils.delete_files(installed_content)
            utils.delete_temporary_folder(temp_folder)
            raise Exception(maps)

    if install_fabric:

        yield "Downloading fabric...", round(steps_completed / number_of_steps * 100)

        # Downloads the fabric installer and returns the path to the zip file
        fabric_installer = downloader.download_fabric_installer(version, temp_folder)

        if fabric_installer is None:
            # deletes the installed content
            utils.delete_files(installed_content)
            utils.delete_temporary_folder(temp_folder)
            raise Exception("Failed to download the fabric installer.")

        steps_completed += 1

        yield "Installing fabric...", round(steps_completed / number_of_steps * 100)

        # installs fabric
        successful, message = installer.install_fabric(fabric_installer, version)

        if successful:
            steps_completed += 1
            yield message, round(steps_completed / number_of_steps * 100)

        else:
            from src.logic.fabric import install_client
            successful = install_client("0.14.24", utils.get_minecraft_version(version))
            message = "Success with Python"

        if successful:
            steps_completed += 1
            yield message, round(steps_completed / number_of_steps * 100)
        else:
            # deletes the installed content
            utils.delete_files(installed_content)
            utils.delete_temporary_folder(temp_folder)
            raise Exception(message)

    # deletes the temporary folder
    utils.delete_temporary_folder(temp_folder)

    yield "Installation complete!", round(steps_completed / number_of_steps * 100)

    return True
