# Verificar se três valores quaisquer (A, B, C) que serão digitados formam ou não um triângulo retângulo. Um triângulo retângulo é formado por uma hipotenusa (A) e dois catetos (B e C). Lembre-se que o quadrado da hipotenusa é igual a soma dos quadrados dos catetos para formar um triângulo retângulo.

a = int(input('Digite o primeiro lado do triângulo:'))
b = int(input('Digite o segundo lado do triâgulo: '))
c = int(input('Digite o terceiro lado do triângulo: '))

if ( (a * a) == ((b * b) + (c * c) )):
    print('É um triângulo retângulo')

else:
    print('Não é um triângulo retângulo')
    