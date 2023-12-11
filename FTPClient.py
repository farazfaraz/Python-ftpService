from ftplib import FTP, error_perm

class FTPClient:
    def __init__(self, host, port, user, password):
        self.host = host
        self.port = port
        self.user = user
        self.password = password
        self.ftp = FTP()

    def connect(self):
        print("Connecting to", self.host)
        self.ftp.connect(self.host, self.port)
        self.ftp.login(self.user, self.password)

    def list_files_and_folders(self):
        items_with_details = self.ftp.mlsd()

        result = []
        for name, facts in items_with_details:
            # Determine if it's a file or a folder
            item_type = "Folder" if facts["type"] == "dir" else "File"
            # Construct the absolute path
            absolute_path = self.ftp.pwd() + "/" + name
            # Append information to the result list
            result.append({"type": item_type, "path": absolute_path, "name": name})

        return result

    def file_exists(self, remote_file_path):
        try:
             # Get the directory part of the remote file path
            #  it only performs one split (1 as the second argument). The [0] at the end selects the first part of the split result, which represents the directory.
            remote_directory = remote_file_path.rsplit('/', 1)[0]
            # Get the current working directory
            current_directory = self.ftp.pwd()
            # Change to the directory of the remote file
            self.ftp.cwd(remote_directory)
            # Get a list of file names in the current directory
            file_list = self.ftp.nlst()
             # Check if the file exists in the list
            file_exists = remote_file_path.rsplit('/', 1)[-1] in file_list
            # Return to the original working directory
            self.ftp.cwd(current_directory)

            return file_exists
        except error_perm as e:
            if "550" in str(e):
                return False
            else:
                raise

    def download_file(self, remote_file_path, local_file_path):
        # The open() function is a built-in function in Python used for opening files. 
        # 'wb' specifies that you want to open the file in binary write mode.
        # The retrbinary method is then used to retrieve the binary file from the FTP server and save it locally.
        # The 'RETR' command is an FTP command used to retrieve (download) a file from the server. It stands for "Retrieve."
        if self.file_exists(remote_file_path):
            with open(local_file_path, 'wb') as local_file:
                try:
                    self.ftp.retrbinary('RETR ' + remote_file_path, local_file.write)
                except TypeError:
                    # If TypeError occurs, retry with 'RETR' in text mode
                    self.ftp.retrlines('RETR ' + remote_file_path, local_file.write)
            result = f"File downloaded successfully: {local_file_path}"
        else:
            result = f"File does not exist on the FTP server: {remote_file_path}"
        return result

    def upload_file(self, local_file_path, remote_file_path):
        # This upload_file method uses the storbinary method of the FTP object to store the binary file on the FTP server. 
        # The 'STOR' command is an FTP command used to store (upload) a file to the server.
        try:
            with open(local_file_path, 'rb') as local_file:
                self.ftp.storbinary('STOR ' + remote_file_path, local_file)
            result = f"File uploaded successfully: {local_file_path} to {remote_file_path}"
        except FileNotFoundError:
            result = f"Local file not found: {local_file_path}"
        except Exception as e:
            result = f"Error uploading file: {e}"

        return result

    def close_connection(self):
        self.ftp.quit()

