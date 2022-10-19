import os

import pysftp
import paramiko


def upload_files(file_paths: list[str]) -> None:
    host = str(os.getenv("SFTP_HOSTNAME"))
    user = str(os.getenv("SFTP_USERNAME"))
    pwd = str(os.getenv("SFTP_PASSWORD"))
    dir = str(os.getenv("SFTP_FOLDER"))

    print(f"\nuploading files to -> {host}")

    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())

    ssh.connect(host, 22, user, pwd)
    sftp = ssh.open_sftp()
    for file_path in file_paths:
        file_name = os.path.basename(file_path)
        sftp.put(file_path, os.path.join(dir, file_name))
        print(f"{file_name} saved at {os.path.join(dir, file_name)}")

    sftp.close()
    ssh.close()
