import time

from src.logic.vAlpha import *
from src.logic.vInstallerUI import *
from src.logic.vLatest import *


def create_executable(version):

    versions = {
        "alpha": alpha_version,
        "latest": latest_version,
        "interface": interface_version
    }

    versions[version]()


if __name__ == '__main__':
    v = "alpha"
    try:
        create_executable(v)
        time.sleep(3)
    except Exception as e:
        print(e)
        time.sleep(15)
