import PyPDF2, os

def combinePdfPages(start_page = 0):
    """
    Combine pdf files in the current directory starting from the specified the page.
    param start_page: the specified page number after which the pages will be combined.
    """
    pdfFiles = []
    for filename in os.listdir('.'):
        if filename.endswith('.pdf'):
            pdfFiles.append(filename)

    pdfFiles.sort(key = str.lower)

    pdfWriter = PyPDF2.PdfFileWriter()

    for filename in pdfFiles:
        pdfFileObj = open(filename, 'rb')
        pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

        for pageNum in range(start_page, pdfReader.numPages):
            pageObj = pdfReader.getPage(pageNum)
            pdfWriter.addPage(pageObj)

    pdfOutput = open('CombinedPdf.pdf', 'wb')
    pdfWriter.write(pdfOutput)
    pdfOutput.close()
    

