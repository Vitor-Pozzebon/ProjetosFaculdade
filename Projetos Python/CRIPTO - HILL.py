import os
os.system("cls")

# CHAVE DE CRIPTOGRAFIA
chavecriptosimetrica2=[{"A":29,"B":49,"C":58,"D":72,"E":13,
                        "F":28,"G":48,"H":57,"I":71,"J":12,
                        "K":27,"L":47,"M":56,"N":70,"O":11,
                        "P":26,"Q":46,"R":55,"S":69,"T":10,
                        "U":25,"V":45,"X":54,"Y":68,"Z":9,
                        "W":24,".":44,",":53,"!":67,"?":8,
                        "$":23,"#":43,"%":52,"*":66,"+":7,
                        "-":22,"/":42,"0":51,"1":65,"2":6,
                        "3":21,"4":41,"5":50,"6":64,"7":5,
                        "8":20,"9":35,
                        "a":19,"b":34,"c":40,"d":63,"e":4,
                        "f":18,"g":33,"h":39,"i":62,"j":3,
                        "k":17,"l":32,"m":38,"n":61,"o":2,
                        "p":16,"q":31,"r":37,"s":60,"t":1,
                        "u":15,"v":30,"x":36,"y":59,"z":0,
                        "w":14," ":73
                        }]

chavedecriptosimetrica2=["z","t","o","j","e","7","2","+","?","Z",
                         "T","O","J","E","w","u","p","k","f","a",
                         "8","3","-","$","W","U","P","K","F","A",
                         "v","q","l","g","b","9","x","r","m","h",
                         "c","4","/","#",",","V","Q","L","G","B",
                         "5","0","%",",","X","R","M","H","C","y",
                         "s","n","i","d","6","1","*","!","Y","S",
                         "N","I","D"," ",]

#chave de criptografia (K)
chavecriptomatrix=[ [1,3],
                    [9,6]]

#chave de decriptografia (K)^-1
chavedecriptomatrix=[ [-2/7,1/7],
                      [3/7,-1/21]]

#função para multiplicar as matrizes
def multiplicar(chave,cod):
    result=[]
    tam=len(chave)
    for lin in range(tam):
        soma=0
        for col in range(tam):
            soma+=chave[lin][col]*cod[col]
        result=result+[int(soma+0.5)]    
    return result

frase = input("DIGITE UMA FRASE: ")
if (len(frase)%2 == 1):         #verificar se a frase possui numero impar de letras
    frase = frase + " "

#vetor criptografado
cripto = ""

#CONVERSÃO DE CADA LETRA PARA O VALOR DA TABELA DE STRING
for pos in range(0, len(frase), 2):
    #separar os caracteres da frase dois a dois
    ftoken = frase[pos:pos+2]
    #montar o valor numérico de cada caractere
    cdtoken = [chavecriptosimetrica2[0][ftoken[0]],
               chavecriptosimetrica2[0][ftoken[1]]]
    #multiplica o vetor numérico pela matriz de criptografia
    result = multiplicar(chavecriptomatrix, cdtoken)
    print(ftoken, "   ", cdtoken, "   ", result)
    
    cripto = cripto + format(result[0], "04d")
    cripto = cripto + format(result[1], "04d")
    print(cripto)

print("\n\nA frase: ", frase)
print("Criptografada é: ", cripto)

#---------------------------------------------------------------------------------------

# DECRIPTOGRAFIA

#frase decriptografada
decripto = ""
fator = 4       #numero de sígitos codificados

for pos in range(0,len(cripto),fator*2):
    #SEPARAR OS PRIMEIROS 4 DIGITOS DO NÚMERO CRIPTOGRAFADO
    ftoken1=int(cripto[pos:pos+fator])
    #SEPARAR OS 4 ÚLTIMOS DIGITOS DO NÚMERO CRIPTOGRAFADO
    ftoken2=int(cripto[pos+fator:pos+2*fator])
    print(ftoken1,"   ",ftoken2)
    #VETOR COM OS DADOS CRIPTOGRAFADOS
    cdtoken=[ftoken1,ftoken2]
    print(cdtoken)

    #multiplicar o vetor com os dados criptografados
    #pela matriz de criptografia
    result = multiplicar(chavedecriptomatrix, cdtoken)
    print("Resultado: ", result)

    for p in range(2):
        decripto=decripto+chavedecriptosimetrica2[result[p]]
    
    print(decripto)