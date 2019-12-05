import PyPDF2
from pdf2image import convert_from_path, convert_from_bytes
import os, os.path
import sys

#filename = 'test1.pdf'

directory = os.fsencode(sys.argv[1])
noFiles= len([name for name in os.listdir(directory) if os.path.isfile(os.path.join(directory, name))])
i=0
os.mkdir(sys.argv[1]+"/images")
for file in os.listdir(directory):
    filename = os.fsdecode(file)
    if os.path.isfile(os.path.join(directory, file)) and filename != '.DS_Store':
        i+=1
        print ("Processing " + filename + " " + str(i) + " of " + str(noFiles))
        pdf_file = open(sys.argv[1]+'/'+filename, 'rb')
        read_pdf = PyPDF2.PdfFileReader(pdf_file)
        number_of_pages = read_pdf.getNumPages()
        print(number_of_pages)
        for x in range(number_of_pages):
            print ("Processing Page" + str(x) + " of " + str(number_of_pages))
            page = read_pdf.getPage(x)
            print (filename)

            basename = os.path.basename(sys.argv[1]+'/'+filename)
            new_name, _ = os.path.splitext(basename)
            d = sys.argv[1]+'/images/'
            # nn = d+new_name + "_pg_" + str(x)
            nn = d+new_name
            print(sys.argv[1]+"/"+filename)
            print(nn)
            images = convert_from_path(sys.argv[1]+"/"+filename)
            finalFilename = d+new_name + ".jpg"

            for image in images:
            	image.save(finalFilename,'JPEG')

            # text = textract.process(sys.argv[1]+"/"+filename, method='tesseract', language='eng')
            # # f= open(d+new_name + "_pg_" + str(x) + ".txt", "wb")
            # f= open(d+new_name + ".txt", "wb")
            # f.write(text)
            # f.close

