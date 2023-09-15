import os

os.system("cls")

#declaração das variáveis
diferenca = 0
k = 0

print("\nNome: Vitor Pozzebon Scalari")
print("RA: 12224719")
print("Curso: Ciências da Computação - Quinto Semestre - 2023")

#input dos dados pelo usuário
erro = float(input("\nDigite o valor do erro: "))
x01 = float(input("Digite o valor de x01: "))
x02 = float(input("Digite o valor de x02: "))

#estrutura de repetição para realizar o cálculo
while diferenca > erro or diferenca == 0:

    print("\nPara k = ", k)

    #cálculo par os novos valores de "x"
    x1 = (1 + (x02))/2
    print("\nx1 = (1 + (", format(x02, ".4f"),"))/2 = ", format(x1, ".4f"))
    x2 = (3 - (x1))/2
    print("x2 = (3 - (", format(x1, ".4f"),"))/2 = ", format(x2, ".4f"))

    #cálculo do módulo entre as diferenças
    max1 = abs(x1 - x01)
    print("\n|MAX 1| = ", format(max1, ".4f"))
    max2 = abs(x2 - x02)
    print("|MAX 2| = ", format(max2, ".4f"))

    #verificação dos valores máximos
    maxValorDif = max(max1, max2)
    print("\nMáximo valor da diferença: ", format(maxValorDif, ".4f"))
    maxValorAt = max(x1, x2)
    print("Máximo valor das variáveis novas: ", format(maxValorAt, ".4f"))

    #cálculo da diferença entre os valores encontrados
    diferenca = maxValorDif/maxValorAt
    print("\nValor da diferença entre esses valores: ", format(diferenca, ".4f"))

    #verificação da continuação do cálculo
    if diferenca > erro:
        print("\nDiferença maior que o erro. Devemos continuar")
        x01 = x1
        x02 = x2
        k += 1
    else:
        print("\nDiferença menor que o erro. Encontramos o ponto de parada em k = ", k)
        break
    print("=================================================================================================")
