import socket #fazer o relacionamento entre placa de rede e sistema operacional
import sys #fornece acesso a algumas variaveis e funcões com interação com o interpretador (python)

def main():
    try:
        s = socket.socket(socket.AF_INET,socket.SOCK_STREAM, 0)
    except socket.error as e:
        print('A conexão falhou')
        print("Erro: {}".format(e))
        sys.exit()
    print('Socket criado com sucesso')


    HostAlvo = input('Digite o host ou ip a ser conectado: ')
    portaAlvo = input('diigte a porta a ser conectada')

    try:
        s.connect((HostAlvo,int(portaAlvo)))
        print('Cliente TCP conectado com sucesso no Host: ', HostAlvo, "e na Porta: ", portaAlvo)
        s.shutdown(2)
    except socket.error as e:
        print('A conexão falhou')
        print("Erro: {}".format(e))
        sys.exit()

if __name__ == '__main__':
    main()