from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
import numpy as np
import pandas as pd

data = {
    'resena': [
        'el prodcuto funciona excelente',
        'muy buena calidad',
        'el producto llego dañado',
        'muy mala calidad',
        'excelente producto y calidad'
    ],
    'calificacion': [
        'satisfecho',
        'satisfecho',
        'insatisfecho',
        'insatisfecho',
        'satisfecho'
    ]
}

df = pd.DataFrame(data)
print (df)

vectorizar = CountVectorizer()
x = vectorizar.fit_transform(df['resena'])
print(x.toarray())

y = df['calificacion']

modelo = MultinomialNB()
modelo.fit(x,y)

nueva_resena = ['producto mala calidad']
resena_vectorizar = vectorizar.transform(nueva_resena)
prediccion = modelo.predict(resena_vectorizar)
print(prediccion)