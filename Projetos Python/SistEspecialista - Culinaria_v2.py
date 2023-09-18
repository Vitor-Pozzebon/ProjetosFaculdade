# -*- coding: utf-8 -*-

#código para sistema especialista - culinária brasileira

#base de dados
BD=[
    {"PRATO":"FEIJOADA","INGREDIENTES": {"FEIJAO":7,"CARNES":3,"COUVE":3,"CEBOLA":2,"ARROZ":3},"OCORRENCIAS": 0,"PERCENTUAL":0},
    {"PRATO":"BAIAO DE DOIS","INGREDIENTES": {"FEIJAO":6,"CARNES":4,"COUVE":1,"CEBOLA":1,"ARROZ":6,"QUEIJO":3,"COENTRO":3,"PIMENTA":1},"OCORRENCIAS": 0,"PERCENTUAL":0},
    {"PRATO":"ARROZ CARRETEIRO","INGREDIENTES": {"CARNES":7,"CEBOLA":3,"ARROZ":8,"PIMENTA":2},"OCORRENCIAS": 0,"PERCENTUAL":0},
    {"PRATO":"ACARAJE","INGREDIENTES": {"FEIJAO":7,"CARNES":7,"FARINHA":2,"AMENDOIM":4,"PIMENTA":6},"OCORRENCIAS": 0,"PERCENTUAL":0},
    {"PRATO":"MOQUECA","INGREDIENTES": {"CARNES":6,"CEBOLA":2,"PIMENTAO":3,"QUEIJO":2},"OCORRENCIAS": 0,"PERCENTUAL":0},
    {"PRATO":"FEIJAO TROPEIRO","INGREDIENTES": {"FEIJAO":9,"CARNES":7,"CEBOLA":1,"FARINHA":5},"OCORRENCIAS": 0,"PERCENTUAL":0},
    {"PRATO":"VIRADO PAULISTA","INGREDIENTES": {"FEIJAO":7,"CARNES":6,"COUVE":3,"ARROZ":5,"FARINHA":4,"OVO":5},"OCORRENCIAS": 0,"PERCENTUAL":0}	
    ]

#coletando dados do usuário

#verificação da alergia ou gosto pessoal  
print("***SEJA BEM VINDO AO RESTAURANTE: MODA BRASILEIRA***")  
print("\nLista de ingredientes dos pratos do restaurante: ")
print("\nFEIJAO; CARNES; COUVE; CEBOLA; ARROZ; QUEIJO; COENTRO")
print("AMENDOIM; PIMENTAO; OVO; FARINHA; PIMENTA")
alergia = input("\nHá algum ingrediente que você não goste ou tenha alergia?: ").upper()

while True:
    ing1 = input("\nDigite o primeiro ingrediente que deseja em seu prato: ").upper()
    if(ing1 != alergia):
        break
    else:
        print("Você é alergia a esse ingrediente. Digite outro.")
v1 = int(input("Qual o seu nível de vontade: "))

while True:
    ing2 = input("Digite o segundo ingrediente que deseja em seu prato: ").upper()
    if(ing2 != alergia):
        break
    else:
        print("Você é alérgico a esse ingrediente. Digite outro.")
v2 = int(input("Qual o seu nível de vontade: "))

while True:
    ing3 = input("Digite o terceiro ingrediente que deseja em seu prato: ").upper()
    if(ing3 != alergia):
        break
    else:
        print("Você é alérgico a esse ingrediente. Digite outro")
v3 = int(input("Qual o seu nível de vontade: "))

for i in BD:
    i["OCORRENCIAS"] = 0
    i["PERCENTUAL"] = 0

#Analisando os dados na BD
for i in BD:
    prato = i["PRATO"]
    print(prato)
    ingredientes = i["INGREDIENTES"]
    print(ingredientes)
    
    if(ing1 in ingredientes):
        i["OCORRENCIAS"] += (ingredientes[ing1])*v1
        print("O ingrediente ", ing1, " compoe o prato ", prato, " que tem como outros ingredientes: ", ingredientes)
        print("\n")
    if(ing2 in ingredientes):
        i["OCORRENCIAS"] += (ingredientes[ing2])*v2
        print("O ingrediente ", ing2, " compoe o prato ", prato, " que tem como outros ingredientes: ", ingredientes)
        print("\n")
    if(ing3 in ingredientes):
        i["OCORRENCIAS"] += (ingredientes[ing3])*v3
        print("O ingrediente ", ing3, " compoe o prato ", prato, " que tem como outros ingredientes: ", ingredientes)
        print("\n")
    
#realizando a contagem
for i in BD:
    print("Prato: ", i["PRATO"], " Peso: ", i["OCORRENCIAS"])
    
#Impressão dos totais com as porcentagens
print("\nRESULTADO:")
for i in BD:
    ingredientes = i["INGREDIENTES"]
    soma = 0
    for j in ingredientes:
        soma += ingredientes[j]
    if(alergia in ingredientes):
        i["PERCENTUAL"] = 0
    else:
        i["PERCENTUAL"] = ((i["OCORRENCIAS"] / soma)/10) * 100
    
    print("\nO prato ", i["PRATO"], " tem probabilidade de ", "{:.2f}".format(i["PERCENTUAL"]), " % de ser o melhor para você hoje!")