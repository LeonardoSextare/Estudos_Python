from interface import *

arquivo = 'cadastros.txt'


def inicializar(nome):
    os.system('cls')
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        aviso('Arquivo não encontrado!', 'red', 1)
        criarArquivo(nome)
    else:
        aviso('Arquivo encontrado!', 'green', 1)

    os.system('cls')


def criarArquivo(nome):
    aviso('Criando arquivo...', 'cyan', 2)
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        aviso('Houve um erro ao criar o arquivo', 'red', 1)
    else:
        aviso('Arquivo criado com sucesso!', 'green', 1)


def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        cprint('Houve um erro ao ler o arquivo', 'red')
    else:
        for linha in a:
            info = linha.split(';')
            info[2] = info[2].replace('\n', '')
            print(f'{info[0]:<24} {info[1]:^10} {info[2]:^3}')
    finally:
        a.close()


def cadastrarP(arq, nome='<não informado>', idade=0, sexo='N/A'):
    try:
        a = open(arq, 'at')
    except:
        aviso('Erro ao abrir o arquivo', 'red', 1)
    else:
        try:
            a.write(f'{nome};{idade};{sexo}\n')
        except:
            aviso('Erro ao escrever no arquivo', 'red', 1)
        else:
            aviso(f'{nome} cadastrado com sucesso!', 'green', 2)
        
