import PyPDF2

def split_pdf(file_path, page_limit=30):
    # Open the PDF file
    pdf_file = open(file_path, 'rb')
    pdf_reader = PyPDF2.PdfFileReader(pdf_file)

    # Get the number of pages in the PDF file
    num_pages = pdf_reader.numPages

    # Calculate the number of stacks
    num_stacks = num_pages // page_limit

    # Loop through each stack
    for i in range(num_stacks):
        # Create a PDF file for the stack
        stack_file = open(f"stack_{i}.pdf", 'wb')
        pdf_writer = PyPDF2.PdfFileWriter()

        # Add pages to the stack
        for j in range(page_limit):
            page_num = i * page_limit + j
            if page_num >= num_pages:
                break
            page = pdf_reader.getPage(page_num)
            pdf_writer.addPage(page)

        # Write the stack to the file
        pdf_writer.write(stack_file)

        # Close the stack file
        stack_file.close()

    # Close the PDF file
    pdf_file.close()

# Example usage
split_pdf('sample.pdf')

