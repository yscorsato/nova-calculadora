while True:
    print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')
    print('Yasmin Scosato')
    print('1 para soma')
    print('2 para subtração')
    print('3 para divisão')
    print('4 para multiplicação')
    print('5 para Sair do sistema')
    print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-')

    try:
        n = int(input('Escolha a operação: '))
    except ValueError:
        print("Por favor, digite um número válido para a operação.")
        continue


    if n == 1:
        print('Vamos somar')
        try:
            n1 = int(input('Número 1: '))
            n2 = int(input('Número 2: '))
        except ValueError:
            print("Erro: Por favor, digite apenas números.")
            continue
        r = n1 + n2
        print(f'Resultado: {r}')

    elif n == 2:
        print('Vamos subtrair')
        try:
            n1 = int(input('Número 1: '))
            n2 = int(input('Número 2: '))
        except ValueError:
            print("Erro: Por favor, digite apenas números.")
            continue
        r = n1 - n2
        print(f'Resultado: {r}')

    elif n == 3:
        print('Vamos dividir')
        try:
            n1 = float(input('Número 1: '))
            while True:
                n2 = int(input('Número 2: '))
                if n2 != 0:
                    break  # ao brecar o laço de repetição ele sai do laço
                else:
                    print("Não é possível dividir por zero. Tente novamente.")
        except ValueError:
            print("Erro: Por favor, digite apenas números.")
            continue

        r = n1 / n2
        print(f'Resultado: {n1} / {n2} = {r}')

    elif n == 4:
        print('Vamos multiplicar')
        try:
            n1 = int(input('Número 1: '))
            n2 = int(input('Número 2: '))
        except ValueError:
            print("Erro: Por favor, digite apenas números.")
            continue
        r = n1 * n2
        print(f'Resultado: {r}')

    elif n == 5:
        print('Fim')
        break
    else:
        print("Opção inválida. Tente novamente.")