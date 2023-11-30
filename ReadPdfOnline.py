#!pip install PyMuPDF
import fitz
import requests
from io import BytesIO
import pandas as pd

datos = []
def extraer_pdf(url):
  #url = "https://storage.googleapis.com/certificados-vur/001-1415753.pdf" # URL del PDF que deseas leer
  response = requests.get(url) # Descarga el PDF desde la URL
  pdf_data = response.content
  pdf_document = fitz.open(stream=pdf_data, filetype="pdf") # Abre el documento PDF desde los datos descargados
  texto = []
  for page_number in range(pdf_document.page_count): # Itera a través de las páginas del PDF
    page = pdf_document.load_page(page_number) # Obtiene la página actual
    page_text = page.get_text() # Extrae el texto de la página
    texto.append(f"Texto en la página {page_number + 1}:\n{page_text}\n")
    print(f"Texto en la página {page_number + 1}:\n{page_text}\n") # Imprime el texto de la página actual
  pdf_document.close() # Cierra el documento PDF
  datos.append("".join(texto))
  return 
