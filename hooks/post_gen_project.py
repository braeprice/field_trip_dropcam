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
    
    # Create desktop shortcuts for batch files
    create_shortcuts_choice = input("Do you want to create desktop shortcuts for the batch files? (yes/no) [yes]: ").strip().lower()
    if create_shortcuts_choice == '' or create_shortcuts_choice == 'yes' or create_shortcuts_choice == 'y':
        import winshell
        from win32com.client import Dispatch
        
        desktop = winshell.desktop()
        field_trip_id = "{{ cookiecutter.field_trip_id }}"
        
        # List of batch files to create shortcuts for (with templated names)
        batch_files = [
            ("install.bat", "Install Environment", "shell32.dll,21"),  # Setup/install icon
            (f"{field_trip_id}_clean_cards.bat", f"{field_trip_id} - Clean Memory Cards", "shell32.dll,31"),  # Recycle bin icon
            (f"{field_trip_id}_import_cards.bat", f"{field_trip_id} - Import Memory Cards", "shell32.dll,132"),  # Import/download icon
            (f"{field_trip_id}_register_cards.bat", f"{field_trip_id} - Register Memory Cards", "shell32.dll,147")  # Document/register icon
        ]
        
        for bat_file, description, icon in batch_files:
            bat_path = os.path.join(BIN_DIR, bat_file)
            if os.path.exists(bat_path):
                shell = Dispatch('WScript.Shell')
                shortcut_path = os.path.join(desktop, f"{description}.lnk")
                shortcut = shell.CreateShortCut(shortcut_path)
                shortcut.Targetpath = bat_path
                shortcut.WorkingDirectory = os.path.dirname(bat_path)
                shortcut.Description = description
                shortcut.IconLocation = icon  # Set the icon
                shortcut.save()
                print(f"Created desktop shortcut: {description}")
            else:
                print(f"Warning: {bat_file} not found, skipping shortcut creation")
    else:
        print("Skipped creating desktop shortcuts")

