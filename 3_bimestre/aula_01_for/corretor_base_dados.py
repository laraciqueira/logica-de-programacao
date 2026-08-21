dados_brutos = [
    "  JOAO@EMAIL.COM  ",
    " 000.111.222-33 ",
    " Rua das Flores, No 123 ",
    " MARIA@EXEMPLO.COM ",
    " 111.222.333-44 "
]

dados_limpos = []

for item in dados_brutos:

    # 1. Remover espaços no início e no final
    item = item.strip()

    # 2. Padronizar e-mails
    if "@" in item:
        item = item.lower()

    # 3. Padronizar endereços
    if "No" in item:
        item = item.replace("No", "Número")

    # 4. Limpar CPF formatado
    if len(item) == 14 and item[3] == "." and item[7] == "." and item[11] == "-":
        item = item.replace(".", "").replace("-", "")

    # 5. Armazenar na nova lista
    dados_limpos.append(item)

print(dados_limpos)
