from fastapi import FastAPI, HTTPException,status
from fastapi.responses import JSONResponse
from models import Curso

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
        
@app.post('/cursos', status_code=status.HTTP_201_CREATED)
async def postCurso(curso: Curso):
    if curso.id not in cursos:
        cursos[curso.id] = curso
        return curso
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                            detail="Curso já existente")

@app.put('/cursos/{id}', status_code=status.HTTP_202_ACCEPTED)
async def putCurso(id: int, curso: Curso):
   if id in cursos:
        cursos[id] = curso
        return curso
   else:
       raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                           detail="Curso não existente com este id")

@app.delete('/cursos/{id}')
async def deleteCurso(id: int):
    if id in cursos:
        del cursos[id]
        return JSONResponse(status_code=status.HTTP_200_OK, content=None)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail="Curso não existente com este id")

if __name__ == '__main__':
    import uvicorn

    uvicorn.run("main:app",
                host="0.0.0.0",
                port=8000,
                log_level="info",
                reload=True
                )