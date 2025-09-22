# Fazer um programa que irá receber duas notas e irá calcular a média e verificar se o aluno está aprovado ou reprovado. Para estar aprovado é necessário obter uma média igual ou superior a 5, caso contrário o aluno estará reprovado.

p1 = float(input("Digite a sua nota da P1: "))

p2 = float(input("Digite a sua notga da P2: "))

m = (p1 + p2) / 2

if (m >= 5):
    print('Aprovado')

else:
    print('Reprovado')

print(m)
    


