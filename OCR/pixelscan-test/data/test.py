import PyPDF2
import textract
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

filename = 'test1.pdf'

#open allows you to read the file
pdfFileObj = open(filename,'rb')
#The pdfReader variable is a readable object that will be parsed
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
#discerning the number of pages will allow us to parse through all #the pages
num_pages = pdfReader.numPages
count = 0
text = ""

pageObj = pdfReader.getPage(0)
text += pageObj.extractText()

#This if statement exists to check if the above library returned #words. It's done because PyPDF2 cannot read scanned files.
if text != "":
   text = text
#If the above returns as False, we run the OCR library textract to #convert scanned/image based PDF files into text
else:
   text = textract.process(filename, method='tesseract', language='eng')
   f= open("test.txt","wb")
   f.write(text)
   f.close
