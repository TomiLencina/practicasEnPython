from pdf2docx import Converter

#En pdf_file poner la ruta del pdf a convertir y en docx_file poner la ruta del nuevo archivo

pdf_file = "grabador de voz\Laboratorio.pdf"
docx_file = "grabador de voz\Laboratorio.docx"
cv = Converter(pdf_file)
cv.convert(docx_file)
cv.close()