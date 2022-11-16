import pandas as pd
import numpy as np
import json as js

cols = ["PAC_HOS", "SEXO", "Municipio_ocurrencia", "CON_FIN", "FEC_NOT", "ANO","EDAD", "Departamento_ocurrencia"] 
datos = pd.read_excel("Dengue_todos.xlsx", usecols=cols)

datos.to_csv("df_clean.csv" , index = False, sep = ",", encoding='utf-8')
df = pd.read_csv("df_clean.csv")

clean_df = df.drop(index = df.index[720714:720747])
#clean_df[clean_df.isnull().any(axis=1)]

dic_dep = {
    "Departamentos": ["AMAZONAS", "ANTIOQUIA", "ARAUCA", \
        "ATLANTICO", "BOGOTA", "BOLIVAR", "BOYACA", "CALDAS", \
        "CAQUETA", "CASANARE", "CAUCA", "CESAR", "CHOCO", "CORDOBA",\
        "CUNDINAMARCA", "EXTERIOR", "GUAINIA", "GUAJIRA", "GUAVIARE",\
        "HUILA","MAGDALENA", "META", "NARIÑO", "NORTE SANTANDER",\
        "PROCEDENCIA DESCONOCIDA", "PUTUMAYO", "QUINDIO", "RISARALDA", \
        "SAN ANDRES", "SANTANDER", "SUCRE", "TOLIMA", "VALLE", "VAUPES","VICHADA"]
}

y = js.dumps(dic_dep)
print(y)