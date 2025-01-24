from fastapi import APIRouter, Form
from app.models.User import User

router = APIRouter()

@router.post('/getuser')
def getusers(email: str = Form(...), senha: str = Form(...)):
    user = User.getuser(email, senha)
    result = {"id": user[0], "nome": user[1], "email": user[2], 
    "longitude":user[4], "latitude":user[5]}  
    
    return result 

@router.post('/createuser')
def createuser(
    nome: str = Form(...),
    email: str = Form(...), 
    senha: str = Form(...), 
    longitude: float = Form(...),  
    latitude: float = Form(...)    
):
    User.createuser(nome, email, senha, longitude, latitude)
    user = User.getuser(email, senha)
    return {"message": "Usuario criado com sucesso"}