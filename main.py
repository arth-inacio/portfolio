from fastapi import FastAPI, Form
from pydantic import BaseModel

app = FastAPI()

class Contact(BaseModel):
    name: str
    email: str
    phone: str
    subject: str
    message: str

@app.post("/save-contact")
async def save_contact(name: str = Form(...), email: str = Form(...), phone: str = Form(...), subject: str = Form(...), message: str = Form(...)):
    # Salvar as informações em um banco de dados ou arquivo
    contact_info = {
        "name": name,
        "email": email,
        "phone": phone,
        "subject": subject,
        "message": message
    }
    print(contact_info)  # Para testar no console
    return {"message": "Contato salvo com sucesso!", "data": contact_info}
