import xml.etree.ElementTree as ET

def adicionar_contato():
    nome = input("Digite o nome do contato: ")
    telefone = input("Digite o número de telefone do contato: ")
    email = input("Digite o e-mail do contato: ")

    contato = ET.Element("contato")
    nome_elemento = ET.SubElement(contato, "nome")
    telefone_elemento = ET.SubElement(contato, "telefone")
    email_elemento = ET.SubElement(contato, "email")

    nome_elemento.text = nome
    telefone_elemento.text = telefone
    email_elemento.text = email

    try:
        tree = ET.parse("contatos.xml")
        root = tree.getroot()
    except FileNotFoundError:
        root = ET.Element("contatos")
        tree = ET.ElementTree(root)

    root.append(contato)

    tree.write("contatos.xml")

def listar_contatos():
    try:
        tree = ET.parse("contatos.xml")
        root = tree.getroot()
        contatos = root.findall("contato")

        print("\nLista de Contatos:")
        for contato in contatos:
            nome = contato.find("nome").text
            telefone = contato.find("telefone").text
            email = contato.find("email").text
            print(f"Nome: {nome}, Telefone: {telefone}, E-mail: {email}")
    except FileNotFoundError:
        print("Nenhum contato encontrado.")

def main():
    while True:
        print("\nMenu:")
        print("1. Adicionar novo contato")
        print("2. Listar contatos")
        print("3. Sair")
        escolha = input("Escolha uma opção: ")

        if escolha == "1":
            adicionar_contato()
            print("Contato adicionado com sucesso!")
        elif escolha == "2":
            listar_contatos()
        elif escolha == "3":
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()