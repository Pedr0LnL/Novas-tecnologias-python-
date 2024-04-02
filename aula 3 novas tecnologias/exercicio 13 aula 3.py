# Lista de pedidos de sanduíches
sandwich_orders = ['atum', 'frango', 'queijo', 'presunto']

# Lista de sanduíches prontos
finished_sandwiches = []

# Preparando os sanduíches
for pedido in sandwich_orders:
    print("Preparando seu sanduíche de", pedido + ".")
    # Transferindo o sanduíche preparado para a lista de sanduíches prontos
    finished_sandwiches.append(pedido)

# Mostrando os sanduíches preparados
print("\nSanduíches preparados:")
for sanduiche in finished_sandwiches:
    print("- " + sanduiche)
