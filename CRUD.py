#         0   1   2   3
lista = [10, 20, 30, 40] # Criar
# lista[2] = 300 # Alterar
# del lista[2] # Deletar
# print(lista)
# print(lista[2])
# Trabalhar só no fim deletando um índice da lista
lista.append(50) # Adiciona 50 no fim da lista
lista.pop() # Remove o último número que adicionei, no caso aqui seria o 50
lista.append(60) # Adiciona 60 no fim da lista
lista.append(70) # Adiciona 70 no fim da lista
ultimo_valor = lista.pop(3) 
print(lista, 'Valor removido:', ultimo_valor)
