import sys
from nos import *
from eval import *
import time as Time

class Parser:
    def __init__(self, nodes, variaveis):
        self.nodes = nodes
        self.variaveis = variaveis

    def parse(self, code):

        linhas = [x for x in code.split("\n") if x.strip() != ""]

        for linha in linhas:
            tokens = self.getTokens(linha)
            match tokens[0]:
                case "set":
                    tokens = [x for x in tokens if x != " "]

                    if 1 >= len(tokens):
                        raise Exception(f"""Comando set sem nome. --> "{linha}", linha {linhas.index(linha)+1}""")

                    if any(char not in  "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz_" for char in tokens[1]):
                        raise Exception(f"""Caractere proibido no nome da variavel. --> "{linha}", linha {linhas.index(linha)+1}""")
                    
                    if 2 >= len(tokens):
                        raise Exception(f"""Comando set sem operação. --> "{linha}", linha {linhas.index(linha)+1}""")
                    
                    self.nodes.append(Setter(tokens[1], tokens[2:]))

                    if tokens[1] not in self.variaveis:
                        self.nodes.append(Variavel(tokens[1], None))
                        self.variaveis[tokens[1]] = self.nodes[-1]

                case "show":
                    if " " in tokens:
                        tokens.remove(" ")
                    if 1 >= len(tokens):
                        raise Exception(f"""Comando show sem argumentos. --> "{linha}", linha {linhas.index(linha)+1}""")
                    if tokens.count('`') % 2 != 0:
                        raise Exception(f"""Quantia indevida de indicadores --> "{linha}", linha {linhas.index(linha)+1}""")
                    self.nodes.append(Show(tokens[1:]))

                case "#":
                    pass


                case _:
                    raise Exception(f"""Comando desconhecido. --> "{tokens[0]}", linha {linhas.index(linha)+1}""")
    
        return self
    

    def getTokens(self, linha):
        tokens = []
        current = ""
        i = 0 
        def format(token):
            try:
                token = float(token)
                if token.is_integer():
                    return(int(token))
                else:
                    return(float(token))
            except:
                return(token)

        while i < len(linha):
            char = linha[i]
            if char.isnumeric() or char in ".":
                current+=char
            elif char.isalpha():
                current+=char
            else:
                if current != "":
                    tokens.append(format(current))
                current = ""
                if char != "":
                    tokens.append(char)
            i += 1
        if current != "" and current != " ":
            tokens.append(format(current))
        return(tokens)


def execute(nodes, variaveis):
    for node in nodes:
        if type(node) is Setter:
            variaveis[node.setwho].valor = Eval(variaveis).evaluate(node.setto)
            #print("set", variaveis[node.setwho].nome,"to", variaveis[node.setwho].valor)
        if type(node) is Show:
            node.show(variaveis)
    return




startTime = Time.time()
astCommands = Parser(nodes=[],variaveis={}).parse(open("test.command").read())
parseTime = Time.time()-startTime



startTime = Time.time()
execute(astCommands.nodes, astCommands.variaveis)
execTime = Time.time()-startTime

print("\nTempo de parse:", parseTime, "s")
print("Tempo de execução:" ,execTime, "s")
