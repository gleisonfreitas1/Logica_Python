contadora = 1
somadora = 0

while (contadora < 501):
    if contadora % 2 == 0:
        somadora = somadora+contadora;
    contadora = contadora + 1;

print ("A soma dos 500 primeiros numeros pares é: ",somadora)