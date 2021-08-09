import PyPDF2
import pyttsx3

filePath = open('file.pdf','rb')
pdfReader = PyPDF2.PdfFileReader(filePath)

startPage = pdfReader.getPage(1)
text = startPage.extractText()

read = pyttsx3.init()
read.say(text)
read.runAndWait()