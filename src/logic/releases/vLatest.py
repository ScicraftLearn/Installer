import src.logic.utils as utils
from src.logic.installation import *


def latest_version():
    for step in run_installer(
            "latest",  # release version
            ["minelabs"],  # mods to install
            ["demo-world"]  # maps to install
    ):
        text, value = step
        utils.print_progress(text, value)
