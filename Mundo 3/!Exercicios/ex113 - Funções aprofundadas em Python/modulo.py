def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('ERRO! Digite um número inteiro valido.')
            continue
        except (KeyboardInterrupt):
            print('Usuario Interrompeu a Operação.')
            return 0
        else:
            return n
        
        
def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (TypeError, ValueError):
            print('ERRO! Digite um número decimal valido.')
        except KeyboardInterrupt:
            print('Usuario Interrompeu a Operação.')
            return 0
        else:
            return n