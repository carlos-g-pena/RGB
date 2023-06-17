from PIL import Image
import numpy as np

from main import (
    leer_imagen,
    guardar_matriz,
    cargar_matriz,
    crear_imagen,
    leer_archivo,
    convertir_imagen_a_archivo,
    copiar_matriz,
    convertir_matriz_a_imagen,
)

# CON numpy


def modificar_matriz(matriz):
    matriz_modificada = matriz.copy()
    matriz_modificada[:, :, 0] = 0
    matriz_modificada[:, :, 1] = 2
    # matriz_modificada[:, :, 2] = 255
    return matriz_modificada


# def modificar_matriz_reverse(matriz):
#     matriz_modificada = matriz.copy()
#     return matriz_modificada[::-1, ::-1, :]


def modificar_matriz_reverse(matriz):
    matriz_modificada = matriz.copy()
    for i in range(matriz_modificada.shape[0]):
        for j in range(matriz_modificada.shape[1]):
            matriz_modificada[i, j, :] = matriz[
                matriz.shape[0] - i - 1, matriz.shape[1] - j - 1, :
            ]
    return matriz_modificada


# con MATRIZ
def saturar_colores(m):
    saturacion=0.1
    matriz = copiar_matriz(m)
    for fila in matriz:
        for pixel in fila:
            for i in range(3):
                if pixel[i] < 128:
                    pixel[i] -= int((128 - pixel[i]) * (1 - saturacion))
                else:
                    pixel[i] += int((pixel[i] - 128) * (1 - saturacion))
    return matriz

def saturar_colores(m):
    saturacion=0.1
    matriz = copiar_matriz(m)
    for fila in matriz:
        for pixel in fila:
            for i in range(3):
                if pixel[i] < 128:
                    pixel[i] -= int((128 - pixel[i]) * (1 - saturacion))
                else:
                    pixel[i] += int((pixel[i] - 128) * (1 - saturacion))
    return matriz



def dibujar_linea_en_medio(m):
    rojo=(255,0,0)
    matriz=copiar_matriz(m)
    alto = len(matriz)
    ancho = len(matriz[0])
    fila_medio = alto // 2

    for i in range(fila_medio - 5 // 2, fila_medio + 5 // 2 + 1):
        for j in range(ancho):
            matriz[i][j] = list(rojo)
    return matriz

def aplicar_filtro_promedio(matriz):
    filas = len(matriz)
    columnas = len(matriz[0])
    matriz_difuminada = copiar_matriz(matriz)

    for i in range(1, filas - 1):  # Excluir los bordes de la imagen
        for j in range(1, columnas - 1):  # Excluir los bordes de la imagen
            promedio_r, promedio_g, promedio_b = 0, 0, 0

            for dy in range(-1, 2):  # Rango [-1, 0, 1]
                for dx in range(-1, 2):  # Rango [-1, 0, 1]
                    pixel = matriz_difuminada[i + dy][j + dx]
                    promedio_r += pixel[0]
                    promedio_g += pixel[1]
                    promedio_b += pixel[2]

            promedio_r //= 9  # Dividir por el número de vecinos
            promedio_g //= 9
            promedio_b //= 9

            matriz_difuminada[i][j] = [promedio_r, promedio_g, promedio_b]

    return matriz_difuminada

def difuminar_imagen(m):
    for _ in range(10):
        m = aplicar_filtro_promedio(m) 
    return m

def convertir_escala_de_grises(m):
    matriz = copiar_matriz(m)
    for fila in matriz:
        for pixel in fila:
            pixel[2] = pixel[1]
            pixel[0] = pixel[1]
    return matriz


def convertir_negativo(m):
    matriz = copiar_matriz(m)
    for fila in matriz:
        for pixel in fila:
            pixel[0] = 255 - pixel[0]
            pixel[1] = 255 - pixel[1]
            pixel[2] = 255 - pixel[2]
    return matriz


def promedios_colores(listadecolres):
    suma = sum(listadecolres)
    # Se dividira en 3, ya que tenemos 3  trabajmos con  R, G , B
    Promediofinal = int(suma / 3)
    # Se retorna Promediofinal ya una vez obtenido
    return Promediofinal


def convertir_blanco_negro(m):
    matriz = copiar_matriz(m)
    for fila in matriz:
        for pixel in fila:
            pp = promedios_colores(pixel)
            if pp > 180:
                pixel[0] = 255
                pixel[1] = 255
                pixel[2] = 255
            elif pp <= 180:
                pixel[0] = 0
                pixel[1] = 0
                pixel[2] = 0
    return matriz


name_img = "img.jpg"
array_img = "array_img.txt"
salida_img = "img_modificada.png"

convertir_imagen_a_archivo(name_img, array_img)
matriz_img = leer_archivo(array_img)

new_matriz = difuminar_imagen(matriz_img)

convertir_matriz_a_imagen(new_matriz, salida_img, True)
