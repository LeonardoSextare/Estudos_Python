# Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) e mostre seu status, de acordo com a tabela abaixo:
# IMC abaixo de 18,5: Abaixo do Peso
# Entre 18,5 e 25: Peso Ideal
# 25 até 30: Sobrepeso
# 30 até 40: Obesidade
# Acima de 40: Obesidade Mórbida
from locale import setlocale, atof, LC_ALL
from pygame import mixer
from colorama import Fore, Back, init 

setlocale(LC_ALL, 'portuguese')
init(autoreset=True)

print(Fore.LIGHTCYAN_EX + """
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=
=               Calculadora de IMC                  =
=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=""")

nome = str(input('Digite seu nome: ')).strip().lower()
peso = str(input("Informe o seu peso em KG: "))
altura = str(input("Informe a sua altura (metro ou cm): "))

# Formata a Altura para float de acordo com o que foi digitado:
if ',' in altura:
    altura = atof(altura)
elif '.' in altura:
    altura = float(altura)
else:
    altura = float(altura)/100

# Formata o Peso para float de acordo com o que foi digitado:
if ',' in peso:
    peso = atof(peso)
else:
    peso = float(peso)

# Calculo de IMC
imc = peso / altura**2
if 'vitor' in nome or 'faul' in nome:
    nome = 'l3ft'
elif 'rafael' in nome or 'rafal' in nome:
    nome = 'F4ker404'

print(f'\nOlá {nome.capitalize()}! Seu indice de IMC é:',
      Fore.LIGHTBLUE_EX + f'{imc:.1f}', 'e você está ', end='')
if imc < 18.5:
    print(Fore.YELLOW + 'Abaixo do Peso!')
elif imc < 25:
    print('no', Fore.LIGHTGREEN_EX + 'Peso Ideal')
elif imc < 30:
    print(Fore.YELLOW + 'Acima do Peso!')
elif imc < 40:
    print(Fore.RED + 'Obeso!')
else:
    print('com', Back.RED + Fore.LIGHTWHITE_EX + 'Obesididade Morbida!')
    if 'pedro' in nome:
        print(Fore.RED + 'CADE PEGRIN MAGRELIN?')
    mixer.init()
    mixer.music.load("naoabra.mp3")
    mixer.music.play()
    while mixer.music.get_busy():
        pass


