from src.logic.installation import *


def latest_version():
    run_installer(
        "latest",  # release version
        ["minelabs"],  # mods to install
        ["demo-world"]  # maps to install
    )
