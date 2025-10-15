i = 1
soma = 0
pos = 0
neg = 0

n = int(input('Digite a quantidade de números que serão digitados: '))

while(n <=0 or n>20):
    print('A quantiade deverá ser entre 1 e 20')

while(i <= n):
    num = int(input('Digite um número: '))
    if (i == 1):
        maior = num
        menor = num


    soma += num


    if (num > maior):
        maior = num


    if (num < menor):
        menor = num


    if (num >= 0):
        pos += 1
    else:
        neg += 1
   
    i+=1


media = soma / n
per_neg = (neg * 100) / n
per_pos = (pos * 100) / n


print(f'O maior número: {maior}')
print(f'O menor número: {menor}')
print(f'A soma dos números: {soma}')
print(f'A média dos números: {media:.2f}')
print(f'Percentual negativos: {per_neg:.1f}%')
print(f'Percentual positivos: {per_pos:.1f}%')