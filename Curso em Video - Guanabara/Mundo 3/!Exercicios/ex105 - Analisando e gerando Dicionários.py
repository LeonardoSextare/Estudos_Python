# Faça um programa que tenha uma função notas() que pode receber várias notas de alunos e vai retornar um dicionário com as seguintes informações:
# – Quantidade de notas
# – A maior nota
# – A menor nota
# – A média da turma
# – A situação (opcional)

def notas(*notas, sit=False):
    """
    -> Está função analisa as notas recebidas e retorna informações sobre elas.

    Args:
        sit (bool, optional): Retorna a situação do aluno. Padrão: False.

    Returns:
        dict: Número de Notas, Maior Nota, Menor nota, Média
    """
    media = sum(notas)/len(notas)
    resultado = {'total': len(notas), 'maior': max(notas),
                 'menor': min(notas), 'media': media}
    print(media)
    if sit == True:
        if media >= 7:
            stc = 'Excelente'
        elif 4 <= media < 7:
            stc = 'Razoavel'
        elif media < 4:
            stc = 'Ruim'
            
        resultado['situação'] = stc

    return dict(resultado)


aluno = notas(6,3,6,1)

print(aluno)