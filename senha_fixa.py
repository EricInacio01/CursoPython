# A senha correta é 2002
senha_correta = 2002

while True:
   # Solicitar ao usuário que insira a senha
   senha = int(input("Insira a senha: "))

   # Verificar se a senha é a senha correta
   if senha == senha_correta:
       print("Acesso Permitido")
       break
   else:
       print("Senha Invalida")
