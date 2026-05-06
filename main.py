import pandas as pd
from sqlalchemy import create_engine

# 1. Configuração da conexão (Substitua 'SUA_SENHA' pela sua senha do MySQL)
import urllib.parse
password = urllib.parse.quote_plus("Cacau@2212")
engine = create_engine(f"mysql+pymysql://root:{password}@localhost/projeto_automacao")

try:
    # 2. EXTRAÇÃO: Lendo o arquivo CSV
    print("Lendo dados do estoque...")
    df = pd.read_csv('dados_estoque.csv')

    # 3. TRANSFORMAÇÃO: Padronizando os nomes para maiúsculas
    df['nome_produto'] = df['nome_produto'].str.upper()

    # 4. CARGA: Enviando os dados para o MySQL
    print("Iniciando carga no banco de dados...")
    df.to_sql('tb_estoque', con=engine, if_exists='append', index=False)
    
    print("Automação concluída com sucesso! Verifique seu MySQL Workbench.")

except Exception as e:
    print(f"Ocorreu um erro: {e}")