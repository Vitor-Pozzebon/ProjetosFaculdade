import os
import matplotlib.pyplot as plt
import numpy as np
import random

import pandas as pd
from pandas import read_csv
from pandas import set_option

os.system("cls")

# CHAVE DE CRIPTOGRAFIA
chavecriptosimetrica2 = [{"A": 29, "B": 49, "C": 58, "D": 72, "E": 13,
                          "F": 28, "G": 48, "H": 57, "I": 71, "J": 12,
                          "K": 27, "L": 47, "M": 56, "N": 70, "O": 11,
                          "P": 26, "Q": 46, "R": 55, "S": 69, "T": 10,
                          "U": 25, "V": 45, "X": 54, "Y": 68, "Z": 9,
                          "W": 24, ".": 44, ",": 53, "!": 67, "?": 8,
                          "$": 23, "#": 43, "%": 52, "*": 66, "+": 7,
                          "-": 22, "/": 42, "0": 51, "1": 65, "2": 6,
                          "3": 21, "4": 41, "5": 50, "6": 64, "7": 5,
                          "8": 20, "9": 35,
                          "a": 19, "b": 34, "c": 40, "d": 63, "e": 4,
                          "f": 18, "g": 33, "h": 39, "i": 62, "j": 3,
                          "k": 17, "l": 32, "m": 38, "n": 61, "o": 2,
                          "p": 16, "q": 31, "r": 37, "s": 60, "t": 1,
                          "u": 15, "v": 30, "x": 36, "y": 59, "z": 0,
                          "w": 14, " ": 73
                          }]

chavedecriptosimetrica2 = ["z", "t", "o", "j", "e", "7", "2", "+", "?", "Z",
                           "T", "O", "J", "E", "w", "u", "p", "k", "f", "a",
                           "8", "3", "-", "$", "W", "U", "P", "K", "F", "A",
                           "v", "q", "l", "g", "b", "9", "x", "r", "m", "h",
                           "c", "4", "/", "#", ",", "V", "Q", "L", "G", "B",
                           "5", "0", "%", ",", "X", "R", "M", "H", "C", "y",
                           "s", "n", "i", "d", "6", "1", "*", "!", "Y", "S",
                           "N", "I", "D", " ", ]

# chave de criptografia (K)
chavecriptomatrix = [[1, 3],
                     [9, 6]]

# chave de decriptografia (K)^-1
chavedecriptomatrix = [[-2 / 7, 1 / 7],
                       [3 / 7, -1 / 21]]

# ------------------------------------------------------------------
# função para multiplicar as matrizes
def multiplicar(chave, cod):
    result = []
    tam = len(chave)
    for lin in range(tam):
        soma = 0
        for col in range(tam):
            soma += chave[lin][col] * cod[col]
        result = result + [int(soma + 0.5)]
    return result

# ------------------------------------------------------------------
# VERIFICAR SE UM NÚMERO É PRIMO
# RETORNA 0 : NÃO PRIMO
# RETORNA 1 : PRIMO
def primo(n):
    if (n == 1):
        return 1
    for i in range(2, n):
        if ((n % i) == 0):
            return 0
    return 1

# ------------------------------------------------------------------
# GERAR NÚMEROS PRIMOS ENTRE: inicio e fim
# RETORNA VETOR COM OS NÚMEROS PRIMOS NO INTERVALO
def gerarPrimo(inicio, fim):
    aux = []
    for i in range(inicio, fim):
        if (primo(i) == 1):
            aux.append(i)
    return aux

# ------------------------------------------------------------------
# Função para gravar a frase no arquivo de frases criptografadas
def gravarCripto(texto1, texto2, texto3):
    # GRAVAR EM ARQUIVO - Frases criptografadas
    f = open('arquivotxt001Cripto.txt', 'w')
    f.writelines(texto1 + "\n")
    f.writelines(texto2 + "\n")
    f.writelines(texto3 + "\n")
    f.close()
    print("Frases criptografadas armazenadas!")
    print("-------------------------------------------------------------------------")

# ------------------------------------------------------------------
# FUNÇÃO PARA GERAR A CRIPTOGRAFIA
def criptografia(frase):
    if (len(frase) % 2 == 1):  # verificar se a frase possui numero impar de letras
        frase = frase + " "

    # vetor criptografado
    cripto = ""

    print("-------------------------------------------------------------------------")
    print("\nCRIPTOGRAFANDO EM HILL...")
    print("FRASE ORIGINAL: ", frase)
    # CONVERSÃO DE CADA LETRA PARA O VALOR DA TABELA DE STRING
    for pos in range(0, len(frase), 2):
        # separar os caracteres da frase dois a dois
        ftoken = frase[pos:pos + 2]
        # montar o valor numérico de cada caractere
        cdtoken = [chavecriptosimetrica2[0][ftoken[0]],
                   chavecriptosimetrica2[0][ftoken[1]]]
        # multiplica o vetor numérico pela matriz de criptografia
        result = multiplicar(chavecriptomatrix, cdtoken)
        print(ftoken, "   ", cdtoken, "   ", result)

        cripto = cripto + format(result[0], "04d")
        cripto = cripto + format(result[1], "04d")
        print(cripto)

    print("\n\nA frase: ", frase)

    print("Criptografada é: ", cripto)

    # --------------------------------------------------------------

    criptoRsa = ""
    cripto2Rsa = []
    print("-------------------------------------------------------------------------")
    print("\nCRIPTOGRAFANDO EM RSA...")

    for i in cripto:
        vl = int(i)
        cp = (vl ** E) % n
        print(vl, "**", E, " = ", vl ** E, "MOD ", n, "= CRIPTO: ", criptoRsa)
        criptoRsa = criptoRsa + str(format(cp, "02d"))
        cripto2Rsa.append(cp)

    print("\nCRIPTOGRAFIA:")
    print(criptoRsa)
    print(cripto2Rsa)
    print("-------------------------------------------------------------------------")

    return criptoRsa
# ------------------------------------------------------------------

# Função para ler arquivo criptografado e fazer a decriptografia
def lerCriptografia():
    # ABRIR O ARQUIVO DE FRASES CRIPTOGRAFADAS
    # LER DADOS DO ARQUIVO
    with open('arquivotxt001Cripto.txt', encoding="utf-8") as f:
        criptografadas = f.readlines()
        f.closed

    # extrai as frases separadamente
    cripto1 = criptografadas[0].strip()
    cripto2 = criptografadas[1].strip()
    cripto3 = criptografadas[2].strip()

    #Chamar a função para decriptografar
    decriptografia(cripto1)
    decriptografia(cripto2)
    decriptografia(cripto3)
# ------------------------------------------------------------------

# FUNÇÃO PARA DECRIPTOGRAFAR UMA FRASE CRIPTOGRAFADA
def decriptografia(texto):
    # Decriptografia RSA
    print("-------------------------------------------------------------------------")
    print("\nDECRIPTOGRAFANDO EM RSA...")
    decriptoRsa = ""
    decripto2Rsa = []

    fator = 2
    for pos in range(0, len(texto), fator):
        token = int(texto[pos:pos + fator])
        decripto2Rsa.append(token)
    print(decripto2Rsa)

    vetorDecripto = []
    for vl in decripto2Rsa:
        dcp = (vl ** D) % n
        decriptoRsa = decriptoRsa + str(dcp)
        print(vl, "**", D, " = ", vl ** D, "MOD ", n, "= CRIPTO: ", dcp)
        vetorDecripto.append(dcp)

    print("DecriptoRsa: ", decriptoRsa)
    print("vetorDecripto: ", vetorDecripto)

    # --------------------------------------------------------------

    print("-------------------------------------------------------------------------")
    print("\nDESCRIPTOGRAFANDO EM HILL...")
    # frase decriptografada
    decripto = ""
    fator = 4  # numero de sígitos codificados

    for pos in range(0, len(decriptoRsa), fator * 2):
        # SEPARAR OS PRIMEIROS 4 DIGITOS DO NÚMERO CRIPTOGRAFADO
        ftoken1 = int(decriptoRsa[pos:pos + fator])
        # SEPARAR OS 4 ÚLTIMOS DIGITOS DO NÚMERO CRIPTOGRAFADO
        ftoken2 = int(decriptoRsa[pos + fator:pos + 2 * fator])
        print(ftoken1, "   ", ftoken2)
        # VETOR COM OS DADOS CRIPTOGRAFADOS
        cdtoken = [ftoken1, ftoken2]
        print(cdtoken)

        # multiplicar o vetor com os dados criptografados
        # pela matriz de criptografia
        result = multiplicar(chavedecriptomatrix, cdtoken)
        print("Resultado: ", result)

        for p in range(2):
            decripto = decripto + chavedecriptosimetrica2[result[p]]

        print("Frase decriptografada: ", decripto)
    print("-------------------------------------------------------------------------")
# ------------------------------------------------------------------

# ------------------------------------------------------------------
# PROGRAMA PRINCIPAL
# ------------------------------------------------------------------

texto1 = "O RATO ROEU A ROUPA DO REI DE RAPIDOPOLIS"
texto2 = "SABIA QUE O SABIA SABIA ASSOVIAR"
texto3 = "CASA SUJA CHAO SUJO"

# GRAVAR EM ARQUIVO
f = open('arquivotxt001.txt', 'w')
f.writelines(texto1+"\n")
f.writelines(texto2+"\n")
f.writelines(texto3+"\n")
f.close()

# LER DADOS DO ARQUIVO
with open('arquivotxt001.txt', encoding="utf-8") as f:
    linhas = f.readlines()
    f.closed

# extrai as frases separadamente
read_data1 = linhas[0].strip()
read_data2 = linhas[1].strip()
read_data3 = linhas[2].strip()
print("Frase 1: ", read_data1)
print("Frase 1: ", read_data2)
print("Frase 1: ", read_data3)

# Escolher dois numeros primos
p = 5
q = 11

# calculo do quantificador n
n = p * q

# Calcular o tociente de Euler
delta = (p - 1) * (q - 1)

print("P= ", p)
print("Q= ", q)
print("N= ", n)
print("Delta= ", delta)

# especifique E   mdc(delta,e)=1 ; 1 < e < delta
print(gerarPrimo(q + 1, delta))
aux = "DIGITE UM NUMERO mdc(" + str(delta) + ",e) =1 ; 1 < e < " + str(delta) + " : "
# Chave de criptografia - pública
E = int(input(aux))

print("-------------------------------------------------------------------------")
print("ESCOLHA UM NUMERO PRIMO")
D = 1
flag = 100
while (flag != 1):
    D = D + 1
    flag = (E * D) % delta
    print(E, "*", D, " % ", delta, " FLAG= ", flag)
    if (flag == 1):
        print("CHAVE PÚBLICA: [", E, ",", n, "]")
        print("CHAVE PRIVADA: [", D, ",", n, "]")

# chamada da função para fazer a criptografia
frase1 = criptografia(read_data1)
frase2 = criptografia(read_data2)
frase3 = criptografia(read_data3)
gravarCripto(frase1, frase2, frase3)
lerCriptografia()