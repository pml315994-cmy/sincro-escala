from pathlib import Path

path_bd=Path("sincro-escala/BD") / "escala_bd.txt"
escalas=[]

def cadastrar_escalas():
    print("======================================")
    print("           CADASTRA ESCALA            ")                
    print("======================================")
    print("")
    listar_escalas()
    print("")
    escala= input("digite o nome da escala: ")
    with open(path_bd, "a", encoding="utf-8") as arquivo:  
        arquivo.write(f"{escala}\n")
    print(f"O nome cadastrado foi: {escala}")
    print("======================================")
    print ("você gostaria de adicionar uma nova escala?")
    print ("1. sim✅")
    print("2. não❌")
    seguir_cadastro=input ("Escolha uma opção")
    print("======================================")
    if seguir_cadastro=="1":
        cadastrar_escalas()
    if seguir_cadastro=="2":
        print ("cadastro concluido")

def listar_escalas():
    with open(path_bd, "r", encoding="utf-8") as arquivo:  
        for linha in arquivo:
            nome_limpo=linha.strip()
            if nome_limpo not in escalas:
                escalas.append(linha.strip())

    print ("\n".join(escalas))

def excluir_escala():
    listar_escalas()
    escala = input("qual escala voce deseja deletar: ")
    with open(path_bd, "r", encoding="utf-8") as arquivo:  
       nomes=arquivo.readlines()

    with open(path_bd, "w", encoding="utf-8") as arquivo:  
         for linha in nomes:
            if linha.strip() == escala:
                linha=""
            arquivo.write(linha) 
