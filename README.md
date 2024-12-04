# 📚 Gerenciador de Tarefas - FastAPI

## 📄 Descrição do Projeto

Uma API simples para gerenciamento de tarefas (To-Do List), criada com FastAPI, que permite criar, listar, atualizar e excluir tarefas.

---

## 👨‍💻 Tecnologias Empregadas  
- **Python 3.10+**  
- **FastAPI**  
- **Uvicorn** (servidor ASGI)  
- **Postman** (para testar as rotas)  

---

## ⚙️ Instruções para Execução 

### Pré-requisitos  
1. Tenha o **Python 3.10+** instalado em sua máquina.
   
2. **Criar e Ativar um Ambiente Virtual (venv)**  
   Para isolar as dependências do projeto e garantir que não haja conflitos com outros projetos, é recomendado criar um ambiente virtual. Siga os passos abaixo:

   - No terminal, navegue até o diretório do projeto e execute o seguinte comando para criar um ambiente virtual:
     ```bash
     python -m venv venv
     ```
   
   - Para ativar o ambiente virtual:
     - **No Windows:**
       ```bash
       .\venv\Scripts\activate
       ```
     - **No macOS/Linux:**
       ```bash
       source venv/bin/activate
       ```

3. **Instalar as dependências**  
   Com o ambiente virtual ativado, instale as dependências necessárias:
   ```bash
   pip install -r requirements.txt
  

## ⚙️  Como Rodar a API

1. **Iniciar o servidor Uvicorn**
2. **Execute o seguinte comando no terminal para iniciar o servidor:**
  ```bash
   uvicorn main:app --reload
  ```

3. **Acessar a API**
Após iniciar o servidor, a API estará disponível em **http://localhost:8000**. Você pode acessar as rotas e testar as funcionalidades.

4. **Testar as rotas com Postman**
Use o Postman para testar as rotas da API, como:

      **GET /tarefas – Listar Tarefas.**
      
      **POST /tarefas – Adicionar uma nova Tarefa.**
      
      **PUT /tarefas/{id} – Atualizar uma Tarefa.**
      
      **DELETE /tarefas/{id} – Deletar uma Tarefa.**
