# Adicione o módulo moeda.py criado nos desafios anteriores, uma função chamada resumo(), que mostre na tela algumas informações geradas pelas funções que já temos no módulo criado até aqui.
def aumentar(num, aumento, format=False):
    """Aumenta em porcentagem o valor informado em num

    Args:
        num (number): Valor a ser aumentado
        aumento (number): Porcentagem a ser acrescida no valor

    Returns:
        float: Valor acrescido por num
    """
    resultado = num*(aumento/100) + num
    if format == True:
        return moeda(resultado)
    else:
        return resultado


def diminuir(num, diminuir,format=False):
    """Diminui em porcentagem o valor informado em num

    Args:
        num (number): Valor a ser diminuido
        diminuir (number): _description_

    Returns:
        float: Valor decrescido por num
    """
    resultado = num - num*(diminuir/100)
    if format == True:
        
        return moeda(resultado)
    else:
        return resultado


def dobro(n, format=False):
    """Retorna o dobro de um valor

    Args:
        n (number): 

    Returns:
        number: o dobro de um número
    """
    resultado = n*2
    if format == True:
        return moeda(resultado)
    else:
        return resultado


def metade(n, format=False):
    resultado = n/2
    if format == True:
        return moeda(resultado)
    else:
        return resultado


def moeda(n, moeda = 'R$'):
    final = f'{moeda} {n:.2f}'.replace('.',',')
    return final

def resumo(num=0, aum=0, red=0):
    print('='*40)
    print(f'Resumo do valor'.center(40))
    print('='*40)
    print(f'Preço Analisado: \t{moeda(num)}')
    print(f'Dobro do preço: \t{dobro(num, True)}')
    print(f'Metade do preço: \t{metade(num,True)}')
    print(f'Aumento de {aum}%: \t{aumentar(num, aum,True)}')
    print(f'Redução de {red}%: \t{diminuir(num, red,True)}')
    