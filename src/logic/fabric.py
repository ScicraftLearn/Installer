import requests
import os
import shutil
import json
import hashlib
import base64
from datetime import datetime
import src.logic.config as config
from typing import List, Dict

def install_client(loader: str, game: str):
    loader_url = config.default_meta_server + config.loader_version_meta
    game_url = config.default_meta_server + config.game_version_meta

    loader_response = requests.get(loader_url)
    if loader_response.status_code == 200:
        loader_json = loader_response.json()
    else:
        print("no response from server")
        return
    loader_versions = [loader_i['version'] for loader_i in loader_json]
    loader_stable = [loader_i['stable'] for loader_i in loader_json]
    if loader not in loader_versions:
        print(f"Loader version {loader} not in the list of versions")
        return
    if not loader_stable[loader_versions.index(loader)]:
        print(f"Loader version {loader} is unstable.")

    game_response = requests.get(game_url)
    if game_response.status_code == 200:
        game_json = game_response.json()
    else:
        print("no response from server")
        return
    game_versions = [game_i["version"] for game_i in game_json]
    game_stable = [game_i["stable"] for game_i in game_json]
    if loader not in loader_versions:
        print(f"Game version {game} not in the list of versions")
        return
    if not game_stable[game_versions.index(game)]:
        print(f"Game version {game} is unstable.")

    loader_stable_latest = loader_versions[loader_stable.index(True)]
    game_stable_latest = game_versions[game_stable.index(True)]

    print(f"Lastest stable loader/game is {loader_stable_latest} - {game_stable_latest}.")

    if not os.path.exists(config.mcdir):
        # minecraft not yet installed
        os.makedirs(config.mcdir)

    if not os.path.exists(config.versionsdir):
        # minecraft not yet installed
        os.makedirs(config.versionsdir)

    #profile_name = f"{config.loader_name}-{loader}-{game}"
    profile_name = "Minelabs"
    profile_dir = os.path.join(config.versionsdir, profile_name)

    if os.path.exists(profile_dir):
        print(f"The dir {profile_dir} was already there")
        shutil.rmtree(profile_dir)
    # make the folder for the fabric profile in the launcher
    os.makedirs(profile_dir)

    profile_jar = os.path.join(profile_dir, f"{profile_name}.jar")
    profile_json = os.path.join(profile_dir, f"{profile_name}.json")

    meta_json_loader_response = requests.get(
        config.default_meta_server + config.loader_version_meta + f"/{game}/{loader}/profile/json"
    )
    if meta_json_loader_response.status_code == 200:
        meta_json_loader_game = meta_json_loader_response.json()
    else:
        print("no response from server")
        return

    with open(profile_json, "w") as json_file:
        meta_json_loader_game["id"] = profile_name
        json.dump(meta_json_loader_game, json_file)

    with open(profile_jar, 'wb') as file:
        file.write(b"")

    if not os.path.exists(config.lidsdir):
        # make the folder for the fabric profile in the launcher
        os.makedirs(config.lidsdir)

    for libdependency in meta_json_loader_game["libraries"]:
        libdepname = libdependency["name"]
        parts = libdepname.split(":", 3)
        libdepfname = parts[1] + "-" + parts[2] + ".jar"
        libdepurl = libdependency["url"] + parts[0].replace(".", "/") + "/" + parts[1] + "/" + parts[2] + "/" + libdepfname
        print(libdepurl)
        libdeppath = os.path.join(config.lidsdir, *parts[0].split("."), parts[1], parts[2])
        print(libdeppath)
        libdepfpath = os.path.join(libdeppath, libdepfname)
        if not os.path.exists(libdeppath):
            os.makedirs(libdeppath)
        if os.path.exists(libdepfpath):
            os.remove(libdepfpath)
        libresponse = requests.get(libdepurl)
        if not libresponse.status_code == 200:
            print(f"couldn't download lib {libdepfname}")
            return
        libresponsemd5 = requests.get(libdepurl + ".md5")
        if not libresponsemd5.status_code == 200:
            print(f"couldn't download the md5 for the lib {libdepfname}")
            return
        if not libresponsemd5.text == hashlib.md5(libresponse.content).hexdigest():
            print(f"The md5 checksum for lib {libdepfname} is not agreeing with the source")
            return
        with open(libdepfpath, 'wb') as file:
            file.write(libresponse.content)

    launcherprofilespath = os.path.join(config.mcdir, config.launcher_profiles_json[0])
    if not os.path.exists(launcherprofilespath):
        launcherprofilespath = os.path.join(config.mcdir, config.launcher_profiles_json[1])
        if not os.path.exists(launcherprofilespath):
            print("neither the profiles or the other thing was discovered, resorting to first guess")
            launcherprofilespath = os.path.join(config.mcdir, config.launcher_profiles_json[0])
            with open(launcherprofilespath, "w") as json_file:
                json.dump({"profiles": {}}, json_file)
    with open(launcherprofilespath, 'r') as json_file:
        profile_data = json.load(json_file)
    if 'profiles' not in profile_data:
        profile_data['profiles'] = {}
    profile_nam = f"Minelabs"
    if profile_nam not in profile_data["profiles"]:
        profile_data["profiles"][profile_nam] = {
            "name": profile_name,
            "type": "custom",
            "created": datetime.utcnow().isoformat(),
            "lastUsed": datetime.utcnow().isoformat(),
            "icon": config.png_data
        }
    profile_data["profiles"][profile_nam]["lastVersionId"] = profile_name
    with open(launcherprofilespath, "w") as json_file:
        json.dump(profile_data, json_file)
    return True