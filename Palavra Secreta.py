import os
os.system('cls') # Limpa minha tela (funcionalidade do Windows).

palavra_secreta = 'cachorro' 
letras_acertadas = '' # Start do 0.
numero_tentativas = 0

while True:
    letra_digitada = input('Digite uma letra: ') 
    numero_tentativas += 1 # A cada letra 1 tentativa será computada.

    if len(letra_digitada) > 1: # Regrinha para impossibilitar o usuário de digitar mais que uma letra.
        print('Digite apenas uma letra.')

    elif len(letra_digitada) < 1: # Regrinha para impossibilitar o usuário de digitar menos que uma letra.
        print('Digite alguma tentativa.')

    elif letra_digitada == ' ': # Regrinha para impossibilitar o usuário de digitar espaço.
        print('Espaço não é uma tentativa.')
        
    elif not letra_digitada.isalpha(): # Regrinha para impossibilitar o usuário de digitar números.
        print('Digite SOMENTE LETRAS.')
        
        continue

    if letra_digitada in palavra_secreta:
        letras_acertadas += letra_digitada # Somará a letra digitada na letra acertada, verificando se acertou uma letra.

    palavra_formada = '' # Variável nova para a palavra formada.
    for letra_secreta in palavra_secreta: # Para uma letra secreta dentro da palavra secreta.
        if letra_secreta in letras_acertadas: # Somente se letra secreta estiver em letras acertadas.
            palavra_formada += letra_secreta # Adicionará a variável palavra formada em letra secreta.
        else:
            palavra_formada += '*' # Se não acertada nenhuma letra, exibirá o tamanho da nossa palavra secreta com '*'.

    print(f'Palavra formada: {palavra_formada}') # Imprimirá a Palavra formada, do jeito que ela estiver (com asterisco ou com a letra acertada).

    if palavra_formada == palavra_secreta: # Se a palavra formada for igual a palavra secreta...
        print('Acertô Mizeravi!!!') # Você ganha.
        print(f'A palavra era: {palavra_secreta}') # Dirá a palavra.
        print(f'Você precisou de: {numero_tentativas} tentativas para acertar.') # Dirá o quanto de tentativas você precisou para acertar.
        break
            
