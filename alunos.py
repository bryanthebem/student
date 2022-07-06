#4) Média do Aluno; Solicite o nome e 3 valores, no caso, variáveis A, B e C, que são as três notas de um aluno.
# A seguir, calcule a média do aluno, sabendo que a nota A tem peso 2, a nota B tem peso 3 e a nota C tem peso 5. 
# Armazene estes dados em um dicionário. Escreva um programa que solicita os dados de N alunos.
# Armazene estes dados em uma lista e ao final informe o total de alunos aprovados e reprovados. 
# Considere como média para aprovação, média igual ou superior a 6.0. Considere que cada nota pode ir de 0 até 10.0.

L=[]
alunos_aprovados = 0
alunos_reprovados = 0
N = int(input('Digite a quantidade de alunos:'))
for i in range(N):
    Nome = input('Insira o nome do aluno: ')
    A = int(input('Digite a primeira nota do aluno: '))
    B = int(input('Digite a segunda nota do aluno: '))
    C = int(input('Digite a terceira nota do aluno: '))
    media = (A*2 + B*3 + C*5) / 10
    aluno = {'nome': Nome, 'A': A, 'B':B,'C': C, 'media': media }
    L.append(aluno)
    if media >= 6.0:
        alunos_aprovados = alunos_aprovados + 1
    else:
        alunos_reprovados = alunos_reprovados + 1
print('qtd alunos aprovados foram: ', alunos_aprovados, 'qtd alunos reprovados foram: ', alunos_reprovados)
      