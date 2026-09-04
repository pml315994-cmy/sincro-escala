from pathlib import Path


path_bd=Path("sincro-escala/BD") / "escala_bd.txt"
escalas=[]

def cadastrar_escala():
    escala=input("digite o nome do funcionario: ")
    with open(path_bd, "a", encoding="utf-8") as arquivo:  
        arquivo.write(f"{escala}\n")
    escalas.append(escala)
    print(f"O nome cadastrado foi: {escala}")
    print("======================================")
    print ("você gostaria de adicionar um novo funcionario?")
    print ("1. sim✅")
    print("2. não❌")
    seguir_cadastro=input ("Escolha uma opção")
    print("======================================")
    if seguir_cadastro=="1":
        cadastrar_escala()
    if seguir_cadastro=="2":
        print ("cadastro concluido")
