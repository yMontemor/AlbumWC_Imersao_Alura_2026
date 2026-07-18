import os
import glob
# pyrefly: ignore [missing-import]
from fastapi import FastAPI, HTTPException
# pyrefly: ignore [missing-import]
from fastapi.responses import FileResponse
# pyrefly: ignore [missing-import]
from fastapi.middleware.cors import CORSMiddleware

# Cria a instância da aplicação FastAPI
app = FastAPI()

# Configure o middleware CORS para aceitar requisições de qualquer origem
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Define o caminho absoluto da pasta de imagens para o servidor encontrar a pasta independente de onde for executado
PASTA_BASE = os.path.dirname(os.path.abspath(__file__))
PASTA_IMAGENS = os.path.join(PASTA_BASE, "figurinhas")

# Lista contendo as figurinhas do álbum (total de 30 figurinhas)
# Apenas as figurinhas cujas imagens existem na pasta figurinhas/ ficam ativas.
# As outras (IDs 21 a 30) estão comentadas até que suas respectivas imagens estejam disponíveis.
figurinhas = [
    {
        "id": 1,
        "nome": "Lautaro Martínez",
        "categoria": "Argentina",
        "imagem_url": "/figurinhas/1/imagem"
    },
    {
        "id": 2,
        "nome": "Julián Álvarez",
        "categoria": "Argentina",
        "imagem_url": "/figurinhas/2/imagem"
    },
    {
        "id": 3,
        "nome": "Lionel Messi",
        "categoria": "Argentina",
        "imagem_url": "/figurinhas/3/imagem"
    },
    {
        "id": 4,
        "nome": "Emiliano Martínez",
        "categoria": "Argentina",
        "imagem_url": "/figurinhas/4/imagem"
    },
    {
        "id": 5,
        "nome": "Lionel Scaloni",
        "categoria": "Argentina",
        "imagem_url": "/figurinhas/5/imagem"
    },
    {
        "id": 6,
        "nome": "Harry Kane",
        "categoria": "Inglaterra",
        "imagem_url": "/figurinhas/6/imagem"
    },
    {
        "id": 7,
        "nome": "Bukayo Saka",
        "categoria": "Inglaterra",
        "imagem_url": "/figurinhas/7/imagem"
    },
    {
        "id": 8,
        "nome": "Jude Bellingham",
        "categoria": "Inglaterra",
        "imagem_url": "/figurinhas/8/imagem"
    },
    {
        "id": 9,
        "nome": "Pickford",
        "categoria": "Inglaterra",
        "imagem_url": "/figurinhas/9/imagem"
    },
    {
        "id": 10,
        "nome": "Tomas Tuchel",
        "categoria": "Inglaterra",
        "imagem_url": "/figurinhas/10/imagem"
    },
    {
        "id": 11,
        "nome": "Rodri",
        "categoria": "Espanha",
        "imagem_url": "/figurinhas/11/imagem"
    },
    {
        "id": 12,
        "nome": "Nico Willians",
        "categoria": "Espanha",
        "imagem_url": "/figurinhas/12/imagem"
    },
    {
        "id": 13,
        "nome": "Lamine Yamal",
        "categoria": "Espanha",
        "imagem_url": "/figurinhas/13/imagem"
    },
    {
        "id": 14,
        "nome": "Dani Olmo",
        "categoria": "Espanha",
        "imagem_url": "/figurinhas/14/imagem"
    },
    {
        "id": 15,
        "nome": "Luis de La Fuente",
        "categoria": "Espanha",
        "imagem_url": "/figurinhas/15/imagem"
    },
    {
        "id": 16,
        "nome": "Michael Olise",
        "categoria": "França",
        "imagem_url": "/figurinhas/16/imagem"
    },
    {
        "id": 17,
        "nome": "Ousmane Dembele",
        "categoria": "França",
        "imagem_url": "/figurinhas/17/imagem"
    },
    {
        "id": 18,
        "nome": "Kylian Mbappe",
        "categoria": "França",
        "imagem_url": "/figurinhas/18/imagem"
    },
    {
        "id": 19,
        "nome": "Dayot Upamecano",
        "categoria": "França",
        "imagem_url": "/figurinhas/19/imagem"
    },
    {
        "id": 20,
        "nome": "Didier Deschamps",
        "categoria": "França",
        "imagem_url": "/figurinhas/20/imagem"
    },
    {
        "id": 21,
        "nome": "AT&T Stadium",
        "categoria": "Palcos de Decisão",
        "imagem_url": "/figurinhas/21/imagem"
    },
    {
        "id": 22,
        "nome": "Atlanta Stadium",
        "categoria": "Palcos de Decisão",
        "imagem_url": "/figurinhas/22/imagem"
    },
    {
        "id": 23,
        "nome": "MetLife Stadium",
        "categoria": "Palcos de Decisão",
        "imagem_url": "/figurinhas/23/imagem"
    },
    {
        "id": 24,
        "nome": "Hard Rock Stadium",
        "categoria": "Palcos de Decisão",
        "imagem_url": "/figurinhas/24/imagem"
    },
    {
        "id": 25,
        "nome": "Logo Oficial",
        "categoria": "Palcos de Decisão",
        "imagem_url": "/figurinhas/25/imagem"
    },
    {
        "id": 26,
        "nome": "Maple",
        "categoria": "Mascotes e Símbolos",
        "imagem_url": "/figurinhas/26/imagem"
    },
    {
        "id": 27,
        "nome": "Zayu",
        "categoria": "Mascotes e Símbolos",
        "imagem_url": "/figurinhas/27/imagem"
    },
    {
        "id": 28,
        "nome": "Trófeu da Copa do Mundo",
        "categoria": "Mascotes e Símbolos",
        "imagem_url": "/figurinhas/28/imagem"
    },
    {
        "id": 29,
        "nome": "Clutch",
        "categoria": "Mascotes e Símbolos",
        "imagem_url": "/figurinhas/29/imagem"
    },
    {
        "id": 30,
        "nome": "Trionda",
        "categoria": "Mascotes e Símbolos",
        "imagem_url": "/figurinhas/30/imagem"
    }
]

# Define o endpoint GET para obter a lista de figurinhas
@app.get("/figurinhas")
def listar_figurinhas():
    return figurinhas

# Endpoint para servir a imagem de cada figurinha pelo id
@app.get("/figurinhas/{id}/imagem")
def obter_imagem_figurinha(id: int):
    # Usa glob para encontrar o arquivo com prefixo "{id:02d}[!0-9]*" na pasta figurinhas/
    padrao = os.path.join(PASTA_IMAGENS, f"{id:02d}[!0-9]*")
    arquivos = glob.glob(padrao)
    
    # Retorna 404 se não encontrar nenhuma imagem com esse padrão
    if not arquivos:
        raise HTTPException(status_code=404, detail="Imagem não encontrada")
    
    # Retorna FileResponse com o arquivo encontrado
    return FileResponse(arquivos[0])

