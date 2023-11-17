###################################
#      RETIRANDO INFORMAÇÕES      #
###################################
enderecos_ip = []
with open('01102002.txt', 'r') as f:
   #enquanto tiver linhas no arquivo, faça
   while True:
      tudo = f.readline()
      enderecos_puros = tudo.split('|')
      try:
         enderecos_ip.append(enderecos_puros[3])
      except IndexError:
         break
      if not tudo:
         break

#separe em endereços únicos
enderecos_unicos = []
for endereco in enderecos_ip:
   endereco = endereco.split()
   for item in endereco:
      enderecos_unicos.append(item)

#mostre apenas os endereços únicos
enderecos_unicos = set(enderecos_unicos)
enderecos_unicos = list(enderecos_unicos)

with open('enderecos_unicos.txt', 'w') as f:
    for endereco in enderecos_unicos:
        f.write(endereco + '\n')

#separe em endereços ipv6 e ipv4
ipv4 = []
ipv6 = []
for endereco in enderecos_unicos:
    if '.' in endereco:
        ipv4.append(endereco)
    else:
        ipv6.append(endereco)

with open('ipv4.txt', 'w') as f:
    for endereco in ipv4:
        f.write(endereco + '\n')

with open('ipv6.txt', 'w') as f:
    for endereco in ipv6:
        f.write(endereco + '\n')
        