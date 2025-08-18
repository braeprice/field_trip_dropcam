@echo off
SET SCRIPT_DIR=%~dp0
CD /D "%SCRIPT_DIR%.."

REM Initialize conda for batch files
call "%LOCALAPPDATA%\miniconda3\Scripts\activate.bat" || "%LOCALAPPDATA%\anaconda3\Scripts\activate.bat" || "%LOCALAPPDATA%\miniconda3\Scripts\activate.bat" || call "%LOCALAPPDATA%\miniconda3\Scripts\activate.bat" || call "%USERPROFILE%\anaconda3\Scripts\activate.bat" || call "%USERPROFILE%\miniconda3\Scripts\activate.bat" || (
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