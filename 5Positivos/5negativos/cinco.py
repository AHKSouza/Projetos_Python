i = 1
soma = 0
pos = 0
neg = 0

while(i <= 5):
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


media = soma / 5
per_neg = (neg * 100) / 5
per_pos = (pos * 100) / 5


print(f'O maior número: {maior}')
print(f'O menor número: {menor}')
print(f'A soma dos números: {soma}')
print(f'A média dos números: {media:.2f}')
print(f'Percentual negativos: {per_neg:.1f}%')
print(f'Percentual positivos: {per_pos:.1f}%')