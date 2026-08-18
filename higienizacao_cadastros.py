# Prática no Laboratório I - Higienização de Cadastros


# EXERCÍCIO 1 - Padronização de nome e e-mail

print("=== EXERCÍCIO 1: NOME E E-MAIL ===")

nome = input("Digite o nome completo: ")
email = input("Digite o e-mail: ")

nome_higienizado = nome.strip().upper()
email_higienizado = email.strip().lower()

print(f"Nome higienizado: {nome_higienizado}")
print(f"E-mail higienizado: {email_higienizado}")


# EXERCÍCIO 2 - Limpeza de CPF e telefone

print("\n=== EXERCÍCIO 2: CPF E TELEFONE ===")

cpf = input("Digite o CPF: ")
telefone = input("Digite o telefone: ")

cpf_limpo = (
    cpf.strip()
    .replace(".", "")
    .replace("-", "")
    .replace("(", "")
    .replace(")", "")
    .replace(" ", "")
)

telefone_limpo = (
    telefone.strip()
    .replace(".", "")
    .replace("-", "")
    .replace("(", "")
    .replace(")", "")
    .replace(" ", "")
)

print(f"CPF limpo: {cpf_limpo}")
print(f"Telefone limpo: {telefone_limpo}")


# EXERCÍCIO 3 - Padronização de SKU / Código de estoque

print("\n=== EXERCÍCIO 3: CÓDIGO DE ESTOQUE ===")

codigo = input("Digite o código do produto: ")

codigo_formatado = codigo.strip().upper().replace("-", "_")

print(f"Código formatado: {codigo_formatado}")
