import log, uuid, random

rez = []

a = [1,1,1]
b = [2,2,2,2]

rez.append(a)
rez.append(b)

a =["to", "t01", "t02", "t03", "t04", "t05", "t06", "t07", "t08", "t09", "t0A","do", "t0B", "d1", "t0C", "t0D", "t0E", "t0F", "zip"]

def rnd_file_create():
   # ip_addr, port, user_name, password, work_ftp_path, file_name
   # generate a random UUID
   filename = f'{uuid.uuid4()}'
   log.logger.info(f'generate random file name {filename}')
   for i in a:
      full_filename = f'./temp_folder/{filename}.{i}'
      newfile = open(full_filename, 'wb')
      size = random.randint(10000, 999999)  # in bytes
      newfile.seek(size)
      newfile.write(b'\0')
      newfile.close()

if __name__ == '__main__':
    rnd_file_create()
