import PyPDF2
import os
from pathlib import Path

def merger(file_name):
    root = Path(__file__).parent.parent
    pdfs_path = root / 'PDF'
    new_pdfs_path = pdfs_path / 'merged'

    new_pdf = PyPDF2.PdfFileMerger()

    for root, dirs, files in os.walk(pdfs_path):
        for file in files:
            complete_pdfs_path = os.path.join(root, file)
            
            pdf_file = open(complete_pdfs_path, 'rb')
            new_pdf.append(pdf_file)

    with open(f'{new_pdfs_path}/{file_name}.pdf', 'wb') as my_new_pdf:
        new_pdf.write(my_new_pdf)


def spliter(file_name):
    root = Path(__file__).parent.parent
    pdfs_path = root / 'PDF'
    new_pdfs_path = pdfs_path / 'splited'

    with open(f'{pdfs_path}/{file_name}.pdf', 'rb') as pdf_file:
        reader = PyPDF2.PdfFileReader(pdf_file)
        pages_numb = reader.getNumPages()
        
        for pages_numb in range(pages_numb):
            writer = PyPDF2.PdfFileWriter()
            actual_page = reader.getPage(pages_numb)
            writer.addPage(actual_page)
            
            with open(f'{new_pdfs_path}/{file_name}{pages_numb + 1}.pdf', 'wb') as new_pdf:
                writer.write(new_pdf)
                