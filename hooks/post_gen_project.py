import os
import platform
import shutil

for root, dirs, files in os.walk("."):
    for filename in files:
        if filename == ".gitkeep":
            filepath = os.path.join(root, filename)
            os.remove(filepath)




BIN_DIR = os.path.join(os.getcwd(), "bin")
#os.makedirs(BIN_DIR, exist_ok=True)

def download(url, dest):
    print(f"Downloading {url} ...")
    urllib.request.urlretrieve(url, dest)

system = platform.system().lower()

if "windows" in system:
    # Example: Download rclone

    
    import shutil   
    import urllib.request
    import zipfile

    # ask the user if they want to download rclone yes or no
    rclone_choice = input("Do you want to download rclone? (yes/no) [yes]: ").strip().lower()
    if rclone_choice == '' or rclone_choice == 'yes' or rclone_choice == 'y':
            
        rclone_url = "https://downloads.rclone.org/v1.67.0/rclone-v1.67.0-windows-amd64.zip"
        zip_path = os.path.join(BIN_DIR, "rclone.zip")
        download(rclone_url, zip_path)
        with zipfile.ZipFile(zip_path, 'r') as zf:
            zf.extractall(BIN_DIR)
        os.remove(zip_path)
        rclone_path = os.path.join(BIN_DIR, "rclone-v1.67.0-windows-amd64", "rclone.exe")
        new_rclone_path = os.path.join(BIN_DIR, "rclone.exe")
        if os.path.exists(rclone_path):
            shutil.copy2(rclone_path, new_rclone_path)
    else:
        print(f"Please download rclone manually from https://rclone.org/downloads/ and place it in the bin directory. {BIN_DIR}")

    # ask the user if they want to download exiftool yes or no
    exiftool_choice = input("Do you want to download exiftool? (yes/no) [yes]: ").strip().lower()
    if exiftool_choice == 'no' or exiftool_choice == 'n':
        print(f"Please download exiftool manually from https://exiftool.org/ and place it in the bin directory. {BIN_DIR}")
        print("And remember to rename the executable to 'exiftool.exe' in the bin directory.")
        exit(0) 
    # Example: Download exiftool
    exiftool_url = "https://sourceforge.net/projects/exiftool/files/exiftool-13.33_64.zip/download"
    zip_path = os.path.join(BIN_DIR, "exiftool.zip")
    download(exiftool_url, zip_path)
    with zipfile.ZipFile(zip_path, 'r') as zf:
        zf.extractall(BIN_DIR)
    os.remove(zip_path) 
    
    # Rename the exiftool executable and move it to the bin directory 
    exiftool_exe = os.path.join(BIN_DIR, "exiftool-13.33_64","exiftool(-k).exe")
    new_exiftool_exe = os.path.join(BIN_DIR, "exiftool.exe")
    if os.path.exists(exiftool_exe):
        shutil.copy2(exiftool_exe, new_exiftool_exe)

