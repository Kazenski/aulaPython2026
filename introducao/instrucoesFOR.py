# A instrução for em Python é um pouco diferente do que costuma ser 
# em C ou Pascal. Ao invés de sempre iterar sobre uma progressão 
# aritmética de números (como no Pascal), ou permitir ao usuário definir 
# o passo de iteração e a condição de parada (como C), a instrução for 
# do Python itera sobre os itens de qualquer sequência (seja uma lista 
# ou uma string), na ordem que aparecem na sequência. 

# Por exemplo:

words = ['cat', 'window', 'defenestrate']
for w in words:
    print(w, len(w))

# Código que modifica uma coleção sobre a qual está iterando pode ser 
# inseguro. No lugar disso, usualmente você deve iterar sobre uma cópia 
# da coleção ou criar uma nova coleção:

# Strategy:  Iterate over a copy
for user, status in users.copy().items():
    if status == 'inactive':
        del users[user]

# Strategy:  Create a new collection
active_users = {}
for user, status in users.items():
    if status == 'active':
        active_users[user] = status