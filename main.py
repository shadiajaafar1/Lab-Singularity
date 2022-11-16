from classes import DoubleLinkedList
from classes import clean_df 

lista_d = DoubleLinkedList()
for i in range(len(clean_df.index[0:25])):
    lista_d.AddNode(i, 'Departamento_ocurrencia', 'QUINDIO')
    
lista_d.Recorrido()