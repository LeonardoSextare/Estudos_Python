# Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante ‘a função input() do Python, só que fazendo a validação para aceitar apenas um valor numérico.
# Ex: n = leiaInt(‘Digite um n: ‘)
def leiaInt(msg=''):
    """Lê um valor e valida se é um número. Sem interromper o programa.

    parametros:
        msg (str, optional): mensagem a ser exibida na tela. Padrão é ' '.

    Retorna:
        (int)
    """
    while True:
        n = str(input(msg)).strip()
        if n.isnumeric():
            n = int(n)
            break
        else:
            print('ERRO! Digite um número valido')

    return n


numero = leiaInt('Digite um número:')

print(f'Você digitou número: {numero}')
