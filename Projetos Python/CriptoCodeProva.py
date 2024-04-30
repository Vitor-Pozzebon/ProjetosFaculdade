import os
os.system("cls")

#----------------------------------------------------------------------
# CRIPTOGRAFIA COM PROGRESSÃO ARITMÉTICA ------------------------------
#----------------------------------------------------------------------

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


def calculoProgressao(primeiro_numero, razao, frase):
    sequenciaTexto = ""
    tamanho_frase = len(frase)
    sequencia = [primeiro_numero + razao * i for i in range(tamanho_frase)]
    for i in sequencia:
        sequenciaTexto = sequencia
    return sequenciaTexto

print("PARTE 1 - CRIPTOGRAFIA USANDO A CIFRA DE HILL")

cripto = ""
frase = input("\nDIGITE UMA FRASE: ")
fator = int(input("DIGITE UM FATOR DE SHIFT: "))
for s in frase:
    token = (chavecriptosimetrica2[0][s] + fator) % 74  #74 = NUMERO DE DADOS DA CHAVE
    cripto = cripto+format(token, "02d")
    print(s, "   ", token, "   ", cripto)

print("FRASE CRIPTOGRAFADA EM HILL: ", cripto)
print("---------------------------------------------------------------------------")
input("Aperte Enter para continuar...")

print("\nPARTE 2 - USO DE UMA PROGRESSÃO ARITMÉTICA GERADA PELO USUÁRIO PARA CODIFICAR NOVAMENTE O TEXTO")

valorInicial = int(input("\nDIGITE O PRIMEIRO VALOR PARA A PROGRESSÃO (ENTRE 0 E 50): "))
while valorInicial < 0 or valorInicial > 50:
    valorInicial = int(input("VALOR FORA DA FAIXA. TENTE NOVAMENTE: "))
razao = int(input("DIGITE O VALOR DA RAZÃO PARA A PROGRESSÃO (ENTRE 1 E 50): "))
while razao < 1 or razao > 50:
    razao = int(input("VALOR FORA DA FAIXA. TENTE NOVAMENTE: "))
resultado = calculoProgressao(valorInicial, razao, cripto)
print("\nSEQUÊNCIA GERADA: ", resultado)

criptoSeq = ""
fatort = 2
posSeq = 0
for pos in range(0, len(cripto), fatort):
    valorCripto = int(cripto[pos:pos+fatort])
    valorSequencia = int(resultado[posSeq])
    soma = valorCripto + valorSequencia
    criptoSeq = criptoSeq + str(format(soma, "04d"))
    print("ValorCripto: ", valorCripto, " valorSeq: ", valorSequencia, " Soma: ", soma, " Seq: ", criptoSeq)
    posSeq += 1

print("\nFRASE CRIPTOGRAFADA COM A PROGRESSÃO: ", criptoSeq)
print("---------------------------------------------------------------------------")
input("Aperte Enter para continuar...")

#----------------------------------------------------------------------
# DECRIPTOGRAFIA COM PROGRESSÃO ARITMÉTICA ----------------------------
#----------------------------------------------------------------------

chavedecriptoHill = ["z", "t", "o", "j", "e", "7", "2", "+", "?", "Z",
                     "T", "O", "J", "E", "w", "u", "p", "k", "f", "a",
                     "8", "3", "-", "$", "W", "U", "P", "K", "F", "A",
                     "v", "q", "l", "g", "b", "9", "x", "r", "m", "h",
                     "c", "4", "/", "#", ",", "V", "Q", "L", "G", "B",
                     "5", "0", "%", ",", "X", "R", "M", "H", "C", "y",
                     "s", "n", "i", "d", "6", "1", "*", "!", "Y", "S",
                     "N", "I", "D", " ", ]

#retorno da criptografia com a sequência para a criptografia de Hill
print("\nPARTE 3 - DECRIPTOGRAFIA USANDO A PROGRESSÃO PARA VOLTAR À CRIPTOGRAFIA DE HILL")

decriptoSeq = ""
fatort2 = 4
posSeq = 0
for pos in range(0, len(criptoSeq), fatort2):
    valorCripto = int(criptoSeq[pos:pos+fatort2])
    valorSequencia = int(resultado[posSeq])
    subtracao = valorCripto - valorSequencia
    decriptoSeq = decriptoSeq + str(subtracao)
    print("ValorCripto: ", valorCripto, " valorSeq: ", valorSequencia, " Subtração: ", subtracao, " Seq: ", decriptoSeq)
    posSeq += 1

print("\nFRASE DECRIPTOGRAFADA COM A PROGRESSÃO: ", decriptoSeq)
print("---------------------------------------------------------------------------")
input("Aperte Enter para continuar...")

#Retorno da frase criptografada em Hill para a frase original (texto claro)

print("\nPARTE 4 - DECRIPTOGRAFIA DA FRASE DE HILL PARA O TEXTO CLARO")

decripto = ""
fatort = 2
tam = len(cripto)
for pos in range(0, len(decriptoSeq), fatort):
    ftoken = int(decriptoSeq[pos:pos+fatort])
    decripto = decripto + chavedecriptoHill[(ftoken - fator) % 74]
    print(ftoken, "   ", decripto)

print("FRASE DECRIPTOGRAFADA (TEXTO CLARO):  ", decripto)