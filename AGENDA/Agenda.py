def salvar_contatos(lista):
    arquivo = open("contatos.txt", "w")

    for contato in lista:
        arquivo.write("{}#{}#{}\n".format(contato['nome'], contato['email'], contato['telefone']))

    arquivo.close()

def carregar_contatos():
    lista = []

    try:
        arquivo = open("contatos.txt", "r")

        for linha in arquivo.readlines():
            coluna = linha.strip().split("#")

            contato = {
                "email": coluna[1],
                "nome": coluna[0],
                "telefone": coluna[2]
            }

            lista.append(contato)

        arquivo.close()
    except FileNotFoundError:
        pass

    return lista

def existe_contato(lista, email):
    if len(lista)> 0:
        for contato in lista:
            if contato['email'] == email:
                return True

        return False

def adicionar(lista):

    while True:
        email = input("Digite o e-mail do contato: ")

        if not existe_contato(lista, email):
            break
        else:
            print("Esse e-mail já foi utilizado.")
            print("Por favor, tente um nvo e-mail.")

    # nesse passo, o e-mail recebido sera unico

    contato = {
        "email": email,
        "nome": input("Digite o nome: "),
        "telefone": input("Digite o numero: ")
    }

    lista.append(contato)

    print("O contato foi cadastrado com sucesso!\n".format(contato['nome']))

def alterar(lista):
    print(" == ALTERAR CONTATO == ")
    if len(lista) > 0:
        email = input("Digite o e-mail do contato a ser encontrado: ")
        if existe_contato(lista, email):
            print("O contato foi encontrado. As informações seguem abaixo: ")
            for contato in lista:
                if contato['email'] == email:
                    print("Nome: {}".format(contato['nome']))
                    print("Email: {}".format(contato['email']))
                    print("Telefone: {}".format(contato['telefone']))
                    print("===============================================\n")

                    contato['nome'] = input("Digite o novo nome do contato: ")
                    contato['telefone'] = input("Digite o novo telefone do contato: ")

                    print("Os dados do contato com email {}, foram alterados com sucesso!".format(contato['email']))
                    break
        else:
            print("Não existe contato cadastrado no sistema com o email {}.\n".format(email))


    else:
        print("Não existe nenhum contato cadastrado no sistema.\n")


def excluir(lista):
    print(" == EXCLUIR CONTATO == ")
    if len(lista) > 0:
        email = input("Digite o e-mail do contato a ser excluido: ")
        if existe_contato(lista, email):
            print("O contato foi encontrado. As informações seguem abaixo: ")
            for item, contato in enumerate(lista):
                if contato['email'] == email:
                    print("Nome: {}".format(contato['nome']))
                    print("Email: {}".format(contato['email']))
                    print("Telefone: {}".format(contato['telefone']))
                    print("===============================================\n")

                    del lista[item]

                    print("O contato foi excluido com sucesso!")
                    break

        else:
            print("Não existe contato cadastrado no sistema com o email {}.\n".format(email))


    else:
        print("Não existe nenhum contato cadastrado no sistema.\n")


def buscar(lista):
    print(" == BUSCAR CONTATO == ")
    if len(lista) > 0:
        email = input("Digite o e-mail do contato a ser encontrado: ")
        if existe_contato(lista, email):
            print("O contato foi encontrado. As informações seguem abaixo: ")
            for contato in lista:
                if contato['email'] == email:
                    print("Nome: {}".format(contato['nome']))
                    print("Email: {}".format(contato['email']))
                    print("Telefone: {}".format(contato['telefone']))
                    print("===============================================\n")
                    break
        else:
            print("Não existe contato cadastrado no sistema com o email {}.\n".format(email))


    else:
        print("Não existe nenhum contato cadastrado no sistema.\n")


def listar(lista):
    print(" == LISTA DE CONTATOS == ")
    if len(lista) > 0:
        for item, contato in enumerate(lista):
            print("Contato {}:".format(item+1))
            print("\tNome: {}".format(contato['nome']))
            print("\tEmail: {}".format(contato['email']))
            print("\tTelefone: {}".format(contato['telefone']))
            print("===============================================")

        print("Quantidade de contatos: {}\n".format(len(lista)))

    else:
        print("Não existe nenhum contato cadastrado no sistema.\n")


def principal():

    lista = carregar_contatos()        # inicializando lista de contatos

    while True:
        print(" === Agenda telefonica === ")
        print(" 1 - Adicionar contato")
        print(" 2 - Alterar contato")
        print(" 3 - Excluir contato")
        print(" 4 - Buscar contato")
        print(" 5 - Listar contatos")
        print(" 6 - Sair")
        opcao = int(input(">>> "))

        if opcao == 1:
            adicionar(lista)
            salvar_contatos(lista)
        elif opcao == 2:
            alterar(lista)
            salvar_contatos(lista)
        elif opcao == 3:
            excluir(lista)
            salvar_contatos(lista)
        elif opcao == 4:
            buscar(lista)
        elif opcao == 5:
            listar(lista)
        elif opcao == 6:
            print(" Saindo do programa...")
            break
        else:
            print("Opção escolhida é invalida. Por favor, tente novamente.")



principal()