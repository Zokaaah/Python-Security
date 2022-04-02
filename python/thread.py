from threading import Thread
import time

def carro(velocidade, piloto):
    trajeto = 0
    # velocidade = int(input('Defina a velocidade'))
    while trajeto <= 20:
        print('Piloto: {} Km:  {} \n'.format(piloto , trajeto))
        trajeto += velocidade
        time.sleep(0.5)
        


# carro1(10)
# carro2(20)        


t_carro1 = Thread (target=carro, args=[2, 'Zokah',])
t_carro2 = Thread (target=carro, args=[3, 'Zokahryus'])

t_carro1.start()
t_carro2.start()

