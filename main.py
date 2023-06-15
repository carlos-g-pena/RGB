from PIL import Image
import numpy as np

# Con numpy

def leer_imagen(ruta):
    imagen = Image.open(ruta)
    matriz_rgb = np.array(imagen.convert('RGB'))
    return matriz_rgb

def guardar_matriz(matriz, nombre_archivo):
    np.save(nombre_archivo, matriz)

def cargar_matriz(nombre_archivo):
    matriz_cargada = np.load(nombre_archivo)
    return matriz_cargada

def crear_imagen(matriz):
    imagen_modificada = Image.fromarray(matriz, 'RGB')
    return imagen_modificada

# Sin numpy

def convertir_imagen_a_archivo(nombre_imagen, nombre_destino):
    imagen = Image.open(nombre_imagen)
    imagen = imagen.convert('RGB')
    matriz_numpy = np.array(imagen)
    archivo = open(nombre_destino, 'w')
    for fila in matriz_numpy:
        for pixel in fila :
            for componente in pixel :
                archivo.write( ' ' + str(componente))
            archivo.write(',')
        archivo.write('\n')
    archivo.close()

def convertir_matriz_a_imagen(matriz, nombre_salida, show = False):
    arr = np.array(matriz)
    im = Image.fromarray(arr.clip(0,255).astype('uint8'), 'RGB')
    im.save(nombre_salida)
    if show:
        im.show()

def leer_archivo(nombre):
    archivo = open(nombre,'r')
    matriz = []
    for i in archivo :
        lista = []
        fila = []
        lista = i.strip(",\n").split(',')
        for pixel in lista :
            aux  = pixel.split()
            for e in range(3) :
                aux[e] = int(aux[e])
            fila.append(aux)
        matriz.append(fila)
    return matriz

def copiar_matriz(matriz):
    matriz_resultado = []
    filas = len(matriz)
    columnas = len(matriz[0])
    for i in range(filas):
        nueva_fila = []
        for  j in range(columnas):
            rojo = matriz[i][j][0]
            verde = matriz [i][j][1]
            azul = matriz[i][j][2]
            pixel = [rojo, verde, azul]
            nueva_fila.append(pixel)
        matriz_resultado.append(nueva_fila)
    return matriz_resultado
