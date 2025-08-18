@echo off
SET SCRIPT_DIR=%~dp0
CD /D "%SCRIPT_DIR%.."

REM Initialize conda for batch files and activate base environment
call "%LOCALAPPDATA%\anaconda3\Scripts\activate.bat" base || call "%LOCALAPPDATA%\miniconda3\Scripts\activate.bat" base || call "%USERPROFILE%\anaconda3\Scripts\activate.bat" base || call "%USERPROFILE%\miniconda3\Scripts\activate.bat" base || (
    echo ERROR: Could not find Anaconda/Miniconda installation
    echo Please ensure Anaconda or Miniconda is installed
    pause
    exit /b 1
)

REM Activate the cardmanager environment
call conda activate cardmanager
if errorlevel 1 (
    echo ERROR: Could not activate cardmanager environment
    echo Please run install.bat first to create the environment
    pause
    exit /b 1
)

sdcard register
pause