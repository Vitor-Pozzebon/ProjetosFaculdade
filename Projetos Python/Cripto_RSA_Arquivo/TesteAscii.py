import os

os.system("cls")

def converterAscii(f):
    caracterNum = ""
    for i in f:
        caracterNum = caracterNum + " " + str(ord(i)).zfill(3)

    print(caracterNum)

frase = input("Digite uma frase para ser convertida em ASCII: ")

converterAscii(frase)