"""O programa deve:
1- Pedir uma frase ao usuário
2- Salvar essa frase em um arquivo chamado anotacoes.txt
3- Depois, ler o arquivo e mostrar todas as frases salvas"""

with open("anotacoes.txt", "a") as arquivo:
    arquivo.write(input("Digite sua anotação: ") + "\n")

print("\nAnotações salvas:")

with open("anotacoes.txt", "r") as arquivo:
    for linha in arquivo:
        print(linha.strip())