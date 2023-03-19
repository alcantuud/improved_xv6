
from urllib.request import urlopen

if __name__ == '__main__':
    url = urlopen('https://gist.githubusercontent.com/jsdario/6d6c69398cb0c73111e49f1218960f79/raw/8d4fc4548d437e2a7203a5aeeace5477f598827d/el_quijote.txt')
    contenido = url.read().decode('utf-8')
    longitud = input('Longitud de palabra mínima: ')
    longitud = int(longitud)
    #las 10 primeras palabras frecuentes con esa longitud mínimo
    '''
    contar apariciones y guardar en diccionario
    '''
    diccionario = {}
    palabras = contenido.split()
    for palabra in palabras:
        palabra = palabra.lower()
        palabra = palabra.strip(',.:;-–!¡¿?\()«»[[]‘“"''')
        if len(palabra) >= longitud:
            if palabra not in diccionario:
                diccionario[palabra] = 1
            else:
                diccionario[palabra] += 1

    inverso = {}
    for palabra in diccionario:
        n = diccionario[palabra]
        if n not in inverso:
            inverso[n] = [palabra]
        else:
            inverso[n].append(palabra)

    claves = list(inverso.keys())
    claves.sort(reverse=True)
    for n in claves[:10]:
        print(n, inverso[n])

