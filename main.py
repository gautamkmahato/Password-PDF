from typing import Union
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
import pikepdf

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

def generatePassword():
    oldPdf = pikepdf.Pdf.open('SamplePDF.pdf') 
    no_extracting = pikepdf.Permissions(extract=False)
    password = "12345"
    outputFolder = './output/'
    outputFileName = 'encrypted.pdf'
    val = outputFolder + outputFileName
    print(val)
    oldPdf.save(val, encryption=pikepdf.Encryption(
        user=password, owner="owner password", allow=no_extracting
    ))


@app.get("/")
def read_root():
    generatePassword()
    return 'PDF Created Successfully'


