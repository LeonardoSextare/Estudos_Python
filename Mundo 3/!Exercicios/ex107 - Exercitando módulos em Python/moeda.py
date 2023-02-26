# Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade().
# Faça também um programa que importe esse módulo e use algumas dessas funções.


def aumentar(num, aumento):
    """Aumenta em porcentagem o valor informado em num

    Args:
        num (number): Valor a ser aumentado
        aumento (number): Porcentagem a ser acrescida no valor

    Returns:
        float: Valor acrescido por num
    """
    return num*(aumento/100) + num


def diminuir(num, diminuir):
    """Diminui em porcentagem o valor informado em num

    Args:
        num (number): Valor a ser diminuido
        diminuir (number): _description_

    Returns:
        float: Valor decrescido por num
    """
    return num - num*(diminuir/100)


def dobro(n):
    """Retorna o dobro de um valor

    Args:
        n (number): 

    Returns:
        number: o dobro de um número
    """
    return n*2


def metade(n):
    return n/2
