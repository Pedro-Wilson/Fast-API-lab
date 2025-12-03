💻 Laboratório: API REST de Gerenciamento de Estoque com FastAPI e XML

Este projeto implementa uma API RESTful simples para gerenciamento de estoque, utilizando o framework FastAPI em Python. A principal característica é a persistência dos dados, que é realizada diretamente em um arquivo XML (estoque.xml), simulando um sistema de armazenamento.


⚙️ Tecnologias Utilizadas

    Python 3.x

    FastAPI: Framework de alta performance para construção de APIs.

    Uvicorn: Servidor ASGI para rodar a aplicação FastAPI.

    Pydantic: Biblioteca para tipagem de dados e validação.

    XML: Formato de arquivo para persistência de dados.

    configparser / xml.etree.ElementTree: Bibliotecas padrão do Python para manipulação de arquivos.


🚀 Instalação e Execução

Pré-requisitos

Certifique-se de ter o Python 3 e o pip instalados.
1. Clonar o Repositório
Bash

git clone [Link do seu repositório]
cd Laboratório-FastAPI

2. Instalar Dependências

Instale os pacotes necessários listados no requirements.txt.

Nota sobre Linux (externally-managed-environment): Caso encontre erros de permissão, utilize a flag --break-system-packages (não recomendado para ambientes de produção):
Bash

pip install -r requirements.txt --break-system-packages

3. Configurar o Arquivo de Estoque

Execute o script de configuração para criar o arquivo config.ini:
Bash

python3 config.py

4. Rodar o Servidor

Inicie o servidor Uvicorn. Use o caminho completo do executável (~/.local/bin/uvicorn) se ele não estiver no seu PATH:
Bash

~/.local/bin/uvicorn app:app --reload

🗺️ Endpoints da API

Com o servidor rodando, a documentação interativa Swagger UI fica disponível em: http://127.0.0.1:8000/docs

A API suporta as seguintes operações para o recurso /aparelhos:
Método	Rota	Descrição
POST	/aparelhos	Adiciona um novo aparelho ao estoque.
GET	/aparelhos	Lista todos os aparelhos.
GET	/aparelhos/{id}	Busca um aparelho específico pelo ID.
PUT	/aparelhos/{id}	Atualiza completamente um aparelho existente.
DELETE	/aparelhos/{id}	Remove um aparelho pelo ID.
PUT	/aparelhos/{id}/transferir/{novo_deposito}	Função de Transferência: Altera o depósito de um aparelho específico.

💡 Modelo de Dados (Pydantic)

O schema de dados (Aparelho) define a estrutura do JSON esperada para as requisições:
Python

class Aparelho(BaseModel):
    id: int
    nome: str
    marca: str
    preco: float
    categoria: str
    deposito: str

📝 Teste de Persistência

A persistência é validada ao inspecionar o arquivo estoque.xml após a execução de operações POST, PUT ou DELETE. O conteúdo do arquivo deve refletir o estado atual do estoque.

Desenvolvido por: Pedro Wilson C. Parreira
