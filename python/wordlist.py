import itertools

string = input("String a ser Permutada: ")

resultado = itertools.permutations(string, len(string))

for i in resultado:
    print(''.join(i))