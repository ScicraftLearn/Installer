import src.logic.utils as utils
from src.logic.installation import *


def alpha_version():
    for step in run_installer(
            "alpha",  # release version
            ["minelabs"],  # mods to install
            ["demo-world"]  # maps to install
    ):
        text, value = step
        utils.print_progress(text, value)
