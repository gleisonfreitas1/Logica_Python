#O custo de um carro novo ao consumidor é a soma do custo de fábrica com a porcentagem
#do distribuidor e dos impostos (aplicados ao custo de fábrica). Supondo que o percentual
#do distribuidor seja de 28% e os impostos de 45%, escrever um algoritmo para ler o custo de
#fábrica de um carro, calcular e escrever o custo final ao consumidor.

custoFabrica =float(input("qual o preço de fabricação do carro? "))

custoFinal= custoFabrica*28/100+custoFabrica*45/100
custoFinal= custoFinal+custoFabrica

print("o custo final do carro é: ",custoFinal)

