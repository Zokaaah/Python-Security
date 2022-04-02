import hashlib
from hmac import digest

arquivo1 = 'C:/Users/gabri/Desktop/Python/Python Security/teste.txt'
arquivo2 = 'C:/Users/gabri/Desktop/Python/Python Security/teste2.txt'


hash1 = hashlib.new('ripemd160')

hash1.update(open(arquivo1, 'rb').read())

hash2 = hashlib.new('ripemd160')

hash2.update(open(arquivo2, 'rb').read())

if hash1.digest() != hash2.digest():
    print('Arquivos distintos:')
else:
    print('Arquivos iguais')


print('Primeiro arquivo: ', hash1.hexdigest())
print('Segundo arquivo:  ', hash2.hexdigest())
