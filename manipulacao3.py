pedidos = ['Mesa 3 - Bitoque', 'Mesa 7 - Bacalhau à Brás', 'Mesa 1 - Francesinha', 'Mesa 5 - Polvo à Lagareiro']
pedido_atual = pedidos.pop(0)
print(f"A preparar: {pedido_atual}")
pedido_cancelado = "Mesa 7 - Bacalhau à Brás"
pedidos.remove("Mesa 7 - Bacalhau à Brás")
print(f"Cancelado: {pedido_cancelado}")
pedidos.insert(0,"Mesa 2 - Arroz de Marisco (URGENTE)")
print(f"Numero de pedidos na fila: {len(pedidos)}")
print(', '.join(pedidos))

