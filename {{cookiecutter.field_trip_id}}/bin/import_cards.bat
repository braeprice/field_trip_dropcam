@echo off
SET SCRIPT_DIR=%~dp0
CD /D "%SCRIPT_DIR%.."
sdcard import
pause