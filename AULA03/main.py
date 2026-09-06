from mod_rh import cadastrar_colaborador, exibir_colaboradores #This imports the functions from mod_rh so we can use them in this file.

colaboradores = [] #This means the list starts out empty.

while True: 
    print("\n1 - Cadastrar")
    print("2 - Listar")
    print("0 - Sair")
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        nome = input("Nome: ")
        cargo = input("Cargo: ")
        salario = float(input("Salário: "))
        novo_colaborador = cadastrar_colaborador(nome, cargo, salario)
        colaboradores.append(novo_colaborador) #Append adds the new collaborator to the list, essentially
        print("Colaborador cadastrado com sucesso!")
    elif opcao == "2":
        exibir_colaboradores(colaboradores)
    elif opcao == "0":
        print("Encerrando o sistema...")
        break
    else:
        print("Opção inválida. Tente novamente.")

        #   Seems straightforward enough at a glance, right?
        #  The code is a simple command-line interface for managing
        #  a list of collaborators. It allows the user to add new collaborators,
        #  list existing ones, and exit the program.
        #  The functions `cadastrar_colaborador` and `exibir_colaboradores`
        #  are imported from the `mod_rh` to handle the creation and display of collaborator data.