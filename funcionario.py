from pathlib import Path

path_bd=Path("sincro-escala/BD") / "funcionario_bd.txt"
funcionarios=[]

def cadastrar_funcionarios():
    funcionario = input("digite o nome do funcionario: ")
    with open(path_bd, "a", encoding="utf-8") as arquivo:  
        arquivo.write(f"{funcionario}\n")
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
    with open(path_bd, "r", encoding="utf-8") as arquivo:  
        for linha in arquivo:
            print (linha.strip())

def excluir_funcionario():
    listar_funcionarios()
    funcionario = input("qual funcionario voce deseja deletar: ")
    with open(path_bd, "r", encoding="utf-8") as arquivo:  
       nomes=arquivo.readlines()

    with open(path_bd, "w", encoding="utf-8") as arquivo:  
         for linha in nomes:
            if linha.strip() == funcionario:
                linha=""
            arquivo.write(linha) 
