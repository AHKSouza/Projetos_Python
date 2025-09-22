# Entrar com dois valores quaisquer. Exibir o maior deles, se existir, caso contrário, enviar mensagem avisando que os números são idênticos.

a = int(input("Digite o primeiro valor: "))
b = int(input("Digite o segundo valor: "))

if (a == b):
    print("Os números são iguais")

elif (a > b):
    print(f"O maior valor é o {a}")

else:
    print(f"O maior valor é o {b}")
