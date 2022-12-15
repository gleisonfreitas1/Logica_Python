cotacao = float(input("Informe a cotação do dolar: "))
real = float(input("Quantos reais você quer comprar? "))

convercao = real / cotacao

print("Você precisa de U$",round(convercao,2)," para comprar R$",round(real))