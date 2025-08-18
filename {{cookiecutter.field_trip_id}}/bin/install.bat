@echo off
SET SCRIPT_DIR=%~dp0
CD /D "%SCRIPT_DIR%.."

echo Setting up conda environment from environment.yml...
echo.

REM Initialize conda for batch files
call "%USERPROFILE%\anaconda3\Scripts\activate.bat" || call "%USERPROFILE%\miniconda3\Scripts\activate.bat" || (
    echo ERROR: Could not find Anaconda/Miniconda installation
    echo Please ensure Anaconda or Miniconda is installed
    pause
    exit /b 1
)

REM Create environment from yml file
echo Creating conda environment 'cardmanager'...
call conda env create -f environment.yml

if errorlevel 1 (
    echo ERROR: Failed to create environment
    pause
    exit /b 1
) else (
    echo.
    echo SUCCESS: Environment 'cardmanager' created successfully!
    echo.
    echo To activate the environment, run:
    echo   conda activate cardmanager
    echo.
)

pause