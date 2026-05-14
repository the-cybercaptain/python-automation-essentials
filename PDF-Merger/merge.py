from PyPDF2 import PdfMerger
import os

merger = PdfMerger()

# Corrected path with raw string or escaped backslashes
files = [file for file in os.listdir(r"D:\SLIDES") if file.endswith(".pdf")]

for pdf in files:
    merger.append(os.path.join(r"D:\SLIDES", pdf))

merger.write(r"D:\\SLIDES\\merged_output.pdf")
merger.close()