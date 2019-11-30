from fastapi import FastAPI


app = FastAPI()


TAREFAS = [{"id": 1, "titulo": "Comprar ovos"},
           {"id": 1, "titulo": "tirar o lixo"}]


@app.get('/tarefas')
def listar():
    return TAREFAS