#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
check and create directory
'''

import os, random, uuid
import load_to_ftp_random_files_new, log, upload_file_to_ftp

subfolders = "temp_folder"

def create_dir(creating_directory: str):
    try:
        # Create target Directory
        os.mkdir(creating_directory)
        log.logger.info(f"created {creating_directory} directory")
    except FileExistsError:
        log.logger.info(f"directory {creating_directory} already exist")

# create random file
def rnd_file_create(current_dir, arr_ending):
    # generate a random UUID
    filename = f'{uuid.uuid4()}'
    log.logger.info(f"generate random file name {filename}")
    create_dir(subfolders)
    for end_file in arr_ending:
        full_filename = f'{current_dir}/{subfolders}/{filename}.{end_file}'
        newfile = open(full_filename, 'wb')
        size = random.randint(10000, 999999) # in bytes
        newfile.seek(size)
        newfile.write(b'\0')
        newfile.close()
        log.logger.info(f"created random files {full_filename}")
        #upload_file_to_ftp(ftp, full_filename)
        #myfile = open(f'{current_dir}/temp_folder/{file}', 'rb')
    return filename

