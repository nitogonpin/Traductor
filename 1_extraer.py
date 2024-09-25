import PyPDF2

def crearTxt(numero, texto):  
    """
    Crea un archivo de texto con el nombre numero.txt en la carpeta paginas y 
    escribe el texto en el archivo.

    Parameters
    ----------
    numero : int
        El numero del archivo.
    texto : str
        El texto a escribir en el archivo.

    Returns
    -------
    bool
        True si el archivo se ha creado correctamente.
    """
    with open(f'./paginas/{numero}.txt', 'w') as f:
        f.write(texto)
        return True


def extraerTexto(pdf):
  """
  Extrae el texto de un archivo PDF.

  Parameters
  ----------
  pdf : str
    El nombre del archivo PDF.

  Returns
  -------
  str
    El texto extraido del archivo PDF.
  """
  texto = ''
  contador = 1
  # Abrir el archivo PDF
  with open(pdf, 'rb') as f:
    # Crear un objeto de lectura de PDF
    pdfReader = PyPDF2.PdfReader(f)
    # Iterar sobre las paginas del PDF
    for page in pdfReader.pages:
      texto = page.extract_text()
      crearTxt(contador, texto)
      contador += 1
  return texto


def main():
    """
    Funcion principal del programa.
    """
    # Obtener el texto del PDF
    pdf = 'a-christmas-carol-charles-dickens.pdf'
    text = extraerTexto(pdf)    
     
 

if __name__ == '__main__':
    # Llamar a la funcion principal
    main()
