# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade, se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
import time
sexo = int(input('Informe seu sexo: \n1 - Masculino\n2 - Feminino\n'))

if sexo == 1:
    ano = int(input('Insira seu ano de nascimento: \nAno: '))
    idade = time.localtime().tm_year - ano

    print(f'Quem nasceu em {ano} tem {idade} anos!')
    if idade == 17:
        print('Você deve se alistar em breve!')
    elif idade==18:
        print('Procure uma junta militar e se aliste!')
    elif idade < 17:
        print(f'Ainda falta {(18-idade)} anos para você se alistar em {time.localtime().tm_year + (18 - idade)}')
    else:
        print(f'Você está atrasado! Deveria ter se alistado em {time.localtime().tm_year - (idade-18)}!')
elif sexo == 2:
    print('O alistamento é opcional!')
        
    