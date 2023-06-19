try:
    a = int(input('N1: '))
    b = int(input('N2: '))
    c = a/b
except (ValueError, TypeError, ZeroDivisionError) as erro:
    print(f'Erro! {erro.__class__}')
else:
    print('Deu certo')
    
print('Teste')