import socket
from threading import local

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)   #obj de conexao

print("Socket criado com sucesso")

host = 'localhost'
porta = 5432

s.bind((host,porta))

mensagem = 'Servidor, dale'

while 1:
    dados, end = s.recvfrom(4096)

    if dados:
        print('servidor enviando msg')
        s.sendto(dados + (mensagem.encode()), end)
