def multiplica(*args):
    total = 1
    for c in range(len(args)):
        total *= args[c]
    return total


def parOuImpar(numero):
    resto = numero % 2
    if resto == 0:
        return 'Par'
    return 'Impar'


print(parOuImpar(multiplica(1, 3)))
