# ==============================================================================
# PROVA PRÁTICA AV2 - 3º BIMESTRE
# ARQUIVO: av2_sistema_modular.py
# Nome do Aluno: Lara e Luighi
# Data: 18/09/2026
# Link do Repositório:
# ==============================================================================

# Lista com os dados dos funcionários
dados_brutos = [
    "  carlos eduardo silva;desenvolvedor;11988887777  ",
    "  ana paula mendes;analista de rh;21977776666  ",
    "  roberto carlos oliveira;gerente de projetos;31966665555  "
]

def limpar_e_formatar_texto(texto):
    # Tira os espaços e coloca tudo em maiúsculo
    texto = texto.strip()
    texto = texto.upper()

    return texto


def extrair_codigo_ou_ddd(dado):
    # Tira os espaços do telefone
    dado = dado.strip()

    # Pega os dois primeiros números
    codigo = dado[0:2]

    return codigo


def processar_e_exibir_cadastros(lista_dados):
    total = 0

    # Percorre os dados da lista
    for dado in lista_dados:

        # Separa os dados pelo ;
        partes = dado.split(";")

        nome = limpar_e_formatar_texto(partes[0])
        cargo = limpar_e_formatar_texto(partes[1])
        telefone = partes[2].strip()

        # Pega o DDD
        ddd = extrair_codigo_ou_ddd(telefone)

        # Mostra os dados
        print("Nome:", nome)
        print("Cargo:", cargo)
        print(f"DDD: {ddd}")
        print(f"Telefone: {telefone}")
        print("------------------------------")

        total = total + 1

    return total

def main():
    print("==================================================")
    print("       SISTEMA DE GESTÃO MODULARIZADO - AV2")
    print("==================================================")
    print()

    print("Iniciando o processamento dos dados...")
    print()

    # Chama a função para processar os cadastros
    total_processado = processar_e_exibir_cadastros(dados_brutos)

    # Mostra o total de cadastros
    print(f"Total de registros processados: {total_processado}")

    print()
    print("==================================================")
    print("             PROCESSAMENTO CONCLUÍDO")
    print("==================================================")


# Executa o programa
if __name__ == "__main__":
    main()
