# Minelabs installer

## Table of contents

- [Introduction](#introduction)
- [Functionality](#functionality)
    - [v1 - script version](#v1---script-version)
    - [v2 - GUI version](#v2---gui-version)
- [Running the code](#running-the-code)
- [Creating an executable](#creating-an-executable)
    - [Note](#note)
- [Adding new content to the installer](#adding-new-content-to-the-installer)
- [Changing the dialogues in the GUI version](#changing-the-dialogues-in-the-gui-version)

## Introduction

Welcome to the documentation for the Minelabs Installer, a tool designed to simplify the installation process of
essential components. The Minelabs Installer comes in two versions, each serving a distinct purpose.

The tool is only available for Windows.

## Functionality

### v1 - script version

The script version of the Minelabs installer is primarily for internal use.

This installs the following components:

- Minelabs mod
- Dashboard-link mod
- Demo world
- fabric
- fabric api

The version of these components depends on the version of the installer.

### v2 - GUI version

The GUI version of the Minelabs installer is intended for external use.

It provides the ability to do different types of installation:

- Standard installation:
    - Minelabs mod
    - Dashboard-link mod
    - Demo world
    - fabric
    - fabric api
- Teacher installation:
    - Minelabs mod
    - Demo world
    - fabric
    - fabric api
- Advanced install:
    - Here the user can choose which version and associated components to install.

Both standard installation and teacher installation is for the latest one available.

## Running the code

There is an install_requirements.bat file provided that creates a virtual environment and installs all the packages
needed to run the code.

After installing all packages, you can choose to run the script version or the GUI version:

- Script version:
    ```bash
     $ python script_version.py
     ``` 
- GUI version:
  ```bash
    $ python interface_version.py
    ``` 

## Creating an executable

To create an executable (see note first), you can use the following commands:

- Script version:
    ```bash
    $ python generate.py script
    ```
- GUI version:
    ```bash
    $ python generate.py interface
    ```

The executable will be created in the dist folder.

### Note

Before creating an executable from the script version, you must first change the release version in 2 places:

- script_version.py
    - In the try and except block there is a variable "version", chance this to the correct version.
- generate.py
    - In the main function there is a variable "r_version", chance this to the correct version.

After this you can create an executable for the script version.

## Adding new content to the installer

There is a config.json file provided. This file contains all the information about the content that can be installed.

If you want to add a new version of a mod, a map, etc. You can add it to this file by simply adding the version at the
top of the file in the versions field and adding the mod or map from that version to the specific field.

The file also contains what will be installed for the script version and the GUI version (default and teacher fields).
If the content needs to be changed for a version, you can change it in the specific field.

## Changing the dialogues in the GUI version

There is a dialog.json file provided. This file contains all the dialogues that are used in the GUI version.

If you want to change a dialogue, you can do so in this file. The file has the same structure as the interface.py file
located in the representation folder.
