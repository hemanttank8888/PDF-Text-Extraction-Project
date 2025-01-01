import PyPDF2

# Open the PDF file
with open(r'C:\Users\HemantTank\Desktop\z_flask\data_analytics_testing\AER6303MFS1user_manual_EN.pdf', 'rb') as file:
    reader = PyPDF2.PdfReader(file)
    
    # Iterate through pages
    for page_num in range(len(reader.pages)):
        page = reader.pages[page_num]
        print(page.extract_text())


import fitz  # PyMuPDF

doc = fitz.open(r'C:\Users\HemantTank\Desktop\z_flask\data_analytics_testing\AER6303MFS1user_manual_EN.pdf')
for page_num in range(len(doc)):
    page = doc.load_page(page_num)
    print(page.get_text())


import pytesseract
from PIL import Image
import pytesseract

# Convert PDF page to an image first (using pdf2image, for example)
# Here we assume you have an image of a PDF page
image = Image.open(r'C:\Users\HemantTank\Desktop\z_flask\data_analytics_testing\centriq_DFB8DE9D-961B-4A46-81E2-16A93E681F31.png')



# Set the tesseract executable path explicitly (change the path if it's different on your system)
pytesseract.pytesseract.tesseract_cmd = r"C:\Users\HemantTank\AppData\Local\Programs\Tesseract-OCR\tesseract.exe"

# Now you can call pytesseract
text = pytesseract.image_to_string(image)

# Extract text using Tesseract
text = pytesseract.image_to_string(image)
print(text)
