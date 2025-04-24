from fastapi import FastAPI, Request, HTTPException
import httpx

app = FastAPI()

ARMAZENADOR_URL = "http://armazenador:8002/armazenar"

@app.post("/processar")
async def processar_comentario(request: Request):
    dados = await request.json()
    comentario = dados.get("comentario", "")
    comentario_processado = comentario.lower().replace("ruim", "***")
    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(ARMAZENADOR_URL, json={"comentario": comentario_processado})
        return {"mensagem": "Comentário processado", "resposta": response.json()}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))