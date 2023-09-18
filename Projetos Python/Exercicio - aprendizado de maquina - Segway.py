# -*- coding: utf-8 -*-

#Exercicio SEGWAY

import matplotlib.pyplot as plt
import numpy as np
import random

from sklearn.neural_network import MLPClassifier
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split

#ENTRADAS
x = [
     
     [0,0,0],
     [1,0,1],
     [1,1,0],
     [0,0,1],
     [0,1,0],
     [1,1,1]
     
     ]

#SAÍDAS
y = [
     
     [0,0,0,0],
     [0,1,0,1],
     [1,0,1,0],
     [0,1,1,0],
     [1,0,0,1],
     [1,1,1,1]
     
     ]

#Comando para configurar a rede
clf = MLPClassifier(solver='lbfgs',activation='logistic', 
        alpha=1e-5,hidden_layer_sizes=(450,450), random_state=1)

#comando para treinar a rede
print("INICIO DO TREINAMENTO DA REDE NEURAL")
clf.fit(x, y)
print("TERMINO DO TREINAMENTO DA REDE NEURAL")

#Realização de testes
t = [0,0,1]
z = clf.predict([t])
print(z)