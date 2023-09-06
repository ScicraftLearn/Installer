from src.logic.installation import *


def alpha_version():
    run_installer(
        "alpha",  # release version
        ["minelabs"],  # mods to install
        ["demo-world"]  # maps to install
    )
