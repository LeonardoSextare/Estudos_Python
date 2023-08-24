print('=== Palavra Secreta ===')
print('Tente adivinhar a palavra secreta!!\nSomente uma letra por vez!\n')

tentativa = str()
palavra_secreta = 'sabonete'
previa = list('*' * len(palavra_secreta))
qntd_tentativa = 0

while True:
    tentativa = input(f'Tentativa n°[{qntd_tentativa}]: ')
    if tentativa == palavra_secreta:
        break

    elif len(tentativa) == 1:
        if tentativa in palavra_secreta:
            for i in range(len(palavra_secreta)):
                if tentativa == palavra_secreta[i]:
                    previa[i] = tentativa

        print(f'Palavra formatada: {"".join(previa)}')
        qntd_tentativa += 1

    elif len(tentativa) > 1:
        print('Somente uma letra!')


print(f'Você acertou! A palavra era "{palavra_secreta}"!')
print(f'Número de tentativas: {qntd_tentativa}')
