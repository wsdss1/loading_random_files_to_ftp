#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
check and creat local folder, generate random files in this folder. 
connect and upload all generated random files to ftp server.
check in DB messages about this files and write info to file result.
'''

import os
import read_config_and_dir, create_dir_and_files, sql, log

conf_path_file = "./config/config.json"
current_dir = os.path.dirname(os.path.realpath(__file__))

# create file result
def file_result(message: str):
    file = open(file_with_result, 'a')
    file.write(f'{message}\n')
    file.close()

if __name__ == '__main__':
    all_arr_rnd_file_names = []
    configuration = read_config_and_dir.read_config_file(conf_path_file)
 #   ending_files = configuration["ending_files"]
    log.logger.info(f'received groups ending_files')
 #   for host in configuration["ftp_hosts"]["linux_ftps"]["hosts"]:

    for key in configuration["ending_files"]:
        new_file_name = create_dir_and_files.rnd_file_create(current_dir, configuration["ending_files"][key])
        all_arr_rnd_file_names.append(new_file_name)
    print(all_arr_rnd_file_names)