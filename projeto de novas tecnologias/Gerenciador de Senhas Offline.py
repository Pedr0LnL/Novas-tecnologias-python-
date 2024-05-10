import os
import json
from cryptography.fernet import Fernet

# Função para gerar uma chave de criptografia
def gerar_chave():
    return Fernet.generate_key()

# Função para carregar a chave de um arquivo ou gerar uma nova
def carregar_ou_gerar_chave():
    chave_arquivo = "chave.key"
    if os.path.exists(chave_arquivo):
        with open(chave_arquivo, "rb") as chave_file:
            chave = chave_file.read()
    else:
        chave = gerar_chave()
        with open(chave_arquivo, "wb") as chave_file:
            chave_file.write(chave)
    return chave

# Função para criptografar dados
def criptografar_dados(dados, chave):
    f = Fernet(chave)
    return f.encrypt(dados.encode())

# Função para descriptografar dados
def descriptografar_dados(dados_criptografados, chave):
    f = Fernet(chave)
    return f.decrypt(dados_criptografados).decode()

# Função para adicionar uma nova senha
def adicionar_senha(sites, usuario, senha, chave):
    sites[usuario] = criptografar_dados(senha, chave)
    print("Senha adicionada com sucesso!")

# Função para visualizar uma senha
def visualizar_senha(sites, usuario, chave):
    if usuario in sites:
        senha = descriptografar_dados(sites[usuario], chave)
        print(f"Senha para o usuário '{usuario}': {senha}")
    else:
        print("Usuário não encontrado!")

# Função para atualizar uma senha
def atualizar_senha(sites, usuario, senha, chave):
    if usuario in sites:
        sites[usuario] = criptografar_dados(senha, chave)
        print("Senha atualizada com sucesso!")
    else:
        print("Usuário não encontrado!")

# Função principal
def main():
    chave = carregar_ou_gerar_chave()

    # Carregar os dados do arquivo (se existir)
    arquivo_dados = "senhas.json"
    if os.path.exists(arquivo_dados):
        with open(arquivo_dados, "r") as file:
            sites = json.load(file)
    else:
        sites = {}

    while True:
        print("\n1. Adicionar senha")
        print("2. Visualizar senha")
        print("3. Atualizar senha")
        print("4. Sair")
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            usuario = input("Digite o usuário: ")
            senha = input("Digite a senha: ")
            adicionar_senha(sites, usuario, senha, chave)
        elif opcao == "2":
            usuario = input("Digite o usuário: ")
            visualizar_senha(sites, usuario, chave)
        elif opcao == "3":
            usuario = input("Digite o usuário: ")
            senha = input("Digite a nova senha: ")
            atualizar_senha(sites, usuario, senha, chave)
        elif opcao == "4":
            # Salvar os dados no arquivo antes de sair
            with open(arquivo_dados, "w") as file:
                json.dump(sites, file)
            print("Saindo...")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()
