import os
import platform

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
    import urllib.request
    import zipfile
    rclone_url = "https://downloads.rclone.org/v1.67.0/rclone-v1.67.0-windows-amd64.zip"
    zip_path = os.path.join(BIN_DIR, "rclone.zip")
    download(rclone_url, zip_path)
    with zipfile.ZipFile(zip_path, 'r') as zf:
        zf.extractall(BIN_DIR)
    os.remove(zip_path)

    # Example: Download exiftool
    exiftool_url = "https://exiftool.org/exiftool-13.01.zip"
    zip_path = os.path.join(BIN_DIR, "exiftool.zip")
    download(exiftool_url, zip_path)
    with zipfile.ZipFile(zip_path, 'r') as zf:
        zf.extractall(BIN_DIR)
    os.remove(zip_path)            