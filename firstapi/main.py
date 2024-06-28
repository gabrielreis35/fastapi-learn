from fastapi import FastAPI, HTTPException, status

app = FastAPI()

cursos = {
    1: {
        "titulo": "Programação",
        "aulas": 112,
        "horas": 58
    },
    2: {
        "titulo": "Algoritmo",
        "aulas": 85,
        "horas": 40
    }
}

@app.get('/cursos')
async def getCursos():
    return cursos

@app.get('/cursos/{id}')
async def getCursoPorId(id: int):
    try:
        curso = cursos[id]
        return curso
    except KeyError:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Não encontrado")

if __name__ == '__main__':
    import uvicorn

    uvicorn.run("main:app",
                host="0.0.0.0",
                port=8000,
                log_level="info",
                reload=True,
                debug=True
                )