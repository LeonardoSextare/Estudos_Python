# Exercicio - Adiando execução de funções
def soma(x, y):
    return x + y


def multiplica(x, y):
    return x * y


def criar_funcao(funcao, n1):
    def executa(*args):
        return funcao(n1, *args)
    return executa


soma_com_cinco = criar_funcao(soma, 5)
multiplica_por_dez = criar_funcao(multiplica, 10)

soma_com_2 = criar_funcao(soma, 2)


print(soma_com_cinco(5))
print(multiplica_por_dez(30))
print(soma_com_2(30))
