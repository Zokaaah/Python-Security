import socket
from sqlite3 import connect
import sys


def main():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM, 0)
    except socket.error as e:
        print('A conexão falhou')
        print("erro{}".format(e))
        sys.exit()
    print('Socket criado com sucesso!!')

host_alvo= input('digite o host desejado: ')
porta_alvo = input('Digite a porta desejada: ')

try: 
    s.connect((host_alvo, int(porta_alvo)))
    print("Cliente TCP conectado com sucesso no Host:  " + host_alvo + " na porta: " + porta_alvo)
    s.shutdown(2)
except:
    print("Não foi possivel conectar no host: " + host_alvo + " na porta: " + porta_alvo)
    sys.exit()


if __name__ == "__main__":
    main()
