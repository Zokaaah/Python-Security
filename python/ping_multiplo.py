import os
import time 

with open('C:/Users/gabri/Desktop/Python/Python Security/hosts.txt') as file:
    dump = file.read()
    dump = dump.splitlines()

    print(dump)

    for ip in dump:
        print('Verificando os Ips')
        print('-' *60)
        os.system('ping -n 2 {}'.format(ip))
        print('-' *60)
        time.sleep(5)