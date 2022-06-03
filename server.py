from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    username:str
    email:str
    password:str

@app.post("/datos")
async def home(user: User):
        if(user.username and user.password and user.email):
                return f'Hola {user.username} el sistema accedio sin problemas a tu cuenta'
        else:
                return 'Ocurrio un error , intenta de nuevo con los campos correspondientes'
@app.get("/")
def root():
        return 'QUE TAL BIENVENIDO, REGISTRATE CON TU INFORMACION EN UN JSON EN BODY XD'
