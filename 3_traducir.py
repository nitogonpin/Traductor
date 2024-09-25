import os
import re
from transformers import pipeline

generador_respuesta = pipeline("translation", model="robertrengel/autotrain-traductor-en-es-2023-3608896666")
#generador_respuesta = pipeline("translation", model="robertrengel/autotrain-traductor-en-es-2023-3608896666", device=0)

ruta_origen = './paginas_limpias'
ruta_destino = './paginas_traducidas'

os.makedirs(ruta_destino, exist_ok=True)

def traducir(texto):
    """
    Esta función toma una cadena de texto y utiliza el modelo robertrengel/autotrain-traductor-en-es-2023-3608896666
    para traducirla del inglés al español. El texto traducido se devuelve entonces.
    """
    # Utiliza la tuber a para generar una traducci n del texto de entrada
    respuesta = generador_respuesta(texto, max_length=30)
    # La respuesta es una lista de diccionarios, por lo que debemos extraer el texto traducido de ella
    respuesta = respuesta[0]['translation_text']
    # Devuelve el texto traducido
    return respuesta
  

def main():
    """
    Iterar sobre los archivos de la carpeta especificada y traducir
    cada archivo. Luego, guardar el resultado en una carpeta
    diferente.
    """
    # Iterar sobre la carpeta y sus subcarpetas
    for root, dirs, files in os.walk(ruta_origen):
        # Iterar sobre los archivos de cada carpeta
        for file in files:
            texto_a_insertar = ""
            # Verificar si el archivo es un archivo de texto

            if file.endswith('.txt'):
                # Conformar la ruta del archivo actual
                file_path = os.path.join(root, file)
                # Abrir el archivo en modo de lectura

                with open(file_path, 'r') as f:
                    # Leer el contenido del archivo en una lista
                    texto = f.readlines()
                    # Iterar sobre cada l nea del archivo
                    
                    for linea in texto:
                        # Llamar a la función traducir para traducir la línea actual
                        traducion = traducir(linea)
                        # Imprimir el resultado para depurar
                        print(traducion)
                        # Agregar el resultado a la variable texto_a_insertar
                        texto_a_insertar += traducion

                # Abrir el archivo en la carpeta de destino en modo de escritura
                with open(os.path.join(ruta_destino, file), 'w') as f:
                    # Escribir el resultado en el archivo
                    f.write(texto_a_insertar)

if __name__ == '__main__':
    main()
