try:  
    from PIL import Image
except ImportError:  
    import Image
import pytesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract'

def ocr(filename):  
    """
    This function will handle the core OCR processing of images.
    """

    try:
        newImage = Image.open(filename) 

        print( pytesseract.image_to_string(newImage) )
    except IOError:
    	print('File not found, please check the source folder')


userFile = input('Please add filename \n')

ocr(userFile)