# Entrar via teclado com o valor da cotação do dólar e uma certa quantidade de dólares. Calcular e exibir o valor correspondente em Reais (R$).

c = float(input('Digite o valor da cotação do dólar: '))
d = float(input('Digite a quantidade de dólares: '))

r = c * d
print(f'O valor convertido em Reais é R$ {r:.2f}')
