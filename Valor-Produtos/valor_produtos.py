# Entrar via teclado com o valor de cinco produtos.Após as  entradas, digitar um valor referente ao pagamento da somatória destes valores. Calcular e exibir o troco que deverá ser devolvido.

a = float(input('Digite o valor do primeiro produto: R$'))
b = float(input('Digite o valor do segundo produto: R$'))
c = float(input('Digite o valor do terceiro produto: R$'))
d = float(input('Digite o valor do quarto produto: R$'))
e = float(input('Digite o valor do quinto produto: R$'))
p = float(input('Digite o valor do pagamento: R$'))

x = (a+b+c+d+e)
t = p - x
print(f'O valor total das compras foi R$ {x:.2f} e o valor do pagamento foi R$ {p: .2f}, com isso o valor do troco é R$ {t:.2f}')