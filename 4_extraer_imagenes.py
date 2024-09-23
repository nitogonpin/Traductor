import fitz
import os

# Ruta donde se guardaran las imagenes extraidas
ruta_destino_imagnes = './imagen_pdf'

# Crear la carpeta de destino si no existe
os.makedirs(ruta_destino_imagnes, exist_ok=True)

def extraerImagenesPdf(pdf):
    """
    Extrae las imágenes de un archivo PDF y las guarda como archivos PNG.

    El nombre de los archivos se forma como "imagen_<número_de_página>.png"
    si hay una imagen en la página o "imagen_<número_de_página>_<número_de_imagen>.png"
    si hay varias imágenes en la página.

    Parameters:
        pdf (str): La ruta del archivo PDF.

    Returns:
        None
    """
    """
    Abre un archivo PDF con la libreria PyMuPDF (fitz) y extrae las imágenes de cada página.

    Luego, itera sobre las imágenes de cada página, las extrae y las guarda como archivos PNG.

    El nombre de los archivos se forma como "imagen_<número_de_página>.png"
    si hay una imagen en la página o "imagen_<número_de_página>_<número_de_imagen>.png"
    si hay varias imágenes en la página.

    Parameters:
        pdf (str): La ruta del archivo PDF.

    Returns:
        None
    """
    pdf_document = fitz.open(pdf)
    # Iterar sobre las páginas
    for page_index in range(len(pdf_document)):
        page = pdf_document[page_index]
        image_list = page.get_images()
        # Iterar sobre las imágenes de la página
        for image_index, img in enumerate(image_list, start=1):
            xref = img[0]
            base_image = pdf_document.extract_image(xref)
            image_data = base_image["image"]
            # Formar el nombre del archivo de la imagen
            # si hay varias imágenes en la página, se pone el número de imagen
            # si solo hay una, no se pone el número de imagen
            if len(image_list) > 1:
                nombre_archivo = f"imagen_{page_index}_{image_index}.png"
            else:
                nombre_archivo = f"imagen_{page_index}.png"
            ruta_archivo = os.path.join(ruta_destino_imagnes, nombre_archivo)
            with open(ruta_archivo, "wb") as fp:
                # Escribir el contenido de la imagen en el archivo
                fp.write(image_data)

def main():
    extraerImagenesPdf("Deep Reinforcement Learning with Python (2024).pdf")

if __name__ == "__main__":
    main()
