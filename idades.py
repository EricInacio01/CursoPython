soma_idades = 0
contagem_idades = 0

while True:
   idade = int(input("Insira a idade: "))

   if idade < 0:
       break
   
   soma_idades += idade
   contagem_idades += 1

idade_media = soma_idades / contagem_idades
print("{:.2f}".format(idade_media))
