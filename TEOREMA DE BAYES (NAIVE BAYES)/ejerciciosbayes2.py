from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import numpy as np
import pandas as pd

data = {
    'titular': [
        'equipo gana campeonato',
        'nuevo telefono inteligente',
        'jugador anota gol decisivo',
        'empresa lanza nueva computadora',
        'equipo gana torneo'
    ],
    'categoria': [
        'deportes',
        'tecnologia',
        'deportes',
        'tecnologia',
        'deportes'
    ]
}

df = pd.DataFrame(data)
print (df)

vector = CountVectorizer()
x = vector.fit_transform(df['titular'])
print(x.toarray())

y = df['categoria']

modelo = MultinomialNB()
modelo.fit(x,y)

#vER EL VOCABULARIO QUE DETECTO EL MODELO
print("\nCONTADOR DE PALABRAS")
palabras = vector.get_feature_names_out()
print(palabras)

tabla_prob = pd.DataFrame(
    modelo.feature_log_prob_,
    columns=palabras,
    index=modelo.classes_
)
print("ORDENAR")
tabla_prob.loc["deportes"].sort_values(ascending=False)
print(tabla_prob)

print("\nPREDICCION")
titular = ['nuevo equipo gana']
titulo_vector = vector.transform(titular)
prediccion = modelo.predict(titulo_vector)
print(prediccion)