class Contato:
    def __init__(self, nome, telefone, endereco, email=''):
        self.nome = nome
        self.telefone = telefone
        self.endereco = endereco
        self.email = email

    def __str__(self):
        return f"Nome: {self.nome}\nTelefone: {self.telefone}\nEndereço: {self.endereco}\nEmail: {self.email}\n"

class Agenda:
    def __init__(self):
        self.contatos = []

    def adicionar_contato(self, contato):
        self.contatos.append(contato)

    def buscar_contato(self, nome):
        for contato in self.contatos:
            if contato.nome.lower() == nome.lower():
                return contato
        return None

    def remover_contato(self, nome):
        contato = self.buscar_contato(nome)
        if contato:
            self.contatos.remove(contato)
            print(f"Contato {nome} removido com sucesso.")
        else:
            print(f"Contato {nome} não encontrado na agenda.")

    def listar_contatos(self):
        if self.contatos:
            print("Lista de contatos:")
            for contato in self.contatos:
                print(contato)
        else:
            print("Nenhum contato na agenda.")

# Função para exibir o menu de opções
def exibir_menu():
    print("\nMenu de opções:")
    print("1. Adicionar contato")
    print("2. Buscar contato")
    print("3. Remover contato")
    print("4. Listar contatos")
    print("0. Sair")

# Exemplo de uso interativo
agenda = Agenda()

while True:
    exibir_menu()
    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        nome = input("Digite o nome do contato: ")
        telefone = input("Digite o telefone do contato: ")
        endereco = input("Digite o endereço do contato: ")
        email = input("Digite o email do contato (opcional): ")
        contato = Contato(nome, telefone, endereco, email)
        agenda.adicionar_contato(contato)
        print("Contato adicionado com sucesso.")

    elif opcao == '2':
        nome = input("Digite o nome do contato a ser buscado: ")
        contato = agenda.buscar_contato(nome)
        if contato:
            print("Contato encontrado:")
            print(contato)
        else:
            print("Contato não encontrado.")

    elif opcao == '3':
        nome = input("Digite o nome do contato a ser removido: ")
        agenda.remover_contato(nome)

    elif opcao == '4':
        agenda.listar_contatos()

    elif opcao == '0':
        print("Saindo...")
        break

    else:
        print("Opção inválida. Por favor, escolha uma opção válida.")
