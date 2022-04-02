import os
print('-'* 60)
ip_ou_host = input('digite o Ip ou Host desejado: ')
print('-'* 60)

os.system('ping -n 6 {}'.format(ip_ou_host))

# arquivo = open('ip.txt', 'w')

# arquivo.write(str(os.system('ping -n 6 {}'.format(ip_ou_host))))
# arquivo.close()