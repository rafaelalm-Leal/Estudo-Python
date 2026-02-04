"""Programa que:
1. Pede ao usuário uma idade
2. Se a idade for menor que 0 -> lançar uma exceção personalizada chamada IdadeInvalidaError
3. Se for válida -> mostrar mensagem confirmando
4. Tratar o erro com try/except"""

class IdadeInvalidaError(Exception):
    pass
try:
    idade = int(input("Digite sua idade: "))
    if idade <= 0:
        raise IdadeInvalidaError("Sua idade não pode ser menor ou igual a 0")
    print("Idade válida!")
    
except IdadeInvalidaError as erro:
    print(f"Erro: {erro}")

except ValueError:
    print("Digite apenas números")

finally:
    print("Programa encerrado")
