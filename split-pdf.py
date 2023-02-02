import PyPDF2
import os

def select_file():
    file_path = input("Enter the file path: ")
    num_pages = int(input("Enter the number of pages per split file: "))
    split_pdf(file_path, num_pages)

def split_pdf(file_path, num_pages):
    with open(file_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        for i in range(0, len(pdf_reader.pages), num_pages):
            pdf_writer = PyPDF2.PdfWriter()
            for page in pdf_reader.pages[i:i + num_pages]:
                pdf_writer.add_page(page)
            output_file = f"split_{i//num_pages}.pdf"
            with open(output_file, 'wb') as output:
                pdf_writer.write(output)

select_file()

