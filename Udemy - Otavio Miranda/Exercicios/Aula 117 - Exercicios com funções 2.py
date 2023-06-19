def multiplicar(multiplicador):
    def funcao(numero):
        return numero * multiplicador

    return funcao


duplica = multiplicar(2)
triplica = multiplicar(3)
quadruplica = multiplicar(4)

print(duplica(2))
print(triplica(2))
print(quadruplica(2))
