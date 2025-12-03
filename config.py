import configparser

# Cria um objeto ConfigParser
config = configparser.ConfigParser()

# Adiciona as propriedades (chave-valor)
config['DEFAULT'] = {
    'arquivo': 'estoque.xml',
}

# Tenta gravar as propriedades no arquivo "config.ini"
try:
    with open('config.ini', 'w') as configfile:
        config.write(configfile)
    print("Arquivo 'config.ini' criado com sucesso.")
except Exception as e:
    print(f"Erro ao escrever o arquivo config.ini: {e}")