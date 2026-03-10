# Provavelmente a mais conhecida instrução de controle de fluxo é o if. 

# Por exemplo:

x = int(input("Please enter an integer: "))
#Console: Please enter an integer: 42

if x < 0:
    x = 0
    print('Negative changed to zero')
elif x == 0:
    print('Zero')
elif x == 1:
    print('Single')
else:
    print('More')

# Pode haver zero ou mais partes elif, e a parte else é opcional. 
# A palavra-chave ‘elif’ é uma abreviação para ‘else if’, e é útil 
# para evitar indentação excessiva. Uma sequência if … elif … elif … 
# substitui as instruções switch ou case, encontrados em outras linguagens.