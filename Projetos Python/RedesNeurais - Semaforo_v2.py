# -*- coding: utf-8 -*-

import matplotlib.pyplot as plt
import numpy as np
import random
import time
import os

from sklearn.neural_network import MLPClassifier
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
#ENTRADAS    G1|Y1|R1   G2|Y2|R2   G3|Y3|R3   G4|Y4|R4 
X        = [[1.,0.,0.,  0.,0.,1.,  0.,0.,1.,  0.,0.,1.],
            [0.,1.,0.,  0.,0.,1.,  0.,0.,1.,  0.,0.,1.],
            [0.,0.,1.,  1.,0.,0.,  0.,0.,1.,  0.,0.,1.],
            [0.,0.,1.,  0.,1.,0.,  0.,0.,1.,  0.,0.,1.],
            [0.,0.,1.,  0.,0.,1.,  1.,0.,0.,  0.,0.,1.],
            [0.,0.,1.,  0.,0.,1.,  0.,1.,0.,  0.,0.,1.],
            [0.,0.,1.,  0.,0.,1.,  0.,0.,1.,  1.,0.,0.],
            [0.,0.,1.,  0.,0.,1.,  0.,0.,1.,  0.,1.,0.]]

#SAIDAS      G1|Y1|R1   G2|Y2|R2   G3|Y3|R3   G4|Y4|R4
Y        = [[0.,1.,0.,  0.,0.,1.,  0.,0.,1.,  0.,0.,1.],
            [0.,0.,1.,  1.,0.,0.,  0.,0.,1.,  0.,0.,1.],
            [0.,0.,1.,  0.,1.,0.,  0.,0.,1.,  0.,0.,1.],
            [0.,0.,1.,  0.,0.,1.,  1.,0.,0.,  0.,0.,1.],
            [0.,0.,1.,  0.,0.,1.,  0.,1.,0.,  0.,0.,1.],
            [0.,0.,1.,  0.,0.,1.,  0.,0.,1.,  1.,0.,0.],
            [0.,0.,1.,  0.,0.,1.,  0.,0.,1.,  0.,1.,0.],
            [1.,0.,0.,  0.,0.,1.,  0.,0.,1.,  0.,0.,1.]]

clf = MLPClassifier(solver='lbfgs',activation='logistic', 
        alpha=1e-5,hidden_layer_sizes=(300,300), random_state=1)
print("INICIO DO TREINAMENTO DA REDE NEURAL - SEMÁFORO")
clf.fit(X, Y)
print("TERMINO DO TREINAMENTO DA REDE NEURAL - SEMÁFORO")

vetor = [[1,0,0,0,0,1,0,0,1,0,0,1]]
while True:
    Z = clf.predict(vetor)
    print("\n\n")
    print(Z)
    print(" SE1    SE2    SE3    SE4")
    C= "| "+str(Z[0][0])+" |  | "+str(Z[0][3])+" |  | "+str(Z[0][6])+" |  | "+str(Z[0][9])+" |\n"
    C+= "|---|  |---|  |---|  |---|\n"
    C+= "| "+str(Z[0][1])+" |  | "+str(Z[0][4])+" |  | "+str(Z[0][7])+" |  | "+str(Z[0][10])+" |\n"
    C+= "|---|  |---|  |---|  |---|\n"
    C+= "| "+str(Z[0][2])+" |  | "+str(Z[0][5])+" |  | "+str(Z[0][8])+" |  | "+str(Z[0][11])+" |\n"
    print(C)
    vetor = Z
    time.sleep(5)