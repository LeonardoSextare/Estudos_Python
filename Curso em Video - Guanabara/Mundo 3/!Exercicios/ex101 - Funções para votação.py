#Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL e OBRIGATÓRIO nas eleições.

def voto(nasc):
    from datetime import date
    ano = date.today().year
    idade = ano - nasc
    
    if 18 <= idade < 60:
        voto = 'Voto Obrigatorio'
    elif idade >= 16 or idade >= 60:
        voto = 'Voto Opcional'
    elif idade < 16:
        voto = 'Voto Negado'
    
    return {'idade':idade, 'situação': voto}


nasc = int(input('Que ano você nasceu??'))
result = voto(nasc)

print(f'Com {result["idade"]} anos: {result["situação"]}')