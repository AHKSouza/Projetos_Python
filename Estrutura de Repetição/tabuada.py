print('Tabuada While')

num = int(input('Digite um número para ver a tabuada: '))
while (num <= 0):
    print('Número negativo!')
    num = int(input('Digite um ou númeor para obter a tabuada: '))
i = 1

while (i < 11):
        r = num * i
        print(f'{num} x {i} = {r}')
        i = i +1
              

