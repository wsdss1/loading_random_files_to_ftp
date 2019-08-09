#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
connect to sql server and execute SELECT
#SQL_SERVER_CONNECT = "Driver={SQL Server Native Client 11.0};Server=192.168.10.24;Database=SSNTI;Trusted_Connection=no;uid=test;pwd=Password12!"
'''

import pyodbc

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
            else:
                logger.info(f'{sys._getframe().f_code.co_name}  file {file_name} in Data Base.  OK!')
                file_names.remove(file_name)
        logger.info(f'{sys._getframe().f_code.co_name}  wait one minute ')
    logger.info(f'{sys._getframe().f_code.co_name}  all files in the DB')
    print('all files in DB')