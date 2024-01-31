def calculadora():
    while True:
        # Mostrar as opções
        print("\nOperações disponíveis:")
        print("1: Soma")
        print("2: Subtração")
        print("3: Multiplicação")
        print("4: Divisão")
        print("0: Sair")

        # Solicitar a escolha do usuário
        escolha = input("Digite o número para a operação correspondente: ")

        # Verificar a escolha do usuário
        if escolha == '0':
            print("Saindo da calculadora. Até logo!")
            break
        elif escolha in ('1', '2', '3', '4'):
            # Solicitar os valores
            try:
                num1 = float(input("Digite o primeiro valor: "))
                num2 = float(input("Digite o segundo valor: "))
            except ValueError:
                print("Por favor, insira valores numéricos válidos.")
                continue

            # Executar a operação
            if escolha == '1':
                resultado = num1 + num2
                print(f"Resultado da soma: {resultado}")
            elif escolha == '2':
                resultado = num1 - num2
                print(f"Resultado da subtração: {resultado}")
            elif escolha == '3':
                resultado = num1 * num2
                print(f"Resultado da multiplicação: {resultado}")
            elif escolha == '4':
                if num2 != 0:
                    resultado = num1 / num2
                    print(f"Resultado da divisão: {resultado}")
                else:
                    print("Erro: Divisão por zero.")

        else:
            print("Essa opção não existe. Por favor, escolha uma opção válida.")

if __name__ == "__main__":
    calculadora()
