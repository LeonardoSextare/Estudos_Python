# Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA, mostrando os 10 primeiros termos da progressão usando a estrutura while.

print('===== Calculadora de PA =====')
termo = int(input('Digite o Primeiro Termo: '))
razao = int(input('Digite a Razão da PA: '))
escolha = cont = int(10)
contfinal = 0

while escolha != 0:
    while cont < escolha*2:
        print(f'{termo} > ', end='')
        termo += razao
        cont += 1
        contfinal += 1
    print('Pausa')
    escolha = int(input('Quantos termos você quer mostrar? (0 - Encerra o programa)\n'))
    cont = escolha
print(f'O programa mostrou {contfinal} termos para você!')