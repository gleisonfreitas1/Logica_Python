salarioFixo = float(input("digite seu salario fixo: "))
valorVendas = float(input("digite a quantidade de vendas: "))

if valorVendas <= 1500:
    comi = (valorVendas*3/100)
    salarioFinal = salarioFixo + comi
    print("Seu salario final é: ",salarioFinal)
else:
    comi =   valorVendas - 1500
    comi = (comi*5/100)+(1500*3/100)
    salarioFinal = salarioFixo + comi
    print("Seu salario final é: ",salarioFinal);
