from FTPClient import FTPClient
def main():
    # FTP server credentials
    ftp_host = '10.199.22.85'
    ftp_port = 21
    ftp_user = 'test'
    ftp_password = 'test'

    # Create an instance of FTPClient
    ftp_client = FTPClient(ftp_host, ftp_port, ftp_user, ftp_password)

    # Connect to the FTP server
    ftp_client.connect()

    # Perform FTP operations and get the list of files and folders
    files_and_folders = ftp_client.list_files_and_folders()

    # Download from ftp to local
    remote_file_paths = ['/Public/istat/test.pdf', '/Public/istat/test.jpg', '/Public/istat/test.txt']
    local_file_paths = ['C:/Users/GuestGeosystems/OneDrive/Desktop/ftp/test.pdf', 'C:/Users/GuestGeosystems/OneDrive/Desktop/ftp/test.jpg', 'C:/Users/GuestGeosystems/OneDrive/Desktop/ftp/test.txt']
	
    for index, remote_file_path in enumerate(remote_file_paths):
        result = ftp_client.download_file(remote_file_path, local_file_paths[index])
        print(result)

    # Upload to ftp 
    local_file_paths = ['C:/Users/GuestGeosystems/OneDrive/Desktop/ftp/test.pdf', 'C:/Users/GuestGeosystems/OneDrive/Desktop/ftp/test.jpg', 'C:/Users/GuestGeosystems/OneDrive/Desktop/ftp/test.txt']
    remote_destination_paths = ['/Public/istat/test2.pdf', '/Public/istat/test2.jpg', '/Public/istat/test2.txt']
    for index, local_file_path in enumerate(local_file_paths):
        upload_result = ftp_client.upload_file(local_file_path, remote_destination_paths[index])
        print(upload_result)

    # Close the FTP connection
    ftp_client.close_connection()

    # Print or process the list of files and folders
    for item in files_and_folders:
        print(f"type: {item['type']}, absolute path: {item['path']}, name: {item['name']}")

if __name__ == "__main__":
    main()