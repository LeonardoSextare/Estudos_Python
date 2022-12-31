frase = 'Curso em Video Python'
print(frase)
 
print('\nPega o caractere das posição indicada')
print(frase[9])

print('\nPega os caracteres das posições indicadas [inicio:fim]')
print(frase[9:13])

print('\nPega os caracteres das posições indicadas pulando 2 [inicio:fim:pula]')
print(frase[9:18:2])

print('\nMostra quantas letras tem a frase len(frase) = 38 letras')
print(len(frase))

print('\nConta quantas vezes aparece a letra escolhida')
print(frase.count('X'))
 
print('\nProcura os caracteres escolhidos e mostra aonde começa no index / Se não tiver retorna -1')
print(frase.find('Video'))

print('\nLocaliza se a palavra está na string e retorna valor boleano')
print('Curso' in frase)

print('\nTroca uma palavra por outra na frase')
print(frase.replace('Python', 'Java'))

print('\nColoca todas as letras em maiúsculo')
print(frase.upper())

print('\nColocar todas letras em minusculo')
print(frase.lower())

print('\nColoca a primeira letra da frase em maiusculo e o resto minusculo')
print(frase.capitalize())

print('\nDeixa todas as palavras da string com a prmeira letra maiúscula')
print(frase.title())

print('\nTira o espaço do começo e no fim da frase / Variantes: frase.strip()  frase.lstrip()  frase.rstrip()')
print(frase.strip())

print('\nCria um lista com as palavras da string')
print(frase.split())

print('\nJuntar strings utilizando como separador a string informada')
print('='.join(frase))



# """ Tres(3) aspas para utilizar quebra de linha durante o codigo em string, ele irá quebrar a linha junto
