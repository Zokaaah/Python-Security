import hashlib



string = input('palavra a criptografar: ')

menu = int(input('''#### MENU - ESCOLHA O TIPO DE HASH ####
    1) MD5 
    2) SHA1 
    3) SHA256 
    4) SHA512 
                        
 DIGITE O NÚMERO DO HASH A SER GERADO:   '''))

if menu ==1:
    resultado = hashlib.md5(string.encode('utf-8'))
    print(resultado.hexdigest())

elif menu == 2:
    resultado = hashlib.sha1(string.encode('utf-8'))
    print(resultado.hexdigest())

elif menu == 3:
    resultado = hashlib.sha256(string.encode('utf-8'))
    print(resultado.hexdigest())

elif menu == 4:
    resultado = hashlib.sha512(string.encode('utf-8'))
    print(resultado.hexdigest())

else:
    print('NUMERO INVALIDO')