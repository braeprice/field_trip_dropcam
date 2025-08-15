@echo off
SET SCRIPT_DIR=%~dp0
CD /D "%SCRIPT_DIR%.."

echo Do you want to clean the cards first? (Y/N)
set /p ANSWER="> "

if /I "%ANSWER%"=="Y" (
    echo Cleaning cards...
    sdcard import --move
) else (
    echo Not Cleaning Cards...
)

pause