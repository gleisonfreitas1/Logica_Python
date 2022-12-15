quantidadeM = int(input("Quantas maças o senhor vai querer? "))

if quantidadeM > 12:
    print("o preço é R$",round(quantidadeM,2))
else:
    preco = quantidadeM * 1.30
    print("O preço é R$",round(preco,2));
