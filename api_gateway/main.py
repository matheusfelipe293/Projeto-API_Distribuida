from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
import httpx

app = FastAPI()

PROCESSADOR_URL = "http://processador:8001/processar"

class ComentarioEntrada(BaseModel):
    comentario: str = Field(..., min_length=5, description="Comentário deve ter no mínimo 5 caracteres")

@app.post("/comentario")
async def receber_comentario(entrada: ComentarioEntrada):
    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(PROCESSADOR_URL, json=entrada.dict())
        return {"mensagem": "Comentário enviado para processamento", "resposta": response.json()}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))