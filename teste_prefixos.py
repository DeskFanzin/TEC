teste = 'isso é uma string | opa | aqui | tenho que retirar apenas o aqui da string | aaa|'
teste = teste.split('|')
print(teste[2])


prefixos = []
with open('01102002.txt', 'r') as f:
   #enquanto tiver linhas no arquivo, faça
   while True:
      tudo = f.readline()
      prefixos_puros = tudo.split('|')
      try:
         prefixos.append(prefixos_puros[2])
      except IndexError:
         break
      if not tudo:
         break

#separe os prefixos
prefixos_unicos = []
for prefixo in prefixos:
   prefixo = prefixo.split()
   for item in prefixo:
      prefixos_unicos.append(item)

   
#mostre apenas os prefixos únicos
prefixos_unicos = set(prefixos_unicos)
prefixos_unicos = list(prefixos_unicos)
with open('prefixos_unicos.txt', 'w') as f:
   for prefixo in prefixos_unicos:
      f.write(prefixo + '\n')