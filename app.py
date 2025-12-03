import configparser
import os
import xml.etree.ElementTree as ET
from typing import List, Dict, Any

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

# --- 1. CONFIGURAÇÃO E VARIÁVEIS GLOBAIS ---
# Carrega o nome do arquivo de estoque do config.ini
config = configparser.ConfigParser()
config.read('config.ini')
# Usa 'estoque.xml' como fallback, caso config.ini não seja lido
ARQUIVO_ESTOQUE = config['DEFAULT'].get('arquivo', 'estoque.xml') 

# Instância da aplicação FastAPI
app = FastAPI(
    title="FastAPI Gerenciamento de Estoque",
    description="API REST para operações CRUD em um estoque persistido em XML.",
)


# --- 2. MODELO DE DADOS (Pydantic) ---
# Define a estrutura de um aparelho. 
class Aparelho(BaseModel):
    id: int = Field(..., gt=0)
    nome: str
    marca: str
    preco: float = Field(..., gt=0.0)
    categoria: str
    deposito: str


# --- 3. FUNÇÕES AUXILIARES DE PERSISTÊNCIA (XML) ---

def carregar_aparelhos_xml() -> List[Dict[str, Any]]:
    """Carrega os aparelhos do arquivo XML. Cria o arquivo se não existir."""
    aparelhos = []
    
    if not os.path.exists(ARQUIVO_ESTOQUE):
        # Cria um nó raiz vazio se o arquivo não existe
        root = ET.Element('estoque')
        tree = ET.ElementTree(root)
        tree.write(ARQUIVO_ESTOQUE, encoding='utf-8', xml_declaration=True)
        return aparelhos

    try:
        tree = ET.parse(ARQUIVO_ESTOQUE)
        root = tree.getroot()
        
        for aparelho_elem in root.findall('aparelho'):
            ap = {
                "id": int(aparelho_elem.find('id').text),
                "nome": aparelho_elem.find('nome').text,
                "marca": aparelho_elem.find('marca').text,
                "preco": float(aparelho_elem.find('preco').text),
                "categoria": aparelho_elem.find('categoria').text,
                "deposito": aparelho_elem.find('deposito').text,
            }
            aparelhos.append(ap)
            
    except ET.ParseError:
        print("Atenção: Erro ao analisar o arquivo XML. Retornando estoque vazio.")
    
    return aparelhos


def salvar_aparelhos_xml(aparelhos: List[Dict[str, Any]]) -> None:
    """Salva a lista de aparelhos no arquivo XML."""
    root = ET.Element('estoque')
    
    for ap_data in aparelhos:
        aparelho_elem = ET.SubElement(root, 'aparelho')
        for key, value in ap_data.items():
            child = ET.SubElement(aparelho_elem, key)
            child.text = str(value)

    tree = ET.ElementTree(root)
    # Salvando com formatação bonita (pretty-print)
    ET.indent(tree, space="\t", level=0)
    tree.write(ARQUIVO_ESTOQUE, encoding='utf-8', xml_declaration=True)


# --- 4. ENDPOINTS DA API ---

@app.post("/aparelhos", status_code=201, tags=["Aparelhos"])
def adicionar_aparelho(aparelho: Aparelho):
    """Adiciona um novo aparelho ao estoque."""
    aparelhos = carregar_aparelhos_xml()
    
    # Verifica duplicidade de ID
    if any(a["id"] == aparelho.id for a in aparelhos):
        raise HTTPException(status_code=400, detail="ID já existe. Não foi possível adicionar o aparelho.")
    
    aparelhos.append(aparelho.model_dump())
    salvar_aparelhos_xml(aparelhos)
    
    return {"message": "Aparelho adicionado com sucesso", "aparelho": aparelho}


@app.get("/aparelhos", response_model=List[Aparelho], tags=["Aparelhos"])
def listar_aparelhos():
    """Lista todos os aparelhos no estoque."""
    return carregar_aparelhos_xml()


@app.get("/aparelhos/{id}", response_model=Aparelho, tags=["Aparelhos"])
def buscar_aparelho(id: int):
    """Busca um aparelho pelo ID."""
    aparelhos = carregar_aparelhos_xml()
    
    for ap in aparelhos:
        if ap["id"] == id:
            return ap
            
    raise HTTPException(status_code=404, detail=f"Aparelho com ID {id} não encontrado.")


@app.put("/aparelhos/{id}", response_model=Aparelho, tags=["Aparelhos"])
def atualizar_aparelho(id: int, aparelho_novo: Aparelho):
    """Atualiza todas as informações de um aparelho existente pelo ID."""
    aparelhos = carregar_aparelhos_xml()
    aparelho_encontrado = None
    
    for i, ap in enumerate(aparelhos):
        if ap["id"] == id:
            aparelho_encontrado = i
            break
    
    if aparelho_encontrado is None:
        raise HTTPException(status_code=404, detail=f"Aparelho com ID {id} não encontrado.")

    if aparelho_novo.id != id:
        raise HTTPException(status_code=400, detail="O ID no corpo da requisição deve ser igual ao ID na URL.")

    aparelhos[aparelho_encontrado] = aparelho_novo.model_dump()
    salvar_aparelhos_xml(aparelhos)
    
    return aparelho_novo


@app.delete("/aparelhos/{id}", status_code=200, tags=["Aparelhos"])
def deletar_aparelho(id: int):
    """Deleta um aparelho pelo ID."""
    aparelhos = carregar_aparelhos_xml()
    
    aparelhos_atualizados = [ap for ap in aparelhos if ap["id"] != id]
    
    if len(aparelhos_atualizados) == len(aparelhos):
        raise HTTPException(status_code=404, detail=f"Aparelho com ID {id} não encontrado.")
    
    salvar_aparelhos_xml(aparelhos_atualizados)
    return {"message": f"Aparelho com ID {id} deletado com sucesso."}


@app.put("/aparelhos/{id}/transferir/{novo_deposito}", response_model=Aparelho, tags=["Aparelhos"])
def transferir_aparelho(id: int, novo_deposito: str):
    """Transfere um aparelho para um novo depósito."""
    aparelhos = carregar_aparelhos_xml()
    aparelho_encontrado = None
    
    for ap in aparelhos:
        if ap["id"] == id:
            ap["deposito"] = novo_deposito
            aparelho_encontrado = ap
            break
            
    if aparelho_encontrado is None:
        raise HTTPException(status_code=404, detail=f"Aparelho com ID {id} não encontrado.")

    salvar_aparelhos_xml(aparelhos)
    
    return aparelho_encontrado