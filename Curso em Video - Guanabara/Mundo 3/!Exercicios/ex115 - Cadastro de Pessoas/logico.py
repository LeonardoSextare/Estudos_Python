from arquivos import *


def leiaInt(msg):
    while True:
        try:
            num = int(input(msg))
        except (TypeError, ValueError):
            aviso('ERRO! Digite um número inteiro valido.', 'red', 0.5)
        except:
            aviso('ERRO! Tente novamente.', 'red', 0.5)
        else:
            return num

def leiaSexo():
    while True:
        try:
            sexo = str(input('Sexo [M/F]: '))[0].upper()
        except (IndexError):
            aviso('Sexo não pode ficar em branco', 'red', 0.5)
        except:
            aviso('ERRO! Tente novamente.', 'red', 0.5)
        else:
            if sexo in 'MF':
                return sexo
            aviso('Dado Invalido! Digite somente M ou F', 'red', 0.5)
        
def validarLista(escolha, lista):
    if escolha in range(1, len(lista)):
        return True
    else:
        aviso('Opção Invalida!', 'red', 0.5)
        return False


def scriptMenu(menu):
    if menu == 1:
        print(f'{"Nome":^25}{"Idade":^10}{"Sexo":>2}')
        lerArquivo(arquivo)
        linha()
        input('Pressione enter para voltar ao menu principal.')
    if menu == 2:
        nome = str(input('Nome: ')).strip().title()
        idade = leiaInt('Idade: ')
        sexo = leiaSexo()
        cadastrarP(arquivo, nome, idade, sexo)
    if menu == 3:
        exit()
