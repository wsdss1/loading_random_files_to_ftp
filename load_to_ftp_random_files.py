#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
check and creat local folder, generate random files in this folder. 
connect and upload all generated random files to ftp server.
check in DB messages about this files and write info to file result.
'''

import os, logging, logging.config, time, shutil, random, uuid, sys, pyodbc, datetime
from ftplib import FTP

HOST = "192.168.10.13"
PORT = 21
UNAME = "ftpuser"
PS = "12345"
ftp = FTP('192.168.10.13', 'ftpuser', '12345')
SQL_SERVER_CONNECT = "Driver={SQL Server Native Client 11.0};Server=192.168.10.24;Database=SSNTI;Trusted_Connection=no;uid=test;pwd=Password12!"

FTP_PATH = ['/home/ftpuser/','/home/ftpuser/test_ras','/home/ftpuser/test_ras_zip']

waveform_archive_t = ['to','t01','t02','t03','t04','t05','t06','t07','t08','t09','t0A','t0B','t0C','t0D','t0E','t0F']
waveform_archive_d = ['do','d01','d02','d03','d04','d05','d06','d07','d08','d09','d0A','d0B','d0C','d0D','d0E','d0F']
waveform_archive_zip = ['zip']
waveform_archive_os = ['os1.zip','os2.zip']

temp_folder = "temp_folder"
current_dir = os.path.dirname(os.path.realpath(__file__))
NEW_PATH = 'temp_folder_sended'
file_with_result = './results.txt'

# создаём logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
# создаём консольный и файловый handler-ы и задаём уровень
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
fh = logging.FileHandler(f'./log_{time.strftime("%Y%m%d")}.log')
fh.setLevel(logging.DEBUG)
# создаём formatter для handler-ов
formatter = logging.Formatter('%(asctime)s  [PID %(process)d]  %(levelname)s  [%(message)s]')
# добавляем formatter в ch и fh
ch.setFormatter(formatter)
fh.setFormatter(formatter)
# добавляем ch к logger
logger.addHandler(ch)
logger.addHandler(fh)


# check and create dirrectory
def create_dir(created_directory: str):
    try:
        # Create target Directory
        os.mkdir(created_directory)
        logger.info(f'{sys._getframe().f_code.co_name}  {created_directory}:created')
    except FileExistsError:
        logger.info(f'{sys._getframe().f_code.co_name}  {created_directory}:already exists')

# create random file 
def rnd_file_create():
    filenames = []
    archives = [waveform_archive_t, waveform_archive_d, waveform_archive_zip, waveform_archive_os]
    #used_archive = random.choice(archives)
    for arr in archives:
        # generate a random UUID
        filename = f'{uuid.uuid4()}'
        create_dir(temp_folder)
        for i in arr:
            full_filename = f'{current_dir}/temp_folder/{filename}.{i}'
            newfile = open(full_filename, 'wb')
            size = random.randint(100000, 9999999) # in bytes
            newfile.seek(size)
            newfile.write(b'\0')
            logger.info(f'{sys._getframe().f_code.co_name}  {full_filename}  size= {size} bytes')
            newfile.close()
        filenames.append(filename)
    return filenames


# upload file on ftp
def upload_ftp(file: str, ftp_path: str):
    logger.info(f'{sys._getframe().f_code.co_name}  try connect to {HOST}:{PORT} ftp server')
    ftp.connect(HOST, PORT)
    logger.info(f'{sys._getframe().f_code.co_name}  try login to ftp server')
    ftp.login(UNAME, PS)
    # Перейти в директорию
    ftp.cwd(ftp_path)
    logger.info(f'{sys._getframe().f_code.co_name}  read file from temp_folder')
    myfile = open(f'{current_dir}/temp_folder/{file}', 'rb')
    logger.info(f'{sys._getframe().f_code.co_name}  try stor file to ftp server')
    ftp.storbinary(f'STOR {file}', myfile)
    logger.info(f'{sys._getframe().f_code.co_name}  file sended to ftp server')
    myfile.close()

# read all files from local dir to send them to ftp 
def read_local_dir():
    create_dir(NEW_PATH)
    file_list = os.listdir(f'./{temp_folder}')
    num_files = len(os.listdir(f'./{temp_folder}'))
    logger.info(f'{sys._getframe().f_code.co_name}  read {num_files} files in {temp_folder}')
    for file in file_list:
        logger.info(f'{sys._getframe().f_code.co_name}  try upload {file} to ftp server')
        if file.endswith('.os1.zip'):
            upload_ftp(file, FTP_PATH[1])
        elif file.endswith('.os2.zip'):
            upload_ftp(file, FTP_PATH[1])
        elif file.endswith('.zip'):
            upload_ftp(file, FTP_PATH[2])
        else:
            upload_ftp(file, FTP_PATH[0])
        logger.info(f'{sys._getframe().f_code.co_name}  send file {file} to {NEW_PATH}') 
        shutil.move(f'{current_dir}\\temp_folder\{file}', f'{current_dir}\{NEW_PATH}')


# connect to sql server and execute SELECT   
def sql_connect_select(file_names):
    logger.info(f'{sys._getframe().f_code.co_name}  try connect to SQL Server:{HOST}')
    cnxn = pyodbc.connect(SQL_SERVER_CONNECT)
    cursor = cnxn.cursor()
    logger.info(f'{sys._getframe().f_code.co_name}  select from table') 
    #/****** Скрипт для команды SelectTopNRows из среды SSMS  ******/
    while len(file_names) != 0:
        logger.info(f'{sys._getframe().f_code.co_name}  wait wait 1 minute')
        time.sleep(60)
        for file_name in file_names:
            query_sql = f"SELECT * FROM [SSNTI_20181213].[dbo].[NTI_SYSEVENT] where Message like N'%{file_name}%' and Type='201'"
            rows_count = cursor.execute(query_sql)
            if cursor.rowcount == 0:
                logger.info(f'{sys._getframe().f_code.co_name}  wait information from SQL in table about this {file_name} file')
                print(f'{file_name} wait information from SQL in table about this {file_name} file \n')
            else:
                logger.info(f'{sys._getframe().f_code.co_name}  file {file_name} in Data Base.  OK!')
                file_names.remove(file_name)
        print(f' wait 1 minute \n')
    print('all files in the DB')

# create file result
def file_result(message: str):
    file = open(file_with_result, 'a')
    file.write(f'{message}\n')
    file.close()

if __name__ == '__main__':
    created_file = rnd_file_create()
    read_local_dir()
    sql_connect_select(created_file)   
    file_result(f'{datetime.now()} file {created_file} create -> file on ftp -> info in DB\n')