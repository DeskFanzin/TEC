teste = 'isso é uma string | opa | aqui | tenho que retirar apenas o aqui da string | aaa|'
teste = teste.split('|')
print(teste[2])

###################################
#      RETIRANDO INFORMAÇÕES      #
###################################
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

#faça a mesma coisa para o outro arquivo
prefixos.clear()
prefixos_unicos.clear()
with open('01102002_2am.txt', 'r') as f:
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

with open('prefixos_unicos2.txt', 'w') as f:
   for prefixo in prefixos_unicos:
      f.write(prefixo + '\n')

###################################
# PRIMEIRA ANÁLISE: ANÁLISE DE AS #
###################################

#primeiro, vamos pegar os prefixos únicos e colocar em uma lista
prefixos_unicos = []
with open('prefixos_unicos.txt', 'r') as f:
   while True:
      tudo = f.readline()
      tudo.replace('\n', '')
      prefixos_unicos.append(tudo)
      if not tudo:
         break

#agora, vamos pegar os prefixos únicos do outro arquivo e colocar em uma lista
prefixos_unicos2 = []
with open('prefixos_unicos2.txt', 'r') as f:
   while True:
      tudo = f.readline()
      tudo.replace('\n', '')
      prefixos_unicos2.append(tudo)
      if not tudo:
         break

#agora, vamos comparar os prefixos únicos e ver quais são iguais e quais são diferentes
prefixos_iguais = []
prefixos_diferentes = []
for prefixo in prefixos_unicos:
   if prefixo in prefixos_unicos2:
      prefixos_iguais.append(prefixo)
   else:
      prefixos_diferentes.append(prefixo)

with open('prefixos_iguais.txt', 'w') as f:
   for prefixo in prefixos_iguais:
      f.write(prefixo)

with open('prefixos_diferentes.txt', 'w') as f:
   for prefixo in prefixos_diferentes:
      f.write(prefixo)