import sys
import os
from par import run
version = "2.1.2"
data = "21/11/2025"

def editor() -> None:
    print(f"Command {version} - {data} ")
    print("Digite 'ajuda' para saber mais.")

    codigo = []
    while 1:
        newLine = input(f"- ")
        if newLine == "run":
            try:
                run(codigo='\n'.join(codigo), modo="", path="\\")
            except SystemExit:
                pass
            codigo = []
        elif newLine == "ajuda":
            print("\nDigite run para executar o script.")
            print("Digite forget para limpar o script atual.")
            print("Para sair, digite quit ou use Control+C")
        elif newLine == "forget":
            codigo = []
        elif newLine == "quit":
            break
        else:
            newLine = newLine.expandtabs(4)
            codigo.append(newLine)
        
    sys.exit(0)

def main() -> None:
    if len(sys.argv) <= 1:
        editor()
    else:
        nome = sys.argv[1]
        modo = "normal"

        if nome.endswith(".ccommand"):
            modo = "clock"
        elif nome.endswith(".command"):
            pass
        elif (os.path.exists(nome+".ccommand")):
            nome = nome+".ccommand"
            modo = "clock"
        elif (os.path.exists(nome+".command")):
            nome = nome+".command"
        else:
            print("Arquivo .command não existe!")
            sys.exit(1)

        try:
            path = os.path.dirname(os.path.abspath(nome))
            with open(nome, 'r') as f:
                codigo = f.read()
        except:
            print("Esse arquivo não existe!")
            sys.exit(1)

        run(codigo, modo, path)
        sys.exit(1)

if __name__ == "__main__":
    try:
        main()
    except SystemExit:
        raise 
    except:
       sys.exit(1)