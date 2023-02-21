#Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
media = cont = int(0)

menorNum = maiorNum = num = int(input('Digite um número inteiro: '))
cont += 1
media += num
escolha = str(input('Você desejar continuar?[S/N]\n')).lower()

while escolha != 'n':
    num = int(input('Digite um número inteiro: '))
    cont += 1
    media += num
    
    if num < menorNum:
        menorNum = num
    if num > maiorNum:
        maiorNum = num
        
    escolha = str(input('Você desejar continuar?[S/N]\n')).lower()
media = media/cont
print(f'Você digitou {cont} números!\nMédia: {media}\nMaior Número: {maiorNum}\nMenor Número: {menorNum}')
