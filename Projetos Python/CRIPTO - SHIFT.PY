import os
os.system("cls")

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

cripto = ""
frase = input("DIGITE UMA FRASE: ")
fator = int(input("DIGITE UM FATOR DE SHIFT: "))
for s in frase:
    token = (chavecriptosimetrica2[0][s] + fator) % 74  #74 = NUMERO DE DADOS DA CHAVE
    cripto = cripto+format(token, "02d")
    print(s, "   ", token, "   ", cripto)

print("FRASE CRIPTOGRAFADA: ", cripto)

print("---------------------------------------------------------------------------")

chavedecriptosimetrica2 = ["z", "t", "o", "j", "e", "7", "2", "+", "?", "Z",
                           "T", "O", "J", "E", "w", "u", "p", "k", "f", "a",
                           "8", "3", "-", "$", "W", "U", "P", "K", "F", "A",
                           "v", "q", "l", "g", "b", "9", "x", "r", "m", "h",
                           "c", "4", "/", "#", ",", "V", "Q", "L", "G", "B",
                           "5", "0", "%", ",", "X", "R", "M", "H", "C", "y",
                           "s", "n", "i", "d", "6", "1", "*", "!", "Y", "S",
                           "N", "I", "D", " ", ]

decripto = ""
fatort = 2
tam = len(cripto)
for pos in range(0, len(cripto), fatort):
    ftoken = int(cripto[pos:pos+fatort])
    decripto = decripto + chavedecriptosimetrica2[(ftoken - fator) % 74]

print("FRASE DECRIPTOGRAFADA:  ", decripto)