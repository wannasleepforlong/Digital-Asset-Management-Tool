import io
import os
from googleapiclient.http import MediaIoBaseDownload
from quickstart import main as get_drive_service  # Assuming your auth file is named `your_auth_file.py`

def download_file(service, file_id, file_name):
    """Downloads a file from Google Drive."""
    request = service.files().get_media(fileId=file_id)
    file_path = os.path.join(os.getcwd(), file_name)
    
    fh = io.FileIO(file_path, "wb")
    downloader = MediaIoBaseDownload(fh, request)

    done = False
    while not done:
        status, done = downloader.next_chunk()
        print(f"Download {int(status.progress() * 100)}%.")

    print(f"File downloaded to {file_path}")

if __name__ == "__main__":
    service = get_drive_service()  # This should be your authenticated Drive API service
    # Specify the file ID and name of the image you want to download
    file_id = "your_file_id_here"  # Replace this with the actual file ID of the image on your Google Drive
    file_name = "download.jpg"  # Replace this with the name you want for the downloaded file

    # Call the download function
    download_file(service, file_id, file_name)
