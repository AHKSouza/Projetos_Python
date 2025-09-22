#A partir de três valores que serão digitados, verificar se formam ou não um triângulo. Em caso positivo, exibir sua classificação: “Isósceles, escaleno ou eqüilátero”. Um triângulo escaleno possui todos os lados diferentes, o isósceles, dois lados iguais e o eqüilátero, todos os lados iguais. Para existir triângulo é necessário que a soma de dois lados quaisquer seja maior que o outro, isto, para os três lados.


a = int(input("Digite o primeiro triângulo: "))
b = int(input("Digite o segundo triângulo: "))
c = int(input("Digite o terceiro triângulo: ")) 

if ( (a+b)>c or (a+c)>b or (b+c)>a ):
   
   if ( a!=b and a!=c and b!=c):
      print("Triângulo escaleno")
   elif ( a==b and a==c and b==c):
      print("Triângulo Equilatero")
   else:
      print("Triângulo Isósceles")

else:
   print("Não é um trinângulo")
