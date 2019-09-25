import glob
from PyPDF2 import PdfFileWriter, PdfFileReader
 
def merger(output_path, input_paths):
    pdf_writer = PdfFileWriter()
 
    for path in input_paths:
        pdf_reader = PdfFileReader(path)
        for page in range(pdf_reader.getNumPages()):
            pdf_writer.addPage(pdf_reader.getPage(page))
    with open(output_path, 'wb') as fh:
        pdf_writer.write(fh)
        
if __name__ == '__main__':
    path = 'S:\\'
    #folders = [f for f in glob.glob(path + "**/", recursive=False)]
    #folders.sort()
    #for f in folders:
        #files = []
        #files = [s for s in glob.glob(f + "PDF/*.searchable.pdf", recursive=True) ]
        #if len(files) == 0: 
            #print(f + ' needs searchables')
            
    pFolder = input("Folder: ")
    pFullFolder = path + pFolder + '/'
    files = [s for s in glob.glob(pFullFolder + "PDF/*.searchable.pdf", recursive=True) ]
    if len(files) == 0: 
        print(pFullFolder + ' needs searchables')   
    else: 
        print(pFullFolder + ' has searchables \n')
        print( files[0]) 
        
    hasSearchableBinder = len([b for b in  glob.glob(pFullFolder + "PDF/"+pFolder + ".searchable.pdf", recursive=True)]) 
    
    if hasSearchableBinder > 0:
        print ("has Searchable Binder") 
        domerge = 'n'
    else:
        
        domerge = input ("Do you want to merge them?")
        
    if domerge.lower() in (1,'y'): 
        searchables =    pFullFolder + "PDF/"+pFolder + "*.searchable.pdf"
        print(searchables)
        paths = glob.glob(searchables)
        paths.sort()
        
        output_path = pFullFolder + "PDF/"+pFolder + ".searchable.pdf"
        
        merger(output_path, paths)
        print (output_path +  " created")
        
    hasBinder = len([b for b in  glob.glob(pFullFolder + "PDF/"+pFolder + ".pdf", recursive=True)]) 
    
    if hasBinder > 0:
        print ("has Binder") 
        domergen = 'n'
    else:

        domergen = input ("Do you want to merge the normal PDFs?")
        

        
    if domergen.lower() in (1,'y'): 
        pdfs =  input ("Complete Path line =  " + pFullFolder + "PDF/")
        
        pdfs = pFullFolder + "PDF/" + pdfs
        print(pdfs)
        paths = glob.glob(pdfs)
        paths.sort()
        
        output_path = pFullFolder + "PDF/"+pFolder + ".pdf"
        
        merger(output_path, paths)
        print (output_path +  " created")
        
        