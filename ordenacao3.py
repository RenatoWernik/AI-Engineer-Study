utilizadores = ['Renato', 'Maria', 'João', 'Sofia', 'Pedro', 'Ana']
passos = [8420, 12300, 5600, 15200, 9800, 11500]
print(f"Total de utilizadores: {len(utilizadores)}")
print(f"Ranking(passos): {sorted(passos,reverse=True)}")
print(f"Vencedor: {max(passos)}")
print(f"Último: {min(passos)}")
print(f"Média: {sum(passos)/len(utilizadores)}")

