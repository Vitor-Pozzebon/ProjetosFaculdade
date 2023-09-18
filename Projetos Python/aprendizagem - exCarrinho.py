# -*- coding: utf-8 -*-
"""
Created on Mon Mar 13 20:07:11 2023

@author: 12224719
"""

import matplotlib.pyplot as plt
import numpy as np
import random

from sklearn.neural_network import MLPClassifier
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split

#Entradas
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

#Saidas
y = [
     
     [0.,0.],
     [1.,0.],
     [1.,1.],
     [1.,0.],
     [0.,1.],
     [1.,1.],
     [0.,1.],
     [0.,1.]
     
     ]

#Comando para configurar a rede
clf = MLPClassifier(solver='lbfgs',activation='logistic', 
        alpha=1e-5,hidden_layer_sizes=(450,450), random_state=1)

#comando para treinar a rede
print("INICIO DO TREINAMENTO DA REDE NEURAL")
clf.fit(x, y)
print("TERMINO DO TREINAMENTO DA REDE NEURAL")

#Utilizacao da variavel de teste
t = [1.,1.,0.]

#Execucao do teste
print("TESTANDO...")
z = clf.predict([t])
print(z)