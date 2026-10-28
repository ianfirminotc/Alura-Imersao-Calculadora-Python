# 1. Definição das funções matemáticas
def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Erro: Não é possível dividir por zero!"
    return a / b

# 2. Menu de opções
print("=== CALCULADORA SIMPLES ===")
print("Escolha a operação:")
print("1 - Adição (+)")
print("2 - Subtração (-)")
print("3 - Multiplicação (*)")
print("4 - Divisão (/)")

# 3. Entrada de dados do usuário
opcao = input("Digite o número da operação (1/2/3/4): ")

# Verifica se a opção digitada é válida antes de pedir os números
if opcao in ('1', '2', '3', '4'):
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    # 4. Estrutura de decisão para calcular o resultado
    if opcao == '1':
        resultado = somar(num1, num2)
        print(f"Resultado: {num1} + {num2} = {resultado}")

    elif opcao == '2':
        resultado = subtrair(num1, num2)
        print(f"Resultado: {num1} - {num2} = {resultado}")

    elif opcao == '3':
        resultado = multiplicar(num1, num2)
        print(f"Resultado: {num1} * {num2} = {resultado}")

    elif opcao == '4':
        resultado = dividir(num1, num2)
        print(f"Resultado: {num1} / {num2} = {resultado}")

else:
    print("Opção inválida! Por favor, escolha um número de 1 a 4.")