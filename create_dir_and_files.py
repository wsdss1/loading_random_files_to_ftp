#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
check and create directory
generate random file and upload on ftp-servers
'''

import os, random, uuid
import load_to_ftp_random_files_new, log, upload_file_to_ftp, read_config_and_dir

subfolders = 'temp_folder'

def create_dir(creating_directory: str):
    try:
        # Create target Directory
        os.mkdir(creating_directory)
        log.logger.info(f'created {creating_directory} directory')
    except FileExistsError:
        log.logger.info(f'directory {creating_directory} already exist')

# create random file
def rnd_file_create(current_dir, arr_ending, ip_addr, port, user_name, password):
    # ip_addr, port, user_name, password, work_ftp_path, file_name
    # generate a random UUID
    filename = f'{uuid.uuid4()}'
    log.logger.info(f'generate random file name {filename}')
    create_dir(subfolders)
    for end_file in arr_ending:
        full_filename = f'{current_dir}/{subfolders}/{filename}.{end_file}'
        newfile = open(full_filename, 'wb')
        size = random.randint(10000, 999999) # in bytes
        newfile.seek(size)
        newfile.write(b'\0')
        newfile.close()
        log.logger.info(f'created random files {full_filename}')
        # upload created file to ftp
        if "t" or "d" in end_file:
            work_ftp_path = '/'
            upload_file_to_ftp(f'{ip_addr}', f'{port}', f'{user_name}', f'{password}', f'{work_ftp_path}', f'{full_filename}')
        elif "os" in end_file:
            work_ftp_path = '/os_zip'
            upload_file_to_ftp(f'{ip_addr}', f'{port}', f'{user_name}', f'{password}', f'{work_ftp_path}', f'{full_filename}')
        elif "zip" in end_file:
            work_ftp_path = '/zip'
            upload_file_to_ftp(f'{ip_addr}', f'{port}', f'{user_name}', f'{password}', f'{work_ftp_path}', f'{full_filename}')
    return filename