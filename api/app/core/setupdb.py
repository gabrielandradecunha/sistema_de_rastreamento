from app.models.User import User

def setupdb():
    User.create()
    return "teste"