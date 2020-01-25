import PyPDF2
import re

infile = PyPDF2.PdfFileReader('test.pdf', 'rb') 
output = PyPDF2.PdfFileWriter()

def extract_text(pageObj):
    # May fail since extracting plain text from pdf is difficult
    # Can try: https://stackoverflow.com/questions/34837707/how-to-extract-text-from-a-pdf-file
    text = pageObj.extractText()
    return re.sub('[\n\r\s]+', '', text)

prev_pg_text = extract_text(infile.getPage(0))
del_pages = []

for pgNo in range(1, infile.numPages):
    pg_text = extract_text(infile.getPage(pgNo))
    # If current page contains all text of previous page
    if pg_text.startswith(prev_pg_text):
        del_pages.append(pgNo-1)
    prev_pg_text = pg_text

for pgNo in range(infile.numPages):
    if pgNo not in del_pages:
        pg = infile.getPage(pgNo)
        output.addPage(pg)
  
with open('newfile.pdf', 'wb') as f:
    output.write(f)
