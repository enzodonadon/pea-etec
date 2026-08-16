estoque = int(input("Estoque atual: "))
estoque_max = int(input("Estoque máximo: "))
estoque_min = int(input("Estoque mínimo: "))

media = (estoque_max + estoque_min) / 2

if estoque >= media:
    print("Não efetuar compra.")
else:
    print("Efetuar compra.")