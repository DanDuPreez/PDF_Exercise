import glob
from fpdf import FPDF
from pathlib import Path

# Create a list of text filepaths
filepaths = glob.glob('text/*.txt')
# Create one PDF file
pdf = FPDF(orientation='P', unit='mm', format='A4')

# Go through each text file
for filepath in filepaths:
    # Add a page to the PDF document for each text file
    pdf.add_page()

    # Get the filename without the extention
    # and convert it to title case (eg. Cat)
    filename = Path(filepath).stem
    name = filename.title()

    # Add the name to the PDF
    pdf.set_font(family='Times', size=16, style='B')
    pdf.cell(w=50, h=8, txt=name, ln=1)

# Produce the PDF
pdf.output('output.pdf')
