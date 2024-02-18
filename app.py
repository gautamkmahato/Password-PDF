import pikepdf

oldPdf = pikepdf.Pdf.open('csir.pdf') 

no_extracting = pikepdf.Permissions(extract=False)

passw = "gkm"
outputFolder = './output/'
outputFileName = 'encrypted3.pdf'
val = outputFolder + outputFileName
print(val)
oldPdf.save(val, encryption=pikepdf.Encryption(
    user=passw, owner="owner password", allow=no_extracting
))