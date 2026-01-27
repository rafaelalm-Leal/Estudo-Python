# Desafio Classificador de nível de Herói

print ("Vamos classificar o nível do seu herói!")

#Add informações do herói

print ("Adicione as informações do seu herói")

nome = input("Digite o nome do seu herói: ")

xp = int(input("Digite a quantidade de XP que seu herói possuí atualmente: "))

#Cálculos de XP

nivel = ""

if xp<=1000:
    nivel = "Ferro" 
elif 1001<=xp<=2000:
    nivel = "Bronze"
elif 2001<=xp<=5000:
    nivel = "Prata" 
elif 5001<=xp<=7000:
    nivel = "Ouro" 
elif 7001<=xp<=8000:
    nivel = "Platina" 
elif 8001<=xp<=9000:
    nivel = "Ascendente" 
elif 9001<=xp<=10000:
    nivel = "Imortal" 
else:
    nivel = "Radiante"

#Cálculo final do nível

print(f"O herói de nome {nome} está no nível {nivel}")