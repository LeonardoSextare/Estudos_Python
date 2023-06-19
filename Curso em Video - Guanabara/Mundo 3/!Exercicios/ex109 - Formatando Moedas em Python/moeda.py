# Modifique as funções que form criadas no desafio 107 para que elas aceitem um parâmetro a mais, informando se o valor retornado por elas vai ser ou não formatado pela função moeda(), desenvolvida no desafio 108.

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
