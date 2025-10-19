from fastapi import APIRouter, Form, HTTPException
from app.models.User import User
from app.models.HistoryLocation import HistoryLocation

router = APIRouter()

@router.post('/historylocation')
def gethistory(email: str = Form(...), senha: str = Form(...)):
    user = User.getuser(email, senha)
    if user is None:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")

    return {"longitude": user[4], "latitude": user[5]}

@router.post('/getuser')
def getusers(email: str = Form(...), senha: str = Form(...)):
    user = User.getuser(email, senha)
    if user is None:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")

    history = HistoryLocation.gethistory(user[0])
    result = {
        "id": user[0],
        "nome": user[1],
        "email": user[2],
        "longitude_atual": user[4],
        "latitude_atual": user[5],
        "historico": history
    }
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
    return {"message": "Usuário criado com sucesso"}
