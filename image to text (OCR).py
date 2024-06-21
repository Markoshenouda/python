
import pytesseract
from PIL import Image

# Set the path to Tesseract
pytesseract.pytesseract.tesseract_cmd=r"C:\Program Files\Tesseract-OCR\tesseract.exe"

def convert():
    # Get the image filename from user input
    img=Image.open(input("enter the name of photo : \n")+".png")
    try:
        text = pytesseract.image_to_string(img)
        # Open the image
        # Extract text from the image
        print("Extracted text: \n ")
        # Print the extracted text
        print(text)
    except FileNotFoundError:
         print("Error: Image file '{img_filename}' not found. ")
convert()
# Call the function

