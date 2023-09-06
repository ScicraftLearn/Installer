@echo off
setlocal enabledelayedexpansion

REM Check if there is at least one argument
if "%~1"=="" (
    echo No argument provided.
    goto :eof
)

set input_arg=%~1
call ./venv/Scripts/activate

REM Common PyInstaller options
set common_options=--onefile app.py --icon=resources/images/minelabs-logo.ico --add-data "resources/*.json;resources"

REM Function to build a PyInstaller executable
REM TODO: the map_data variable can be removed after the maps are accessible from the internet
:build_executable
if "%input_arg%"=="alpha" (
    set executable_name=MineLabs-Alpha
    set map_data=--add-data resources/maps/vAlpha/*.zip;resources/maps/vAlpha\
) else if "%input_arg%"=="latest" (
    set executable_name=MineLabs-Latest
    set map_data=--add-data resources/maps/vLatest/*.zip;resources/maps/vLatest\
) else if "%input_arg%"=="interface" (
    set executable_name=MineLabs-Interface
    set map_data=--add-data resources/maps/vAlpha/*.zip;resources/maps/vAlpha\ --add-data resources/maps/vLatest/*.zip;resources/maps/vLatest\
) else (
    echo Invalid option: %input_arg%
    goto :eof
)

call py -m PyInstaller %common_options% --name "%executable_name%" %map_data%

:end
