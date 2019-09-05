#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
upload file on ftp
'''

import log
from ftplib import FTP

def upload_ftp(ip_addr, port, user_name, password, work_ftp_path, file_name):
    log.logger.info(f'try connect to ftp {ip_addr}:{port}')
    ftp = FTP(f'{ip_addr}', f'{user_name}', f'{password}')
    ftp.connect(ip_addr, port)

    ftp.login(user_name, password)
    # Change Workind Directory
    ftp.cwd(work_ftp_path)
    myfile = open(f'{current_dir}/temp_folder/{file}', 'rb')
    ftp.storbinary(f'STOR {file_name}', myfile)
    myfile.close()