import os
import re

ruta_origen = './paginas'
ruta_destino = './paginas_limpias'

os.makedirs(ruta_destino, exist_ok=True)

def guardarTexto(texto, nombre_archivo):
    """
    Guarda el texto en un archivo con el nombre proporcionado.

    Parámetros:
    texto (str): El texto a guardar.
    nombre_archivo (str): El nombre del archivo donde se guardará el texto.

    Returns:
    None
    """

    with open(os.path.join(ruta_destino, nombre_archivo), 'w') as f:
        f.write(texto)

def limpiarTexto(texto, file):
    """
    Limpia el texto dado reemplazando las ocurrencias de " \n" con un solo espacio,
    y luego guarda el texto limpio en un archivo con el nombre dado.

    Parámetros:
    texto (str): El texto a limpiar.
    file (str): El nombre del archivo donde se guardará el texto limpio.

    Retorna:
    None
    """
    texto = re.sub(r" \n", " ", texto)
    print(texto)
    guardarTexto(texto, file)   

def main():
    """
    Recorre el árbol de directorios empezando en ruta_origen y realiza las siguientes acciones para cada archivo .txt encontrado:
    1. Construye la ruta completa del archivo.
    2. Abre el archivo y lee su contenido.
    3. Llama a la función limpiarTexto con el contenido del archivo y el nombre del archivo como argumentos.

    Parámetros:
    Ninguno

    Retorna:
    Ninguno
    """    
    for root, dirs, files in os.walk(ruta_origen):
        for file in files:
            if file.endswith('.txt'):
                file_path = os.path.join(root, file)
                with open(file_path, 'r') as f:
                    texto = f.read()
                    limpiarTexto(texto, file)      

if __name__ == '__main__':
    main()