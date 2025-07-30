import sys
from nos import *
from eval import *
import time as Time

class Parser:
    def __init__(self,varnodes, nodes, variaveis):
        self.varnodes = varnodes
        self.nodes = nodes
        self.variaveis = variaveis

    def parse(self, code):
        linhas = [x for x in code.split("\n") if x.strip() != ""]

        for linha in linhas:
            tokens = self.getTokens(linha)
            if not tokens:
                continue

            depth = tokens.pop(0)

            match tokens[0]:
                case "if":
                    tokens = [x for x in tokens if x != " "] 
                    if 1 >= len(tokens):
                        raise Exception(f"""Condicional sem argumento. --> "{linha}", linha {linhas.index(linha)+1}""")
                    self.nodes.append(Conditional(pergunta=tokens[1:],corpo=None ,fim=None, depth=depth))

                case "elif":
                    tokens = [x for x in tokens if x != " "]
                    if 1 >= len(tokens):
                        raise Exception(f"""Condicional sem argumento. --> "{linha}", linha {linhas.index(linha)+1}""")
                    self.nodes.append(ConditionalElse(pergunta=tokens[1:],corpo=None, fim=None, depth=depth))

                case "else":
                    self.nodes.append(Else(corpo=None, fim=None, depth=depth))

                case "set":
                    tokens = [x for x in tokens if x != " "]

                    if 1 >= len(tokens):
                        raise Exception(f"""Comando set sem nome. --> "{linha}", linha {linhas.index(linha)+1}""")

                    if any(char not in  "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz_" for char in tokens[1]):
                        raise Exception(f"""Caractere proibido no nome da variavel. --> "{linha}", linha {linhas.index(linha)+1}""")
                    
                    if 2 >= len(tokens):
                        raise Exception(f"""Comando set sem operação. --> "{linha}", linha {linhas.index(linha)+1}""")
                    
                    self.nodes.append(Setter(setwho=tokens[1], setto=tokens[2:], depth=depth))

                    if tokens[1] not in self.variaveis:
                        self.varnodes.append(Variavel(nome=tokens[1], valor=None))
                        self.variaveis[tokens[1]] = self.varnodes[-1]

                case "show":
                    if " " in tokens:
                        tokens.remove(" ")
                    if 1 >= len(tokens):
                        raise Exception(f"""Comando show sem argumentos. --> "{linha}", linha {linhas.index(linha)+1}""")
                    if tokens.count('`') % 2 != 0:
                        raise Exception(f"""Quantia indevida de indicadores --> "{linha}", linha {linhas.index(linha)+1}""")
                    self.nodes.append(Show(content=tokens[1:], depth=depth))

                case "#":
                    pass

                case _:
                    raise Exception(f"""Comando desconhecido. --> "{tokens[0]}", linha {linhas.index(linha)+1}""")
    
        self.meaningParse()
        return self
    
    def meaningParse(self):
        # for node in self.nodes:
        #     print(node)
        i = 0
        nodeCount = len(self.nodes)
        while i < nodeCount:
            if type(self.nodes[i]) in [Conditional,ConditionalElse,Else]:
                condDepth = self.nodes[i].depth
                if i+1 >= nodeCount or self.nodes[i+1].depth <= condDepth:
                    raise Exception(f"""Condicional sem corpo.""")
                else:
                    self.nodes[i].corpo = self.nodes[i+1]
                    j = i+2
                    while j < nodeCount:
                        if self.nodes[j].depth <= condDepth:
                            self.nodes[i].fim = self.nodes[j-1]
                            break
                        j += 1
                    if self.nodes[i].fim == None:
                        self.nodes[i].fim = self.nodes[j-1]

            i += 1
        pass

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

        depth = 0
        spaceCount = 0
        while tokens[0] == " ":
            tokens.pop(0)
            spaceCount += 1
            if spaceCount == 4:
                depth += 1
                spaceCount = 0
        tokens.insert(0, depth)
        return(tokens)

def execute(nodes, variaveis):
    lastConditionalResult = {}
    i = 0 
    while i < len(nodes):
        node = nodes[i]
        if type(node) is Setter:
            variaveis[node.setwho].valor = Eval(variaveis).evaluate(node.setto)
            #print("set", variaveis[node.setwho].nome,"to", variaveis[node.setwho].valor)

        elif type(node) is Show:
            node.show(variaveis)

        elif type(node) is Conditional:
            sucessoCondicional = Eval(variaveis).evaluate(node.pergunta)
            lastConditionalResult[node.depth] = sucessoCondicional
            if sucessoCondicional == 1:
                i = nodes.index(node.corpo)-1 
            else:
                i = nodes.index(node.fim)

        elif type(node) is ConditionalElse:
            if lastConditionalResult[node.depth] != 1:
                sucessoCondicional = Eval(variaveis).evaluate(node.pergunta)
                lastConditionalResult[node.depth] = sucessoCondicional
                if sucessoCondicional == 1:
                    i = nodes.index(node.corpo)-1 
                else:
                    i = nodes.index(node.fim)
            else:
                i = nodes.index(node.fim)

        elif type(node) is Else:
            if lastConditionalResult[node.depth] != 1:
                lastConditionalResult[node.depth] = 1
                i = nodes.index(node.corpo)-1
            else:
                i = nodes.index(node.fim)
        i += 1
    return

startTime = Time.time()
astCommands = Parser(varnodes=[], nodes=[],variaveis={}).parse(open("test.command").read())
parseTime = Time.time()-startTime

startTime = Time.time()
execute(astCommands.nodes, astCommands.variaveis)
execTime = Time.time()-startTime

print("\nTempo de parse:", parseTime, "s")
print("Tempo de execução:" ,execTime, "s")