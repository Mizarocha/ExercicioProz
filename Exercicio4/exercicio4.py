import datetime

def calcular_idade(ano_nascimento):
    ano_atual = datetime.datetime.now().year
    idade = ano_atual - ano_nascimento
    return idade

def obter_ano_nascimento():
    while True:
        try:
            ano_nascimento = int(input("Digite o ano de nascimento (entre 1922 e 2022): "))
            if 1922 <= ano_nascimento <= 2021:
                return ano_nascimento
            else:
                print("Ano de nascimento fora do intervalo válido. Tente novamente.")
        except ValueError:
            print("Por favor, insira um valor numérico válido para o ano de nascimento.")

if __name__ == "__main__":
    nome_completo = input("Digite seu nome completo: ")
    
    ano_nascimento = obter_ano_nascimento()
    
    idade = calcular_idade(ano_nascimento)
    
    print(f"\nOlá, {nome_completo}!")
    print(f"No ano de 2024, você completou ou completará {idade} anos.")