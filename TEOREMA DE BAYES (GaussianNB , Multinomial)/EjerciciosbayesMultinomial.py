import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import accuracy_score, confusion_matrix
from sklearn.model_selection import train_test_split

df = pd.read_csv("~/Documents/ENRIQUE UNAM Y TRABAJOFUT\OCTAVO SEMESTRE\Mineria de Datos/amazon_cells_labelled.txt",
                 sep="\t",
                 names=["texto","sentimiento"])

print(df.head())
#Contamos el numero de palabras en cada texto
print(df['sentimiento'].value_counts())

#Crear modelo de Naive Bayes Multinomial
vector = CountVectorizer()
X = vector.fit_transform(df['texto'])
y = df['sentimiento']

#Dividir los datos
modelo = MultinomialNB()
modelo.fit(X,y)

#prediccion
ejemplos = ["I love the anime Jujutsu Kaisen","This product is terrible"]
X_ejemplos = vector.transform(ejemplos)
pred = modelo.predict(X_ejemplos)
print(pred)

#Evaluar el modelo
X_train, X_test, y_train, y_test = train_test_split(X, y , test_size=0.1) #Dividimos los datos en entrenamiento y prueba

modelo.fit(X_train,y_train)
y_pred = modelo.predict(X_test)

accurracy = accuracy_score(y_test, y_pred)
print(f"Precision {accurracy:.2f}")
