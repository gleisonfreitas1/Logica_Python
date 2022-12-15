velocidade= float(input("Digite a velocidade media para essa viagem: "))
print()
tempo= int(input("Digite o tempo medio da viagem: "))
print()
distancia= velocidade*tempo

combustivel= round(distancia/12,2)

print("A quantidade de combustivel gasto é: ",combustivel,"L")