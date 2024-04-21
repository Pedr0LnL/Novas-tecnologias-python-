import csv

def apaga(agenda, nome):
    if nome in agenda:
        del agenda[nome]
        print("Contato '{}' apagado com sucesso.".format(nome))
    else:
        print("Contato '{}' não encontrado na agenda.".format(nome))

def altera(agenda, nome):
    if nome in agenda:
        novo_nome = input("Novo nome: ")
        novo_tel = input("Novo telefone: ")
        novo_aniversario = input("Nova data de aniversário: ")
        novo_email = input("Novo email: ")
        novo_tipo_tel = input("Novo tipo de telefone (celular, fixo, residência ou trabalho): ")
        agenda[novo_nome] = {'telefone': novo_tel, 'aniversario': novo_aniversario, 'email': novo_email, 'tipo_telefone': novo_tipo_tel}
        del agenda[nome]
        print("Contato '{}' alterado com sucesso.".format(nome))
    else:
        print("Contato '{}' não encontrado na agenda.".format(nome))

def lista_nomes(agenda):
    for i, nome in enumerate(agenda.keys()):
        print("{} - {}".format(i+1, nome))

def busca(agenda, nome):
    if nome in agenda:
        print("Detalhes do contato '{}':".format(nome))
        print("Telefone:", agenda[nome]['telefone'])
        print("Data de Aniversário:", agenda[nome]['aniversario'])
        print("Email:", agenda[nome]['email'])
        print("Tipo de Telefone:", agenda[nome]['tipo_telefone'])
    else:
        print("Contato '{}' não encontrado na agenda.".format(nome))

def grava_csv(agenda, arquivo):
    with open(arquivo, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Nome', 'Telefone', 'Aniversário', 'Email', 'Tipo de Telefone'])
        for nome, info in agenda.items():
            writer.writerow([nome, info['telefone'], info['aniversario'], info['email'], info['tipo_telefone']])
    print("Agenda gravada com sucesso.")

def carrega_csv(arquivo):
    agenda = {}
    try:
        with open(arquivo, 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)  # Pula o cabeçalho
            for row in reader:
                nome, telefone, aniversario, email, tipo_telefone = row
                agenda[nome] = {'telefone': telefone, 'aniversario': aniversario, 'email': email, 'tipo_telefone': tipo_telefone}
        print("Agenda carregada com sucesso.")
        return agenda
    except FileNotFoundError:
        print("Arquivo não encontrado. Criando uma nova agenda.")
        return {}

def menu():
    print("\n--- Agenda ---")
    print("1. Adicionar contato")
    print("2. Apagar contato")
    print("3. Alterar contato")
    print("4. Lista de nomes")
    print("5. Buscar contato")
    print("6. Gravar agenda como CSV")
    print("7. Carregar agenda de CSV")
    print("8. Tamanho da agenda")
    print("9. Ordenar agenda por nome")
    print("10. Sair")
    return input("Escolha uma opção: ")

def main():
    agenda = {}
    while True:
        opcao = menu()
        if opcao == '1':
            nome = input("Nome: ")
            if nome in agenda:
                print("Erro: Já existe um contato com o nome '{}' na agenda.".format(nome))
            else:
                tel = input("Telefone: ")
                aniversario = input("Data de aniversário: ")
                email = input("Email: ")
                tipo_tel = input("Tipo de telefone (celular, fixo, residência ou trabalho): ")
                agenda[nome] = {'telefone': tel, 'aniversario': aniversario, 'email': email, 'tipo_telefone': tipo_tel}
        elif opcao == '2':
            nome = input("Nome do contato a ser apagado: ")
            apaga(agenda, nome)
        elif opcao == '3':
            nome = input("Nome do contato a ser alterado: ")
            altera(agenda, nome)
        elif opcao == '4':
            lista_nomes(agenda)
        elif opcao == '5':
            nome = input("Nome do contato a ser buscado: ")
            busca(agenda, nome)
        elif opcao == '6':
            arquivo = input("Nome do arquivo para gravar a agenda (com extensão .csv): ")
            grava_csv(agenda, arquivo)
        elif opcao == '7':
            arquivo = input("Nome do arquivo para carregar a agenda (com extensão .csv): ")
            agenda = carrega_csv(arquivo)
        elif opcao == '8':
            print("Tamanho da agenda:", len(agenda))
        elif opcao == '9':
            agenda_ordenada = sorted(agenda.items())
            print("Agenda ordenada por nome:")
            for nome, info in agenda_ordenada:
                print(nome, "-", info)
        elif opcao == '10':
            print("Saindo...")
            break
        else:
            print("Opção inválida.")

if __name__ == "__main__":
    main()

