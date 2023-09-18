# -*- coding: utf-8 -*-

#Exercício sobre os trens de pouso de um avião.
#O LED verde de autorização deve acender somente se todos os trens de pouso estiverem ativos (Indicado pelo número 1)
#Caso contrário, o LED vermelho acenderá, indicando a não permissão de pouso

import matplotlib.pyplot as plt
import numpy as np
import random

from sklearn.neural_network import MLPClassifier
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split

#entradas
x = [
     
     [0.,0.,0.],
     [0.,0.,1.],
     [0.,1.,0.],
     [0.,1.,1.],
     [1.,0.,0.],
     [1.,0.,1.],
     [1.,1.,0.],
     [1.,1.,1.]
     
     ]

#saidas
y = [
     
     ['LED vermelho'],
     ['LED vermelho'],
     ['LED vermelho'],
     ['LED vermelho'],
     ['LED vermelho'],
     ['LED vermelho'],
     ['LED vermelho'],
     ['LED verde'],
     
     ]

#Comando para configurar a rede
clf = MLPClassifier(solver='lbfgs',activation='logistic', 
        alpha=1e-5,hidden_layer_sizes=(450,450), random_state=1)

#comando para treinar a rede
print("INICIO DO TREINAMENTO DA REDE NEURAL")
clf.fit(x, y)
print("TERMINO DO TREINAMENTO DA REDE NEURAL")

#realização de testes
t = [1.,1.,1.]
print("TESTANDO...")
z = clf.predict([t])
print(z)
