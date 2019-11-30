from fastapi import FastAPI


app = FastAPI()


TAREFAS = [{"id": 1, "titulo": "Comprar ovos"},
           {"id": 1, "titulo": "tirar o lixo"}]


@app.get("/")
def index():
    return "Lista de tarefas.\nPara ver a lista entre em \\tarefas"

@app.get('/tarefas')
def listar():
    return TAREFAS