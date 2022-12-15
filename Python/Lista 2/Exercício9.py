valorDivida= float(input("Informe o valor da suas parcelas : "))

taxa= float(input("Informe a taxa de juros por atraso: "))

tempo= int(input("Informe a quantidade de parcelas atrasadas: "))

parcelas= valorDivida+((valorDivida*taxa/100)*tempo)

print("o valor da suas parcelas apos a negociação é: R$",parcelas)