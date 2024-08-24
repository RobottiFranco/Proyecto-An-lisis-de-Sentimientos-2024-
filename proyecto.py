import numpy as np

frases = [
    "Excelente en su área, su muerte es una enorme pérdida y debería ser luto nacional",
    "Estoy muy feliz con los resultados obtenidos en el examen",
    "El clima está terrible hoy, no me gusta para nada",
    "Es un gran avance para la ciencia",
    "Estoy cansado y estresado por todo lo que sucede",
    "Fue una sorpresa positiva ver que todo salió bien",
    "Perder ese contrato fue una gran decepción",
    "Estoy neutral respecto a la decisión tomada",
    "Me encanta cómo se resolvió todo, fue excelente",
    "Odio cuando las cosas no salen como espero",
    "La película fue genial, pero el final fue un desastre",
    "Me siento muy mal por lo que sucedió",
    "El evento fue un éxito rotundo",
    "Fue una gran pérdida para la compañía",
    "Estoy completamente decepcionado con el servicio"
]

claveWord = {
    'positiva' : ['increible', 'excelente', 'feliz', 'avance', 'positiva', 'bien', 'encanta', 'genial', 'éxito'],
    'neutra' : ['avance', 'sorpresa', 'neutral'],
    'negativa' : ['muerte', 'pérdida', 'luto', 'terrible', 'cansado', 'estresado', 'odio', 'desastre', 'mal', 'decepcionado']
}


def vectorBuildW(frase, claveWord):
    vectorW = []
    for palabra in claveWord['positiva'] + claveWord['negativa'] + claveWord['neutra']:
        vectorW.append(frase.lower().count(palabra))
    return np.array(vectorW)
    

#print (vectorBuildW(frases[1], claveWord))

def vectorBuildS(frase, claveWord):
    positivo, neutral, negativo = 0, 0, 0
    for palabra in frase.lower().split():
        if palabra in claveWord["positiva"]:
            positivo += 1
        elif palabra in claveWord["neutra"]:
            neutral += 1
        elif palabra in claveWord["negativa"]:
            negativo += 1
    return np.array([positivo, neutral, negativo])

#print (vectorBuildS(frases[1], claveWord))


def calidadPromedio(vectorW):
    suma = sum(vectorW)
    totalPalabras = len(vectorW)
    result = suma / totalPalabras
    return result

#print(calidadPromedio(vectorW= vectorBuildW(frases[1], claveWord)))


def promedioSentimiento(vectorS):
    vector = np.array([1, 0, -1])
    return np.dot(vector, vectorS)
 
#print(promedioSentimiento(vectorS= vectorBuildS(frases[8], claveWord)))

totalVectoresW = []
totalVectoresS = []

for w in frases:
    vectorW = vectorBuildW(w, claveWord)
    vectorS = vectorBuildS(w, claveWord)

    totalVectoresW.append(vectorW)
    totalVectoresS.append(vectorS)

    calidad = calidadPromedio(vectorW)
    promSentimiento = promedioSentimiento(vectorS)

    print(f'Frase: "{w}"')
    print(f'Calidad promedio: {calidad:.2f}')
    print(f'Promedio de sentimiento: {promSentimiento}')
    print(f'Palabras positivas: {vectorS[0]}, Neutras: {vectorS[1]}, Negativas: {vectorS[2]}\n')
