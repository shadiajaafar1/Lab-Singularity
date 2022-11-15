import pandas as pd
import numpy as np

cols = ["PAC_HOS", "SEXO", "Municipio_ocurrencia", "CON_FIN", "FEC_NOT", "ANO","EDAD", "Departamento_ocurrencia"] 
datos = pd.read_excel("Dengue_todos.xlsx", usecols=cols)

datos.to_csv("df_clean.csv" , index = False, sep = ",", encoding='utf-8')
df = pd.read_csv("df_clean.csv")

clean_df = df.drop(index = df.index[720714:720747])
#clean_df[clean_df.isnull().any(axis=1)]

class Nodo_Dep:
    def __init__(self, x, nom: str,\
        df, next = None, prev = None):  
        self.ind = x       
        self.nom = clean_df.loc[x, nom]
        self.df = df
        # self.model = model
        self.next = next
        self.prev = prev

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def AddNode(self,x, nom):
        P = Nodo_Dep(x=x, nom=nom)
        if (self.head == None):
            self.head = P
            self.tail = P 
        else:
            self.tail.next = P
            P.prev = self.tail
            self.tail = P  
        self.tail.next = self.head
        self.head.prev = self.tail
    
    def Recorrido(self):
        P = self.head
        print(P.nom, end=" ")
        P = P.prev
        while(P != self.head):
            print(P.nom, end =" ")
            P = P.prev

lista_d = DoubleLinkedList()
for i in range(len(clean_df.index)):
    lista_d.AddNode(i, 'Departamento_ocurrencia')
    
lista_d.Recorrido()