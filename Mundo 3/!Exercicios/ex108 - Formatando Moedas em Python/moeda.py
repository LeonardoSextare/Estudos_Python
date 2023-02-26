# Adapte o código do desafio #107, criando uma função adicional chamada moeda() que consiga mostrar os números como um valor monetário formatado.

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


def moeda(n, moeda = 'R$'):
    final = f'{moeda} {n:.2f}'.replace('.',',')
    return final
