import os

os.system("cls")

chavecriptosimetrica=[{"A":"H","B":"Y","C":"A","D":"P","E":"*",
"F":"I","G":"Z","H":"B","I":"Q","J":"/",
"K":"J","L":"W","M":"C","N":"R","O":"#",
"P":"K","Q":".","R":"D","S":"S","T":"$",
"U":"L","V":",","X":"E","Y":"T","Z":"%",
"W":"M",".":"+",",":" ","!":"U","?":"?",
"$":"N","#":"-","%":"G","*":"V","+":"!",
"-":"O","/":"X","0":"9","1":"8","2":"7",
"3":"6","4":"5","5":"4","6":"3","7":"2",
"8":"1","9":"0",
"a":"f","b":"q","c":"l","d":"v","e":"a",
"f":"g","g":"r","h":"m","i":"x","j":"b",
"k":"h","l":"s","m":"n","n":"y","o":"c",
"p":"i","q":"t","r":"o","s":"z","t":"d",
"u":"j","v":"u","x":"p","y":"w","z":"e",
"w":"k"," ":"F"
}]

cripto = ""
frase=input("DIGITE UMA FRASE: ")
for c in frase:
    aux = chavecriptosimetrica[0][c]
    print(c, "   ", aux)
    cripto = cripto + aux
print("TEXTO ORIGINAL:  ", frase)
print("TEXTO CODIFICADO:   ", cripto)

print("---------------------------------------------------------------------------")

chavedecriptosimetrica=[{"A":"C","B":"H","C":"M","D":"R","E":"X",
"F":" ","G":"%","H":"A","I":"F","J":"K",
"K":"P","L":"U","M":"W","N":"$","O":"-",
"P":"D","Q":"I","R":"N","S":"S","T":"Y",
"U":"!","V":"*","X":"/","Y":"B","Z":"G",
"W":"L",".":"Q",",":"V","!":"+","?":"?",
"$":"T","#":"O","%":"Z","*":"E","+":".",
"-":"#","/":"J","0":"9","1":"8","2":"7",
"3":"6","4":"5","5":"4","6":"3","7":"2",
"8":"1","9":"0",
"a":"e","b":"j","c":"o","d":"t","e":"z",
"f":"a","g":"f","h":"k","i":"p","j":"u",
"k":"w","l":"c","m":"h","n":"m","o":"r",
"p":"x","q":"b","r":"g","s":"l","t":"q",
"u":"v","v":"d","x":"i","y":"n","z":"s",
"w":"y"," ":","
}]

decripto=""
cripto = input("DIGITE UMA FRASE CRIPTOGRAFADA: ")
for s in cripto:
    token=chavedecriptosimetrica[0][s]
    decripto=decripto+token
print("FRASE DECRIPTOGRAFADA: ",decripto)