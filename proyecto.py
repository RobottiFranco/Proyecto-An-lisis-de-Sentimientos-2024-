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
    

print (vectorBuildW(frases[1], claveWord))

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

print (vectorBuildS(frases[1], claveWord))
