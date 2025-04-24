from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel, validator
import httpx

app = FastAPI()

PROCESSADOR_URL = "http://processador:8001/processar"

class ComentarioEntrada(BaseModel):
    comentario: str

    @validator('comentario')
    def validar_conteudo(cls, v):
        if not v.strip():
            raise ValueError("Comentário não pode estar vazio")
        if len(v) < 5:
            raise ValueError("Comentário muito curto")
        return v

@app.post("/comentario")
async def receber_comentario(entrada: ComentarioEntrada):
    try:
        async with httpx.AsyncClient() as client:
            response = await client.post(PROCESSADOR_URL, json=entrada.dict())
        return {"mensagem": "Comentário enviado para processamento", "resposta": response.json()}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
