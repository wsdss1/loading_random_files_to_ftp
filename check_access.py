#!/usr/bin/python
# -*- coding: utf-8 -*-

'''
check access host by ip address and port
'''

import socket
import log

def check_access(ip, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((ip, int(port)))
        s.shutdown(2)
        log.logger.info(f'host {ip}:{port} available')
        return True
    except:
        log.logger.warning(f'host {ip}:{port} not available')
        return False
    finally:
        s.close()

if __name__ == '__main__':
    check_access('192.168.10.28', 2001)