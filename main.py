from typing import Union
from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.staticfiles import StaticFiles
import pikepdf

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

class User(BaseModel):
    name: str
    description: str
    token: str
    password: str 

def generatePassword(name: str):
    oldPdf = pikepdf.Pdf.open('SamplePDF.pdf') 
    no_extracting = pikepdf.Permissions(extract=False)
    password = name
    outputFolder = './output/'
    outputFileName = 'encrypted.pdf'
    val = outputFolder + outputFileName
    print(val)
    try:
        oldPdf.save(val, encryption=pikepdf.Encryption(
            user=password, owner="owner password", allow=no_extracting
        ))
    except:
        return "Something wrong"
    return "Successfully Set the Password in the PDF"


@app.get("/")
def read_root():
    generatePassword()
    return 'PDF Created Successfully'

@app.post("/items/")
async def create_item(user: User):
    if len(user.password) == 0:
        return "Password length is zero, Please provide a valid password"
    res = generatePassword(user.password)
    
    return res


