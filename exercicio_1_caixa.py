quantidade_itens = int(input("Quantidade de itens: "))

total = 0

for i in range(1, quantidade_itens + 1):
    preco = float(input(f"Preço do item {i}: R$ "))
    total += preco

media = total / quantidade_itens

print(f"\nTotal da compra: R$ {total:.2f}")
print(f"Média por item: R$ {media:.2f}")
