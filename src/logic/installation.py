import src.logic.download as downloader
import src.logic.install as installer
import src.logic.utils as utils


def run_installer(version, selected_mods, selected_maps, install_fabric=True):
    yield f"Start installing {version} version...", 0

    number_of_steps = (2 if len(selected_mods) > 0 else 0) + (2 if len(selected_maps) > 0 else 0) + (2 if install_fabric else 0)

    if number_of_steps == 0:
        yield "Nothing to install", 100
        return

    steps_completed = 0
    # Creates a temporary folder and returns the path
    temp_folder = utils.create_temporary_folder()

    if len(selected_mods) > 0:
        yield "Downloading mods...", round(steps_completed / number_of_steps * 100)
        # Downloads the mods and returns the path to the zip file
        mods = downloader.download_mods(
            selected_mods,  # mods to download
            version,  # version of the mods to download
            temp_folder
        )
        steps_completed += 1

        yield "Installing mods...", round(steps_completed / number_of_steps * 100)
        # installs the mods
        installer.install_mods(mods, temp_folder)
        steps_completed += 1

    if len(selected_maps) > 0:
        yield "Downloading maps...", round(steps_completed / number_of_steps * 100)
        # Downloads the maps and returns the path to the zip file
        maps = downloader.download_maps(
            selected_maps,  # mods to download
            version,  # version of the mods to download
            temp_folder
        )
        steps_completed += 1

        yield "Installing maps...", round(steps_completed / number_of_steps * 100)
        # installs the maps
        installer.install_maps(maps, temp_folder)
        steps_completed += 1

    if install_fabric:
        yield "Downloading fabric...", round(steps_completed / number_of_steps * 100)
        # Downloads the fabric installer and returns the path to the zip file
        fabric_installer = downloader.download_fabric_installer(version, temp_folder)
        steps_completed += 1

        yield "Installing fabric...", round(steps_completed / number_of_steps * 100)
        # installs fabric
        installer.install_fabric(fabric_installer, version)
        steps_completed += 1

    # deletes the temporary folder
    utils.delete_temporary_folder(temp_folder)

    yield "Installation complete!", round(steps_completed / number_of_steps * 100)
