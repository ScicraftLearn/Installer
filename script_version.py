import time

from src.logic.installation import *


def script_version(settings):
    try:
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
        utils.print_progress(error, 0)


if __name__ == '__main__':
    try:
        version = "alpha"
        config = utils.get_config()
        settings_ = config["installer-settings"]["script_version"][version]
        script_version(settings_)
        time.sleep(3)
    except Exception as e:
        print(e)
        time.sleep(15)
