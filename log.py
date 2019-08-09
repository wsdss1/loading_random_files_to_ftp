import logging, time

# создаём logger
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
# создаём консольный и файловый handler-ы и задаём уровень
ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
fh = logging.FileHandler(f'./log_{time.strftime("%Y%m%d")}.log')
fh.setLevel(logging.DEBUG)
# создаём formatter для handler-ов
formatter = logging.Formatter('%(asctime)s  [PID %(process)d]  %(module)s  [%(levelname)s]  %(message)s')
# добавляем formatter в ch и fh
ch.setFormatter(formatter)
fh.setFormatter(formatter)
# добавляем ch к logger
logger.addHandler(ch)
logger.addHandler(fh)