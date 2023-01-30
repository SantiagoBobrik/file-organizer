import time
import os
import getpass
import platform as pf


file_extensions = {
    'images': ['jpg', 'jpeg', 'png', 'gif', 'svg', 'bmp', 'ico', 'psd', 'tif', 'tiff'],
    'documents': ['doc', 'docx', 'pdf', 'txt', 'xls', 'xlsx', 'ppt', 'pptx', 'epub', 'md'],
    'apps': ['exe', 'dmg', 'pkg', 'deb', 'rpm'],
    'compressed': ['zip', 'rar', 'tar', 'gz', '7z', 'iso'],
    'sounds':  ['mp3', 'wav', 'ogg', 'flac', 'aac'],
    'videos': ['mp4', 'mkv', 'avi', 'mov', 'wmv', 'flv', 'webm', '3gp'],
    'other': ['bin', 'dat', 'db', 'log', 'msi', 'part', 'torrent', 'nupkg'],
}


def get_download_dir():
    # Download directory
    WIN_DOWNLOAD_DIR = f"C:\\Users\\{getpass.getuser()}\\Downloads\\"
    MAC_DOWNLOAD_DIR = f"/Users/{getpass.getuser()}/Downloads/"
    platform = pf.platform()

    # SO check
    if platform.startswith('Windows'):
        download_dir = WIN_DOWNLOAD_DIR
    elif platform.startswith('macOS'):
        download_dir = MAC_DOWNLOAD_DIR
    else:
        print("OS not supported.")
        exit(1)
    return download_dir


def get_files(folder):
    try:
        files = os.listdir(folder)
    except OSError:
        print(f"Error getting files from {folder}:")
        files = []
    return files


def main():

    download_dir = get_download_dir()
    files = get_files(download_dir)
    folders = file_extensions.keys()

    for folder in folders:

        for file in files:

            file_extension = file.split('.')[-1]
            folder_path = os.path.join(download_dir, folder)

            if file_extension in file_extensions[folder]:

                # Rename file if already exists. Format: timestamp-filename
                renamed_file = None
                if os.path.exists(os.path.join(folder_path, file)):
                    renamed_file = f'{int(time.time())}-{file}'

                # Move file to folder
                file_path = os.path.join(download_dir, file)
                dest_path = os.path.join(folder_path, renamed_file or file)

                try:
                    # Create folder if not exists
                    if not os.path.exists(folder_path):
                        os.mkdir(folder_path)

                    os.rename(file_path, dest_path)

                    print(f"Moved {file} to {folder}")
                except OSError:
                    print(f"Error moving {file} to {folder}")


if __name__ == '__main__':
    main()
    print("Done!")
    input('Press ENTER to exit')
