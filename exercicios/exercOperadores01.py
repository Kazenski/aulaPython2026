# --- DADOS DE ENTRADA ---
valor_compra = 600.00 # eu ainda posso solicitar que ele digite esse valor 
#valor_compra = float(input("Digite o valor da compra com o separador de centavos em '.' (ponto): ')
e_vip = False
conta_bloqueada = False
lista_categorias = ["eletronicos", "perifericos"]

# 1. Operador de Atribuição e Aritmética
# Aplicar taxa de envio de 5% sobre o valor da compra
taxa_envio = valor_compra * 0.05 #taxa_envio = (valor_compra * 5) / 100
total_bruto = valor_compra + taxa_envio

# 2. Operadores de Comparação, Lógicos e Membro
# Regra: Ganha desconto se (Compra > 500 ou for VIP) E (não estiver bloqueado)
# Também vamos checar se "eletronicos" está na lista de categorias
tem_desconto = (valor_compra > 500 or e_vip) and not conta_bloqueada
contem_eletronico = "eletronicos" in lista_categorias

# 3. Operador de Atribuição Composta e Identidade
desconto_aplicado = 0
if tem_desconto:
    desconto_aplicado = 50.00
    total_bruto -= desconto_aplicado # Atribuição composta

# Checando se os valores apontam para o mesmo custo inicial (Identidade)
original = valor_compra
copia = original
mesma_referencia = copia is original

# --- IMPRESSÃO ESPECÍFICA (O seu desafio) ---
# Use f-strings para imprimir o relatório abaixo exatamente assim:

print("-" * 30)
print(f"{'RELATÓRIO DE VENDA':^30}")
print("-" * 30)
print(f"Subtotal:      R$ {valor_compra:>8.2f}")
print(f"Taxa Envio:    R$ {taxa_envio:>8.2f}")
print(f"Desconto:      R$ {desconto_aplicado:>8.2f}")
print(f"Total Final:   R$ {total_bruto:>8.2f}")
print("-" * 30)
print(f"Status Desconto: {tem_desconto}")
print(f"Eletrônico detectado: {contem_eletronico}")
print(f"Referência íntegra: {mesma_referencia}")

#Impressão deste formato:

# ------------------------------
#       RELATÓRIO DE VENDA      
# ------------------------------
# Subtotal:      R$   600.00
# Taxa Envio:    R$    30.00
# Desconto:      R$    50.00
# Total Final:   R$   580.00
# ------------------------------
# Status Desconto: True
# Eletrônico detectado: True
# Referência íntegra: True

# Por que ficou assim? (Análise da "mágica")
# Para que você possa replicar essa estética no seu site, veja o que cada 
# símbolo fez:

# ^30: Pegou o texto "RELATÓRIO DE VENDA" e o centralizou em um espaço 
# de 30 caracteres.

# >8.2f:

# O >8 empurrou o número para a direita, garantindo que ele ocupe sempre 
# 8 espaços (criando aquele alinhamento vertical perfeito das vírgulas).

# O .2f forçou duas casas decimais, transformando 600 em 600.00.

# "-" * 30: Usou o operador aritmético de multiplicação para criar uma 
# linha divisória de exatos 30 traços, combinando com a largura do cabeçalho.


























# -------------------------------------------------------------------------
# --- DADOS DE ENTRADA ---

valor_compra = float(input("Digite o valor da compra com o separador de centavos em '.' (ponto): '"))
original = valor_compra
e_vip = False
conta_bloqueada = False
localFazemosEntrega = ["São José", "Campinas", "Palhoça"] 
localizacaoCliente = input("Insira o local da entrega: ")
taxa_envio = 0
total_bruto = 0
taxa_envio = 0
contasAtivas = ["Kazenski", "Murilo", "Jonathan", "Pedro", "Janete", "Juliana", "Samanta", "Roberta", "Ingrid"]
desconto_aplicado = 0
valorCompraMenor = False
clientesVip = ["Kazenski", "Murilo", "Juliana", "Ingrid"]

# -------------------------------------------------------------------------
# --- PROCESSAMENTO ---

# Aplicar taxa de envio
if (localizacaoCliente in localFazemosEntrega):
    taxa_envio = valor_compra * 0.05 # 5% -- taxa_envio = (valor_compra * 5) / 100
else:
    taxa_envio = valor_compra * 0.15 # 15% -- taxa_envio = (valor_compra * 15) / 100


# Ganha desconto se (Compra > 500 ou for VIP) E (não estiver bloqueado)
tem_desconto = (valor_compra > 500 or e_vip) and not conta_bloqueada


# Valor do desconto
if tem_desconto:
    desconto_aplicado = 50.00
    total_bruto -= desconto_aplicado # Atribuição composta

# Checando se os valores de compra mudaram ou não
if(original > total_bruto):
    valorCompraMenor = True

#calculando o total bruto da compra
total_bruto = valor_compra + taxa_envio

# -------------------------------------------------------------------------
# --- SAIDAS ---

# Use f-strings para imprimir o relatório abaixo exatamente assim:

print("-" * 30)
print(f"{'RELATÓRIO DE VENDA':^30}")
print("-" * 30)
print(f"Subtotal:      R$ {valor_compra:>8.2f}")
print(f"Taxa Envio:    R$ {taxa_envio:>8.2f}")
print(f"Desconto:      R$ {desconto_aplicado:>8.2f}")
print(f"Total Final:   R$ {total_bruto:>8.2f}")
print("-" * 30)
print(f"Status Desconto: {tem_desconto}")



# -------------------------------------------------------------------------
# --- FIM ---












#Impressão deste formato:

# ------------------------------
#       RELATÓRIO DE VENDA      
# ------------------------------
# Subtotal:      R$   600.00
# Taxa Envio:    R$    30.00
# Desconto:      R$    50.00
# Total Final:   R$   580.00
# ------------------------------
# Status Desconto: True
# Eletrônico detectado: True
# Referência íntegra: True

# Por que ficou assim? (Análise da "mágica")
# Para que você possa replicar essa estética no seu site, veja o que cada 
# símbolo fez:

# ^30: Pegou o texto "RELATÓRIO DE VENDA" e o centralizou em um espaço 
# de 30 caracteres.

# >8.2f:

# O >8 empurrou o número para a direita, garantindo que ele ocupe sempre 
# 8 espaços (criando aquele alinhamento vertical perfeito das vírgulas).

# O .2f forçou duas casas decimais, transformando 600 em 600.00.

# "-" * 30: Usou o operador aritmético de multiplicação para criar uma 
# linha divisória de exatos 30 traços, combinando com a largura do cabeçalho.
