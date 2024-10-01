# Crie um programa que receba um número inteiro e calcule o fatorial desse número usando uma estrutura de repetição.

numero = int(input("Digite um número "))
if numero < 0:
    print("sem fatorial para numeros negativos")
else:
    fatorial = 1
    n = 1
    while n <= numero:
        fatorial *= n
        n += 1
    print(f"O fatorial de {numero} é {fatorial}")