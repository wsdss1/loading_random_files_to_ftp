#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
upload file on ftp
'''

import log
from ftplib import FTP

def upload_ftp(file: str, ftp_path: str):
    ftp = FTP('192.168.10.13', 'ftpuser', '12345')
    ftp.connect(HOST, PORT)
    ftp.login(UNAME, PS)
    # Перейти в директорию
    ftp.cwd(ftp_path)
    myfile = open(f'{current_dir}/temp_folder/{file}', 'rb')
    ftp.storbinary(f'STOR {file}', myfile)
    myfile.close()