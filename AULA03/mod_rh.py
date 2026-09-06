def cadastrar_colaborador(nome: str, cargo: str, salario: float) -> dict: #Dict means dictionary. In this case, it will store the collaborator's information.
    colaborador = {
        "nome": nome,
        "cargo": cargo,
        "salario": salario
    }
    return colaborador

def exibir_colaboradores(lista_colaboradores: list) -> None: #None means the function doesn't return anything. It just performs an action, which in this case is displaying the collaborators.
    if not lista_colaboradores:
        print("Nenhum colaborador cadastrado.")
        return
    for colaborador in lista_colaboradores:
        print(f"Nome: {colaborador['nome']} | Cargo: {colaborador['cargo']} | Salário: R${colaborador['salario']:.2f}")

        #   Here, both "dict" and "none" are type hints,
        #  which is a way to indicate what type of data is expected.
        #  It doesn't affect how the code runs,
        #  but it can help with readability and debugging.
