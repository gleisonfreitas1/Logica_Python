#Escreva um algoritmo para ler o número total de eleitores de um município,
#o número de votos brancos, nulos e válidos. Calcular e escrever o percentual
#que cada um representa em relação ao total de eleitores.

totalEleitores= int(input("Digite o numero total de eleitores: "))
Brancos= int(input("Digite o numero total de votos brancos: "))
Nulos=  int(input("Digite o numero total de votos nulos: "))
Validos= totalEleitores-Brancos-Nulos
#Validos= int(input("Digite o numero total de votos validos: "))

votosValidos= Validos/totalEleitores*100
votos_nulos= Nulos/totalEleitores*100
VotosBrancos= Brancos/totalEleitores*100

print("O numero total de eleitores foi: ",totalEleitores)
print("O percentual de votos Validos é: ",votosValidos,"%")
print("O percentual de votos Brancos é: ",votosBrancos,"%")
print("O percentual de votos Nulos é: ",votosNulos,"%")