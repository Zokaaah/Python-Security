import random, string

tamanho = input('Quantos caracteres deseja na senha? ')

chars = string.ascii_uppercase + string.digits + '!@#$%&*()-+=,./?'

rnd = random.SystemRandom()

print(''.join(rnd.choice(chars) for i in range(int (tamanho))))