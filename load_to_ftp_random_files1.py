#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
check and creat local folder, generate random files in this folder. 
connect and upload all generated random files to ftp server.
check in DB messages about this files and write info to file result.
'''

import os, logging, logging.config, time, shutil, random, uuid, sys, pyodbc, datetime
from ftplib import FTP

HOST = "192.168.10.28"
PORT = 201
UNAME = "ftpuser"
PS = "!234Qwer"

#ftp = FTP('192.168.10.28', 'ftpuser', '!234Qwer')
ftp = FTP()

waveform_archive_t = ['to','t01','t02','t03','t04','t05','t06','t07','t08','t09','t0A','t0B','t0C','t0D','t0E','t0F']
waveform_archive_d = ['do','d01','d02','d03','d04','d05','d06','d07','d08','d09','d0A','d0B','d0C','d0D','d0E','d0F']

temp_folder = "temp_folder"
current_dir = os.path.dirname(os.path.realpath(__file__))
NEW_PATH = 'temp_folder_sended'

def rnd_file_create():
    filenames = []
    archives = [waveform_archive_t, waveform_archive_d]
    #used_archive = random.choice(archives)
    for arr in archives:
        # generate a random UUID
        filename = f'{uuid.uuid4()}'
        for i in arr:
            full_filename = f'{current_dir}/temp_folder/{filename}.{i}'
            newfile = open(full_filename, 'wb')
            size = random.randint(100000, 9999999) # in bytes
            newfile.seek(size)
            newfile.write(b'\0')
            newfile.close()
        filenames.append(filename)
    return filenames

# upload file on ftp
def upload_ftp(file: str):
    ftp.connect(HOST, PORT)
    ftp.login(UNAME, PS)
    # Перейти в директорию
    myfile = open(f'{current_dir}/temp_folder/{file}', 'rb')
    ftp.storbinary(f'STOR {file}', myfile)
    myfile.close()

# read all files from local dir to send them to ftp 
def read_local_dir():
    file_list = os.listdir(f'./{temp_folder}')
    num_files = len(os.listdir(f'./{temp_folder}'))
    for file in file_list:
        upload_ftp(file)
        shutil.move(f'{current_dir}\\temp_folder\{file}', f'{current_dir}\{NEW_PATH}')

if __name__ == '__main__':
    created_file = rnd_file_create()
    read_local_dir()
    print(f"all files on ftp{PORT}")