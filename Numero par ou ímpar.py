digite_um_numero = input('Digite um número: ')

if digite_um_numero.isdigit(): # verifica se o usuário digitou um número
    numero = int(digite_um_numero)
    print(f'Seu número é {numero}.')
    if (numero % 2 == 0): # verifica se é par
        print(f'Seu número {numero} é par.')
    else:
        print(f'Seu número {numero} é ímpar.')
else:
    print('Você não digitou um número.')
