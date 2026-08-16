import os
import csv
import sys

# declaracao de variavel global 
lista_msg = []

def carregar_mensagens(csv_path):
    mensagens_arquivo = {}

    with open(csv_path, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            arquivo = row['arquivo']
            mensagem = row['mensagem'].lower()
            # acao = row['acao'].lower()

            if arquivo not in mensagens_arquivo:
                mensagens_arquivo[arquivo] = set()

            mensagens_arquivo[arquivo].add(mensagem)

    return mensagens_arquivo

def confere_diferente(mensagens1,linha1):
    resultado = ""
    qtde = 0
    for msg in mensagens1:
        if msg.casefold() in linha1.casefold():
            qtde += 1
        else:
            resultado = linha1
    if qtde > 0:
        resultado = ""
    return resultado

def confere_igual(mensagens1,linha1):
    resultado = ""
    for msg in mensagens1:
        # divide a mensagem em mensagem e acao. Exemplo: backup successfull * igual
        msg_acao = msg.split("*")
        # o indice da lista comeca em zero. 
        # msg_acao[0] = mensagem
        # msg_acao[1] = acao
        if msg_acao[1] == "igual":
            if msg_acao[0].casefold() in linha1.casefold():
               resultado = linha1
               break
        else:
            if msg.casefold() in linha1.casefold():
                qtde += 1
            else:
                resultado = linha1
            if qtde > 0:
                resultado = ""

    return resultado

def analise_diretorio_diferente(diretorio, mensagens_arquivo):
    for nome_arquivo in os.listdir(diretorio):
        if ((not nome_arquivo.lower().endswith('.txt')) and (not nome_arquivo.lower().endswith('.log'))):
            continue

        caminho = os.path.join(diretorio, nome_arquivo)
        mensagens_permitidas = mensagens_arquivo.get(nome_arquivo, set())
        
        with open(caminho, 'r', encoding='utf-8', errors='ignore') as f:
            for linha in f:
                if len(linha) > 1 :
                    # carregar as palavras POSSIVEIS correspondentes a esse arquivo
                    mensagens_permitidas = mensagens_arquivo.get(nome_arquivo, set())
                    texto = confere_diferente(mensagens_permitidas,linha)                 
                    if texto != "":
                        lista_msg.append(f"[{caminho}] - {texto}")


def analise_diretorio(diretorio, mensagens_arquivo, igual_ou_diferente):
    for nome_arquivo in os.listdir(diretorio):
        if ((not nome_arquivo.lower().endswith('.txt')) and (not nome_arquivo.lower().endswith('.log'))):
            continue

        caminho = os.path.join(diretorio, nome_arquivo)
        mensagens_permitidas = mensagens_arquivo.get(nome_arquivo, set())

        with open(caminho, 'r', encoding='utf-8', errors='ignore') as f:
            for linha in f:
                if (len(linha) > 2):
                    # carregar as palavras POSSIVEIS correspondentes a esse arquivo
                    mensagens_permitidas = mensagens_arquivo.get(nome_arquivo, set())
                    if igual_ou_diferente == "igual":
                        # procura mensagens no LOG iguais aos que foram listadas no arquivo CSV
                        for msg in mensagens_permitidas:
                            if msg.casefold() in linha.casefold():
                                lista_msg.append(f"[{caminho}] - {linha}")
                    else:
                        # lista somente as mensagens do LOG que sao diferentes das listadas no arquivo CSV
                        texto = confere_diferente(mensagens_permitidas,linha)                 
                        if texto != "":
                            lista_msg.append(f"[{caminho}] - {texto}")
                     
"""
                    if igual_ou_diferente == "igual":
                        # procura mensagens no LOG iguais aos que foram listadas no arquivo CSV
                        for msg in mensagens_permitidas:
                            if msg.casefold() in linha.casefold():
                                lista_msg.append(f"[{caminho}] - {linha}")
                    else:
                        # lista somente as mensagens do LOG que sao diferentes das listadas no arquivo CSV
                        texto = confere_diferente(mensagens_permitidas,linha)                 
                        if texto != "":
                            lista_msg.append(f"[{caminho}] - {texto}")
"""
# PRINCIPAL
if __name__ == "__main__":
    if len(sys.argv) != 4:
        print(f"Uso: python analisar.py <diretorio_log> <mensagens.csv> <igual/diferente>")
        sys.exit(1)

    diretorio_log = sys.argv[1]
    arquivo_csv = sys.argv[2]
    # verifica se vai procurar por frases iguais aos dos arquivos de mensagens ou se vai listar as linhas diferentes dos arquivos de mensagens
    igual_ou_diferente = sys.argv[3]
    lista_msg.clear()
    mensagens_arquivo = carregar_mensagens(arquivo_csv)
    analise_diretorio(diretorio_log, mensagens_arquivo, igual_ou_diferente)
    if lista_msg:
        for item_lista in lista_msg:
            print(item_lista) 
   
