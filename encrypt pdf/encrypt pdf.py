from PyPDF2 import PdfFileWriter, PdfFileReader

out = PdfFileWriter()

file_path = "resume.pdf"
file = PdfFileReader(file_path)
num = file.numPages
for idx in range(num):
    page = file.getPage(idx)
    out.addPage(page)

password = "arun123"

out.encrypt(password)
with open("encrypted pdf.pdf", "wb") as f:
    out.write(f)
