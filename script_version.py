import time

import src.logic.delete as delete
from src.logic.installation import *


def script_version(settings):
    try:

        # deleting mods that exists
        all_mods = list(utils.get_all_mods(settings["version"]).keys())
        all_mods.append("fabric")
        for mod in all_mods:
            delete.delete_mod(mod)

        for step in run_installer(
                settings["version"],  # release version
                settings["mods"],  # mods to install
                settings["maps"],  # maps to install
                settings["fabric"],  # install fabric or not
        ):
            text, value = step
            utils.print_progress(text, value)
    except Exception as error:
        # If something went wrong print the error message and set installation progress to zero
        print(error)


if __name__ == '__main__':
    try:
        version = "latest"
        config = utils.get_config()
        settings_ = config["installer-settings"]["script_version"][version]
        script_version(settings_)
        time.sleep(3)
    except Exception as e:
        print(e)
        time.sleep(15)
