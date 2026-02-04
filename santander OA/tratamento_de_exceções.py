try:
    num = int(input("Digite um número para calcular o seu dobro: "))
    dobro = num * 2
    print(f"O dobro do seu número é {dobro}")
except ValueError:
    print("Você digitou algo inválido!")

finally:
    print("O programa terminou")