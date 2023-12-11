# Python-ftpService
The provided code is a Python class FTPClient that encapsulates functionality for interacting with an FTP (File Transfer Protocol) server. 

This class provides a convenient interface for working with FTP servers, handling connection, file listing, checking file existence, downloading, uploading, and closing the connection.

The class FTPClient is defined, and its constructor (__init__) is used to initialize instance variables such as host, port, user, and password.
An instance of the FTP class from the ftplib module is created and stored in the ftp attribute of the class.

The connect method establishes a connection to the FTP server using the provided host, port, username, and password.

The list_files_and_folders method retrieves a list of files and folders from the FTP server using the mlsd method. It processes the details and returns a list containing dictionaries with information about each item, including its type (file or folder), path, and name.

The file_exists method checks if a given file exists on the FTP server by changing to the file's directory, obtaining the file list, and checking if the file is in the list.
It handles the error_perm exception, specifically checking for a "550" error, which typically indicates that the file or directory doesn't exist.

The download_file method checks if the specified file exists on the server, and if so, it downloads the file and saves it locally using either binary or text mode.

The upload_file method uploads a local file to the FTP server using the storbinary method.

The close_connection method closes the connection to the FTP server using the quit method.
