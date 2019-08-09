#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
read config file by default path in json format
'''

import json, sys
import log

def read_config_file(config_path: str):
    with open(config_path) as config_file:
        data = json.load(config_file)
        log.logger.info(f'read and load conf file {config_path}')
    return data

# read all files from local dir to send them to ftp
def read_local_dir():
    create_dir(NEW_PATH)
    file_list = os.listdir(f'./{temp_folder}')
    num_files = len(os.listdir(f'./{temp_folder}'))
    log.logger.info(f'{sys._getframe().f_code.co_name}  read {num_files} files in {temp_folder}')
    for file in file_list:
        log.logger.info(f'{sys._getframe().f_code.co_name}  try upload {file} to ftp server')
        if file.endswith('.os1.zip'):
            upload_ftp(file, FTP_PATH[1])
        elif file.endswith('.os2.zip'):
            upload_ftp(file, FTP_PATH[1])
        elif file.endswith('.zip'):
            upload_ftp(file, FTP_PATH[2])
        else:
            upload_ftp(file, FTP_PATH[0])
        log.logger.info(f'{sys._getframe().f_code.co_name}  send file {file} to {NEW_PATH}')
#        shutil.move(f'{current_dir}\\temp_folder\{file}', f'{current_dir}\{NEW_PATH}')