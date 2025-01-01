# PDF Text Extraction Project
This project demonstrates how to extract text from a PDF document using multiple Python libraries: PyPDF2, PyMuPDF (also known as fitz), and pytesseract for OCR (Optical Character Recognition) when dealing with image-based PDFs.

## Features
- PyPDF2: Extracts text from PDFs with straightforward, text-based content.
- PyMuPDF (fitz): Extracts text from PDFs, providing additional flexibility and accuracy.
- pytesseract: Performs OCR to extract text from image-based PDFs (when PDFs contain scanned images or non-text content).


## Installation
- To run the app locally, follow the steps below:
```bash
git clone https://github.com/hemanttank8888/PDF-Text-Extraction-Project.git
cd /path/to/your/project
python -m venv venv
.\venv\Scripts\activate
pip install -r requirements.txt
python app.py
```
- Requirements

    `Python 3.x`

    `Libraries:`

    `PyPDF2`

    `PyMuPDF (fitz)`

    `pytesseract`

    `Pillow (for image processing)`

    `pdf2image (to convert PDF pages to images, if  using OCR)`
## Usage

    1. Extract Text Using PyPDF2:
    The PyPDF2 library extracts text from the PDF directly if the content is available in a text format (not images).

    2. Extract Text Using PyMuPDF (fitz)
    The PyMuPDF (fitz) library is another option to extract text and has some additional capabilities compared to PyPDF2.

    3. Extract Text Using pytesseract (OCR)
    If the PDF contains images or scanned content (non-selectable text), you can convert the PDF page to an image and then use pytesseract to perform OCR.

    First, convert the PDF to an image (e.g., using pdf2image), then use Tesseract to extract text from the image.




## Running the Code
- Make sure you have installed all the dependencies using pip install -r requirements.txt.
- Ensure that Tesseract-OCR is installed and the path is correctly set.
- Modify the file paths in the examples to point to your PDF or image files.
- Run the scripts to extract text from the PDF in different ways.
