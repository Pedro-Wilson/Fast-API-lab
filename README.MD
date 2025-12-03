# API REST de Gerenciamento de Estoque — FastAPI + XML

Uma API RESTful desenvolvida com **FastAPI** para gerenciamento simples de estoque, utilizando **XML** como mecanismo de persistência.  
O projeto é ideal para fins acadêmicos, experimentação e compreensão de APIs modernas com armazenamento baseado em arquivos.

---

## 📌 Visão Geral

- API estruturada com FastAPI  
- Persistência em `estoque.xml`  
- CRUD completo para o recurso **Aparelhos**  
- Documentação interativa via Swagger UI  
- Validação com **Pydantic**  
- Execução simples e leve  

---

## ⚙️ Tecnologias Utilizadas

- **Python 3.x**
- **FastAPI**
- **Uvicorn**
- **Pydantic**
- **XML**
- **configparser** e **xml.etree.ElementTree**

---

## 🚀 Instalação e Execução

### 1. Clonar o repositório
```bash
git clone https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git
cd Laboratório-FastAPI
```

### 2. Instalar dependências  
```bash
pip install -r requirements.txt
```

Caso enfrente erros do tipo externally-managed-environment em distribuições Linux:  
pip install -r requirements.txt --break-system-packages  
(Não recomendado para ambientes de produção.)

### 3. Gerar arquivo de configuração  
```bash
python3 config.py
```

### 4. Iniciar o servidor  
```bash
uvicorn app:app --reload
```

Se o Uvicorn não estiver no PATH:  
```bash
~/.local/bin/uvicorn app:app --reload
```

### 🗂️ Endpoints da API  

Documentação interativa:  
http://127.0.0.1:8000/docs

Recurso: /aparelhos  
Método – Rota – Descrição  
POST – /aparelhos – Adiciona um novo aparelho  
GET – /aparelhos – Lista todos os aparelhos  
GET – /aparelhos/{id} – Retorna um aparelho pelo ID  
PUT – /aparelhos/{id} – Atualiza completamente um aparelho  
DELETE – /aparelhos/{id} – Remove um aparelho  
PUT – /aparelhos/{id}/transferir/{novo_deposito} – Transfere o aparelho entre depósitos

### 📄 Modelo de Dados (Pydantic)
```python
class Aparelho(BaseModel):
    id: int
    nome: str
    marca: str
    preco: float
    categoria: str
    deposito: str
```

### 📝 Persistência

As operações que modificam o estoque (POST, PUT, DELETE) atualizam automaticamente o arquivo:
```
estoque.xml
```
Esse arquivo sempre representa o estado atual dos aparelhos cadastrados.

### 👨‍💻 Autor
>> Pedro Wilson C. Parreira
