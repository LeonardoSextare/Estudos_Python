#  Crie um programa que tenha uma função fatorial() que receba dois parâmetros:
# o primeiro que indique o número a calcular e outro chamado show, que será um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.
def fatorial(n1, show=False):
    """
    --> Calcula o fatorial de um número.
    :parametro n1: Número a ser calculado
    :parametro show: Se definido como true, irá mostrar o calculo. Padrão: false
    :retorna o resultado do calculo
    """
    resultado = 1
    for c in range(n1, 0, -1):
        resultado *= c
        if show == True:
            if c == n1:
                print(f'{n1}! =', end='')
            if c > 1:
                print(f' {c} X', end='')
            else:
                print(f' {c} = ', end='')
            
    return resultado
    

print(fatorial(5, show=True))
print(fatorial(5))
