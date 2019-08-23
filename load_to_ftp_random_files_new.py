#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
check and creat local folder, generate random files in this folder. 
connect and upload all generated random files to ftp server.
check in DB messages about this files and write info to file result.
'''

import os
import read_config_and_dir, create_dir_and_files, sql, log

conf_path_file = './config/config.json'
current_dir = os.path.dirname(os.path.realpath(__file__))

# create file result
def file_result(message: str):
    file = open(file_with_result, 'a')
    file.write(f'{message}\n')
    file.close()

if __name__ == '__main__':
    all_arr_rnd_file_names = []
    configuration = read_config_and_dir.read_config_file(conf_path_file)
    log.logger.info(f'received groups ending_files')
    # read from config file - ftp_host, ip_addr, port, user_name, password
    for ftp_host in configuration['ftp_hosts']:
        for ip_addr in configuration['ftp_hosts'][f'{ftp_host}']['ip_addrs']:
            for port in configuration['ftp_hosts'][f'{ftp_host}']['ports']:
                if check_access(ip_addr, port) == True:
                    log.logger.info(f'received from config file - ftp_host {ftp_host}, ip_addr {ip_addr}, port {port}, user_name, password')
                    # read arr ending files from config file
                    for key in configuration['ending_files']:
                        new_file_name = create_dir_and_files.rnd_file_create(current_dir, configuration['ending_files'][key])
                        # get all new file names
                        all_arr_rnd_file_names.append(new_file_name)
                else:
                    print(f'FTP cервер {ip_addr}:{port} в данный момент не доступен')
    print(all_arr_rnd_file_names)