Laboratório — API REST de Gerenciamento de Estoque (FastAPI + XML)

Uma API RESTful para gerenciamento de estoque desenvolvida com FastAPI.
O projeto utiliza XML como camada de persistência, simulando um armazenamento leve e sem dependência de banco de dados.

Tecnologias Utilizadas

Python 3.x

FastAPI

Uvicorn

Pydantic

XML (persistência)

configparser e xml.etree.ElementTree (manipulação de arquivos)

Instalação e Execução
1. Clonar o repositório
git clone https://github.com/SEU_USUARIO/SEU_REPOSITORIO.git
cd Laboratório-FastAPI

2. Instalar dependências
pip install -r requirements.txt


Caso ocorra erro “externally-managed-environment” no Linux:
pip install -r requirements.txt --break-system-packages
(não recomendado para ambientes de produção).

3. Gerar arquivo de configuração
python3 config.py

4. Executar o servidor
uvicorn app:app --reload


Se Uvicorn não estiver no PATH:
~/.local/bin/uvicorn app:app --reload

Endpoints da API

Documentação interativa (Swagger UI):
http://127.0.0.1:8000/docs

Recurso: /aparelhos
Método	Rota	Descrição
POST	/aparelhos	Adiciona um aparelho.
GET	/aparelhos	Lista todos os aparelhos.
GET	/aparelhos/{id}	Retorna um aparelho específico.
PUT	/aparelhos/{id}	Atualiza um aparelho completo.
DELETE	/aparelhos/{id}	Remove um aparelho.
PUT	/aparelhos/{id}/transferir/{novo_deposito}	Transfere o aparelho para outro depósito.
Modelo de Dados (Pydantic)
class Aparelho(BaseModel):
    id: int
    nome: str
    marca: str
    preco: float
    categoria: str
    deposito: str

Persistência

Todas as alterações realizadas por meio dos endpoints (POST, PUT, DELETE) são registradas no arquivo:

estoque.xml


O conteúdo do arquivo reflete sempre o estado atual do estoque.

Autor

Pedro Wilson C. Parreira
