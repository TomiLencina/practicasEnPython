import PyPDF2, pyttsx3

#Seguido de la r se tiene que agregar la ruta de donde se encuentra el PDF que se quiere escuchar

path = open(r'grabador de voz\Laboratorio.pdf',  'rb')

pdfReader = PyPDF2.PdfFileReader(path)

from_page = pdfReader.getPage(1)

text = from_page.extractText()

speak = pyttsx3.init()
speak.say(text)
speak.runAndWait()
