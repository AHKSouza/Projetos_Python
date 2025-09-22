# A partir dos valores da base e altura de um triângulo, calcular e exibir sua área. Fórmula: (b * a) / 2

b = float(input('Digite a base do triângulo:'))
a = float(input('Digite a altura do triângulo:'))

area = (b * a) / 2
print(f'A área do triângulo é : {area:.2f}, pois a base é {b:.2f} e a altura é {a:.2f}')
