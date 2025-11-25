import sys
import os
from par import run
version = "2.3.0"
data = "24/11/2025"

def editor() -> None:
    print(f"\033[34mCommand {version}\033[0m - {data} ")
    print("Digite \033[34majuda\033[0m para saber mais.")

    codigo = []
    while 1:
        newLine = input(f"- ")
        command = newLine.lstrip('\t')
        if command == "run":
            print('\033[F\033[K', end='')
            try:
                run(codigo='\n'.join(codigo), modo="", path="\\")
            except SystemExit:
                pass
            except KeyboardInterrupt:
                pass
            codigo = [] 
        elif command == "ajuda":
            print("\nDigite \033[34mrun\033[0m para executar o script.")
            print("Digite \033[34mforget\033[0m para limpar a ultima linha de código digitada.")
            print("Para \033[34msair\033[0m, digite sair ou use Control+C")
        elif command == "forget":
            if codigo:
                codigo.pop()
                print('\033[F\033[K', end='')
            print('\033[F\033[K', end='')
        elif command == "sair":
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