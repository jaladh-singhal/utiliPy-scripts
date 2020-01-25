import PyPDF2
import re, sys

# Input through Command line arguments
if len(sys.argv)<2:
    print('Also give a PDF filepath on which script will work\n')
    exit(1)
else:
    in_fpath= sys.argv[1]

if len(sys.argv)==3: # To give output file path
	out_fpath = sys.argv[2]
else:   # Replace the same file
	out_fpath = in_fpath


# Initialize PDF reader & writer objects
in_file = PyPDF2.PdfFileReader(in_fpath, 'rb') 
out_file = PyPDF2.PdfFileWriter()

# To extract text from a PDF page
def extract_text(pageObj):
    # Works fine for PDFs I tested with, yet it may fail for others
    # See: https://stackoverflow.com/questions/34837707/how-to-extract-text-from-a-pdf-file
    text = pageObj.extractText()
    return re.sub('[\n\r\s]+', '', text)


prev_pg_text = extract_text(in_file.getPage(0))
del_pages = []

for pgNo in range(1, in_file.numPages):
    pg_text = extract_text(in_file.getPage(pgNo))
    # If current page contains all text of previous page
    if pg_text.startswith(prev_pg_text):
        del_pages.append(pgNo-1) # Delete previous page
    prev_pg_text = pg_text

# To delete pages, have to write a new PDF excluding those
for pgNo in range(in_file.numPages):
    if pgNo not in del_pages:
        pg = in_file.getPage(pgNo)
        out_file.addPage(pg)
  
with open(out_fpath, 'wb') as f:
    out_file.write(f)
