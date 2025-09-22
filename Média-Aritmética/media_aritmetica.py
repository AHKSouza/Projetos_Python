# Calcular e exibir a média aritmética de quatro valores quaisquer que serão digitados.

a = float(input('Digite o primeiro valor:'))
b = float(input('Digite o segundo valor: '))
c = float(input('Digite o terceiro valor: '))
d = float(input('Digite o quarto valor: ') )

m = (a + b + c + d) / 4
print(f'A média aritmética é: {m: .1f}')
