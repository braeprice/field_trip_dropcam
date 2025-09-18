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
        
        # Create a folder on the desktop for the shortcuts
        folder_name = f"{field_trip_id} - Field Trip Tools"
        desktop_folder = os.path.join(desktop, folder_name)
        os.makedirs(desktop_folder, exist_ok=True)
        
        # List of batch files to create shortcuts for (with templated names)
        batch_files = [
            ("install.bat", "Install Environment", "shell32.dll,21"),  # Setup/install icon
            (f"99_{field_trip_id}_clean_cards.bat", f"{field_trip_id} - Clean Memory Cards", "shell32.dll,31"),  # Recycle bin icon
            (f"02_{field_trip_id}_import_cards.bat", f"{field_trip_id} - Import Memory Cards", "shell32.dll,308"),  # Import/download icon
            (f"01_{field_trip_id}_register_cards.bat", f"{field_trip_id} - Register Memory Cards", "shell32.dll,21"),  # Document/register icon
            (f"03_{field_trip_id}_process_exif.bat", f"{field_trip_id} - Process EXIF Data", "shell32.dll,16776"),  # Document/register icon
            (f"04_{field_trip_id}_process_all.bat", f"{field_trip_id} - Process All Data", "shell32.dll,51380")  # Document/register icon
        ]
        
        for bat_file, description, icon in batch_files:
            bat_path = os.path.join(BIN_DIR, bat_file)
            if os.path.exists(bat_path):
                shell = Dispatch('WScript.Shell')
                shortcut_path = os.path.join(desktop_folder, f"{description}.lnk")
                shortcut = shell.CreateShortCut(shortcut_path)
                shortcut.Targetpath = bat_path
                shortcut.WorkingDirectory = os.path.dirname(bat_path)
                shortcut.Description = description
                shortcut.IconLocation = icon  # Set the icon
                shortcut.save()
                print(f"Created desktop shortcut: {description}")
            else:
                print(f"Warning: {bat_file} not found, skipping shortcut creation")
        
        print(f"Created desktop folder: {folder_name}")
    else:
        print("Skipped creating desktop shortcuts")
    
    # Download ffmpeg (latest static build for Windows)
    ffmpeg_choice = input("Do you want to download ffmpeg? (yes/no) [yes]: ").strip().lower()
    if ffmpeg_choice == '' or ffmpeg_choice == 'yes' or ffmpeg_choice == 'y':
        ffmpeg_url = "https://www.gyan.dev/ffmpeg/builds/ffmpeg-release-essentials.zip"
        zip_path = os.path.join(BIN_DIR, "ffmpeg.zip")
        print(f"Downloading {ffmpeg_url} ...")
        download(ffmpeg_url, zip_path)
        with zipfile.ZipFile(zip_path, 'r') as zf:
            zf.extractall(BIN_DIR)
        os.remove(zip_path)
        # Find ffmpeg.exe and copy to BIN_DIR
        for root, dirs, files in os.walk(BIN_DIR):
            if "ffmpeg.exe" in files:
                ffmpeg_exe = os.path.join(root, "ffmpeg.exe")
                shutil.copy2(ffmpeg_exe, os.path.join(BIN_DIR, "ffmpeg.exe"))
                print("ffmpeg.exe copied to bin directory.")
                break
            if "ffprobe.exe" in files:
                ffprobe_exe = os.path.join(root, "ffprobe.exe")
                shutil.copy2(ffprobe_exe, os.path.join(BIN_DIR, "ffprobe.exe"))
                print("ffprobe.exe copied to bin directory.")
    else:
        print(f"Please download ffmpeg manually from https://ffmpeg.org/download.html and place ffmpeg.exe in the bin directory. {BIN_DIR}")

    # Download cwrsync
    cwrsync_choice = input("Do you want to download cwrsync? (yes/no) [yes]: ").strip().lower()
    if cwrsync_choice == '' or cwrsync_choice == 'yes' or cwrsync_choice == 'y':
        cwrsync_url = "https://github.com/cwRsync/cwRsync/releases/download/v6.4.5/cwrsync_6.4.5_x64_free.zip"
        zip_path = os.path.join(BIN_DIR, "cwrsync.zip")
        print(f"Downloading {cwrsync_url} ...")
        download(cwrsync_url, zip_path)
        with zipfile.ZipFile(zip_path, 'r') as zf:
            zf.extractall(BIN_DIR)
        os.remove(zip_path)
        # Find rsync.exe and copy to BIN_DIR
        for root, dirs, files in os.walk(BIN_DIR):
            if "rsync.exe" in files:
                rsync_exe = os.path.join(root, "rsync.exe")
                shutil.copy2(rsync_exe, os.path.join(BIN_DIR, "rsync.exe"))
                print("rsync.exe copied to bin directory.")
            for file in files:
                if file.lower().endswith('.dll'):
                    dll_src = os.path.join(root, file)
                    dll_dst = os.path.join(BIN_DIR, file)
                    if not os.path.exists(dll_dst):
                        shutil.copy2(dll_src, dll_dst)
    else:
        print(f"Please download cwrsync manually from https://github.com/cwRsync/cwRsync/releases and place rsync.exe in the bin directory. {BIN_DIR}")

