import sys
import os
from par import run
version = "1.9.0"
data = "25/09/2025"

def main():
    print("="*80)
    print(f"Command {version} - {data}")
    if len(sys.argv) <= 1:
        print(f"Use 'run' para executar o script, 'run clock' para cronometar o tempo de execução.")
        line = 1
        codigo = ""
        while 1:
            newLine = input(f"{line} - ")
            if newLine[:3] == "run":
                modo = "clock" if newLine[3:9] == " clock" else ""
                run(codigo, modo, "\\")
                codigo = ""
                line = 1
            else:
                processNewLine = []
                for char in newLine:
                    if char == "\t":
                        processNewLine.extend([" "] * 4)
                    else:
                        processNewLine.append(char)
                codigo += ''.join(processNewLine)+"\n"
                line+=1
        sys.exit(1)

    else:
        nome = sys.argv[1]
        modo = sys.argv[2] if len(sys.argv) > 2 else "clock"
        if ".command" != nome[-8:]:
            print("tipo de arquivo errado! O script deve ser .command!")
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
    except:
       sys.exit(1)