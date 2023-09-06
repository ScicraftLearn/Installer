@echo off
setlocal enabledelayedexpansion

REM Check if there is at least one argument
if "%~1"=="" (
    echo No argument provided.
    goto :eof
)

set input_arg=%~1
call ./venv/Scripts/activate

REM Perform if statements based on the input argument
if "%input_arg%"=="alpha" (
    echo You chose option 1.
) else if "%input_arg%"=="latest" (
    echo You chose option 2.
) else if "%input_arg%"=="interface" (
    echo You chose option 3.
) else (
    echo Invalid option: %input_arg%
)