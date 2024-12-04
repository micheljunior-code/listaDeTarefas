from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()


class Tarefa(BaseModel):
    id: int
    titulo: str
    descricao: str
    completa: bool = False


tarefas: List[Tarefa] = []
  
@app.get("/")
def get_api():
    return "Bem-Vindo,Liste aqui suas tarefas de rotina..."


@app.get("/tarefas", response_model=List[Tarefa])
def listar_tarefas():
    return tarefas

@app.post("/tarefas", response_model=Tarefa)
def adicionar_tarefa(tarefa: Tarefa):
    for t in tarefas:
        if t.id == tarefa.id:
            raise HTTPException(status_code=400, detail="ID já existe")
    tarefas.append(tarefa)
    return tarefa

@app.put("/tarefas/{tarefa_id}", response_model=Tarefa)
def atualizar_tarefa(tarefa_id: int, tarefa_atualizada: Tarefa):
    for index, tarefa in enumerate(tarefas):
        if tarefa.id == tarefa_id:
            tarefas[index] = tarefa_atualizada
            return tarefa_atualizada
    raise HTTPException(status_code=404, detail="Tarefa não encontrada")

@app.delete("/tarefas/{tarefa_id}")
def deletar_tarefa(tarefa_id: int):
    for index, tarefa in enumerate(tarefas):
        if tarefa.id == tarefa_id:
            del tarefas[index]
            return {"message": "Tarefa removida com sucesso"}
    raise HTTPException(status_code=404, detail="Tarefa não encontrada")
