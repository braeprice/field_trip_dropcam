@echo off
SET SCRIPT_DIR=%~dp0
CD /D "%SCRIPT_DIR%.."

echo Setting up conda environment from environment.yml...
echo.

REM Check if conda is available
conda --version >nul 2>&1
if errorlevel 1 (
    echo ERROR: Conda is not installed or not in PATH
    echo Please install Anaconda or Miniconda first
    pause
    exit /b 1
)

REM Create environment from yml file
echo Creating conda environment 'cardmanager'...
conda env create -f environment.yml

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