from fastapi import FastAPI, Request

app = FastAPI()

base_dados = []

@app.post("/armazenar")
async def armazenar_comentario(request: Request):
    dados = await request.json()
    base_dados.append(dados)
    return {"mensagem": "Comentário armazenado com sucesso"}