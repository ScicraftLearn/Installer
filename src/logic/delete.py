import src.logic.utils as utils

"""
This file contains all the functions for deleting the mods:
"""


def delete_mod(mod_name) -> bool:
    """
    Deletes all mods in the mod folder, that contains the mod name in the name.
    :param mod_name: The name of the mod to delete
    :return bool: Indicates if the mods are successfully deleted
    """

    try:
        folder = utils.get_mods_folder()
        mods = utils.get_files_in_folder(folder)

        to_delete = []

        for mod in mods:
            if mod_name in mod:
                to_delete.append(mod)

        utils.delete_files(to_delete)
        return True

    except Exception as error:
        return False