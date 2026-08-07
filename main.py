funcionarios=[]
sair_do_sistema=False

def apresenta_menu():
    print("======================================")
    print("     SISTEMA DE GESTÃO DE ESCALAS")
    print("======================================")
    print("")
    print("1. Cadastrar funcionário📝")
    print("2. Listar funcionário📝📝")
    print("0. Sair ❌")  
    print("")
    opcao_menu = input("Escolha uma opção: ")
    return opcao_menu

def cadastrar_funcionarios():
    funcionario = input("digite o nome do funcionario: ")
    funcionarios.append(funcionario)
    print(f"O nome cadastrado foi: {funcionario}")
    print("======================================")
    print ("você gostaria de adicionar um novo funcionario?")
    print ("1. sim✅")
    print("2. não❌")
    seguir_cadastro=input ("Escolha uma opção")
    print("======================================")
    if seguir_cadastro=="1":
        cadastrar_funcionarios()
    if seguir_cadastro=="2":
        print ("cadastro concluido")
def listar_funcionarios():
    print("listando funcionarios")

def sair():
    print("saindo do sistema de gestão de escala⏏️")
#=======================================================================
while not sair_do_sistema:

    opcao_menu = apresenta_menu()

    match opcao_menu:
        case "1":
            cadastrar_funcionarios()
        case "2":
            listar_funcionarios()
        case "0":
            sair()
        case _:
            print("Opção Inválida.")
            
