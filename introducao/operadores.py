#=====================================================================
#0. Operadores Aritméticos e Tipagem

# Exercício 1: Operadores Aritméticos
# Calcule a área de um retângulo usando as variáveis de comprimento e largura.
comprimento = 10
largura = 5
area = comprimento * largura
print(f"Área: {area}")
# PARAMETRO

# Exercício 2: Operadores de Comparação
# Verifique se um número é par usando o operador de resto (módulo) e uma verificação de igualdade.
numero = 14
eh_par = (numero % 2 == 0)
print(f"O número {numero} é par? {eh_par}")

# Exercício 3: Operadores Lógicos
# Determine se uma pessoa está apta a votar (deve ter 18 anos ou mais E ser cidadão).
idade = 20
eh_cidadao = True
pode_votar = idade >= 18 and eh_cidadao
print(f"Pode votar: {pode_votar}")

# Exercício 4: Operadores de Atribuição
# Atualize uma variável de pontuação somando 10 pontos usando um operador de atribuição composta.
pontuacao = 50
pontuacao += 10
print(f"Pontuação Atualizada: {pontuacao}")

# Exercício 5: Operadores de Identidade e Associação
# Verifique se 'maçã' está em uma lista de frutas e se duas variáveis apontam para o mesmo objeto.
frutas = ["maçã", "banana", "cereja"]
tem_maca = "maçã" in frutas

a = [1, 2, 3]
b = a
eh_o_mesmo_objeto = a is b
print(f"Tem maçã: {tem_maca}, Mesmo objeto: {eh_o_mesmo_objeto}")


#=====================================================================
# 1. Operadores Aritméticos e Tipagem

# Operadores Aritméticos
a = 15
b = 4

soma = a + b          # 19 (int)
subtracao = a - b     # 11 (int)
multiplicacao = a * b # 60 (int)
divisao = a / b       # 3.75 (float) -> Sempre retorna float
div_inteira = a // b  # 3 (int) -> Descarta as casas decimais
resto = a % b         # 3 (int) -> Resto da divisão de 15 por 4
potencia = a ** 2     # 225 (int)

print(f"Divisão: {divisao} (Tipo: {type(divisao)})")
print(f"Divisão Inteira: {div_inteira} (Tipo: {type(div_inteira)})")


#=====================================================================
# 2. Mesclagem e Precedência (PEMDAS)
# Python segue a ordem: Parênteses, Expoentes, Multiplicação/Divisão, 
# Adição/Subtração.

# A ordem de execução altera drasticamente o tipo e o valor
expressao_1 = 10 + 5 * 2 ** 3 / 4
# 1. Potência: 2**3 = 8
# 2. Multiplicação: 5 * 8 = 40
# 3. Divisão: 40 / 4 = 10.0
# 4. Adição: 10 + 10.0 = 20.0
print(f"Resultado 1: {expressao_1}")

expressao_2 = (10 + 5) * 2 ** (3 / 4)
print(f"Resultado 2: {expressao_2}")



#=====================================================================
# 3. Operadores de Comparação (Retorno Booleano)
# Utilizados para verificar relações entre valores.

x = 10
y = 20
z = "10"

print(x == 10)    # True
print(x != y)    # True
print(x > y)     # False
print(x <= 10)   # True

# Comparação de tipos diferentes
print(x == z)    # False (um é int, o outro é str)
print(x == int(z)) # True (conversão de tipo para mesclagem correta)



#=====================================================================
# 4. Operadores Lógicos e Atalhos (Short-circuit)
# Mesclando condições com and, or e not.

idade = 25
tem_cnh = True
tem_carro = False

# Operador AND: Todas devem ser True
pode_dirigir = idade >= 18 and tem_cnh
print(f"Pode dirigir? {pode_dirigir}") 

# Operador OR: Pelo menos uma deve ser True
precisa_carona = not tem_carro or not tem_cnh
print(f"Precisa de carona? {precisa_carona}")

# Mesclagem complexa
resultado = (10 > 5) and (not (5 == 5)) or (1 == 1)
# True and (not True) or True -> True and False or True -> False or True -> True
print(f"Resultado lógico: {resultado}")



#=====================================================================
# 5. Operadores de Atribuição Composta
# Forma compacta de atualizar variáveis.

pontos = 100

pontos += 10   # pontos = pontos + 10 (110)
pontos -= 5    # pontos = pontos - 5 (105)
pontos *= 2    # pontos = pontos * 2 (210)
pontos /= 3    # pontos = pontos / 3 (70.0)
pontos %= 4    # pontos = pontos % 4 (2.0)

print(f"Pontos finais: {pontos}")



#=====================================================================
# 6. Operadores de Identidade e Membro
# Específicos para verificar referências de objetos e presença em coleções.

lista_a = [1, 2, 3]
lista_b = [1, 2, 3]
lista_c = lista_a

# is: verifica se ocupam o mesmo lugar na memória (identidade)
print(lista_a is lista_b) # False (conteúdo igual, mas objetos diferentes)
print(lista_a is lista_c) # True (apontam para o mesmo objeto)

# in: verifica se o valor está contido (membro)
print(1 in lista_a)       # True
print(5 not in lista_a)   # True



#=====================================================================
# Lembrete de Precedência
# Para entender como o Python "mescla" esses operadores, lembre-se da ordem de execução:

# Parênteses ()

# Potenciação **

# Multiplicação/Divisão *, /, //, %

# Adição/Subtração +, -

# Comparações ==, >, <, etc.

# Lógicos not, depois and, depois or


#=====================================================================
# Entendendo a Formatação (Prática)
# O Python oferece três formas principais de formatar. A f-string (introduzida no Python 3.6)
# é a mais moderna e eficiente para usar em seus projetos na Hostinger.

# O método .format() (e sua evolução, as f-strings) é essencial para exibir resultados de 
# cálculos e operações de forma legível.

# 1. O método clássico .format()
nome = "Carlos"
print("Olá, {}!".format(nome))

# 2. F-Strings (A mais recomendada e rápida)
produto = "Teclado"
preco = 150.50
print(f"O {produto} custa R${preco:.2f}") # .2f limita a 2 casas decimais

# 3. Alinhamento e Espaçamento
# Útil para criar tabelas simples no console
# print(f"{'Item':<10} | {'Preço':>8}")
# print(f"{'Mouse':<10} | {50.00:>8.2f}")