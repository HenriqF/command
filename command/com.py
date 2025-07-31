import sys
from nos import *
from eval import *
import time as Time

class Parser:
    def __init__(self,varnodes, nodes, variaveis, indexNodes):
        self.varnodes = varnodes
        self.nodes = nodes
        self.variaveis = variaveis
        self.indexNodes = indexNodes

    def parse(self, code):
        linhas = [x for x in code.split("\n") if x.strip() != ""]

        for i, linha in enumerate(linhas):
            tokens = self.getTokens(linha)
            if not tokens:
                continue

            depth = tokens.pop(0)

            match tokens[0]:
                case "if":
                    tokens = [x for x in tokens if x != " "] 
                    if 1 >= len(tokens):
                        Erro(linha=[linha, i+1], tipo="Condicional sem argumento.")
                    self.nodes.append(ConditionalIf(pergunta=tokens[1:],corpo=None ,fim=None, depth=depth, linha=[linha, i+1]))

                case "elif":
                    tokens = [x for x in tokens if x != " "]
                    if 1 >= len(tokens):
                        Erro(linha=[linha, i+1], tipo="Condicional sem argumento.")
                    self.nodes.append(ConditionalElse(pergunta=tokens[1:],corpo=None, fim=None, depth=depth, linha=[linha, i+1]))

                case "else":
                    self.nodes.append(Else(corpo=None, fim=None, depth=depth, linha=[linha, i+1]))

                case "set":
                    tokens = [x for x in tokens if x != " "]

                    if 1 >= len(tokens):
                        Erro(linha=[linha, i+1], tipo="Comando set sem nome")
                    elif any(not char.isalpha() and char != "_" for char in tokens[1]):
                        Erro(linha=[linha, i+1], tipo="Caractere proibido no nome da variavel.")
                    elif 2 >= len(tokens):
                        Erro(linha=[linha, i+1], tipo="Comando set sem operação.")

                    self.nodes.append(Setter(setwho=tokens[1], setto=tokens[2:], depth=depth, linha=[linha, i+1]))

                    if tokens[1] not in self.variaveis:
                        self.varnodes.append(Variavel(nome=tokens[1], valor=None, linha=[linha, i+1]))
                        self.variaveis[tokens[1]] = self.varnodes[-1]

                case "show":
                    if " " in tokens:
                        tokens.remove(" ")
                    if 1 >= len(tokens):
                        Erro(linha=[linha, i+1], tipo="Comando show sem argumentos.")
                    if tokens.count('`') % 2 != 0:
                        Erro(linha=[linha, i+1], tipo="Quantia indevida de indicadores.")
                    self.nodes.append(Show(content=tokens[1:], depth=depth, linha=[linha, i+1]))

                case "#":
                    pass

                case _:
                    Erro(linha=[linha, i+1], tipo="Comando desconhecido.")
    
        self.meaningParse()
        return self
    
    def meaningParse(self):
        for i, node in enumerate(self.nodes):
            self.indexNodes[node] = i
            
        i = 0
        nodeCount = len(self.nodes)
        while i < nodeCount:
            if isinstance(self.nodes[i], Conditional):
                condDepth = self.nodes[i].depth
                if i+1 >= nodeCount or self.nodes[i+1].depth <= condDepth:
                    Erro(self.nodes[i].linha, tipo="Condicional sem corpo")
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

def execute(nodes, variaveis, nodesIndex):
    lastConditionalResult = {}
    i = 0 
    while i < len(nodes):
        node = nodes[i]

        if not isinstance(node, Conditional):
            lastConditionalResult[node.depth] = 1

        match node:
            case Setter():
                variaveis[node.setwho].valor = Eval(variaveis=variaveis, askNode=node).evaluate(node.setto)
                #print("set", variaveis[node.setwho].nome,"to", variaveis[node.setwho].valor)

            case Show():
                node.show(variaveis)

            case ConditionalIf():
                sucessoCondicional = Eval(variaveis=variaveis, askNode=node).evaluate(node.pergunta)
                lastConditionalResult[node.depth] = sucessoCondicional
                if sucessoCondicional == 1:
                    i = nodesIndex[node.corpo]-1
                else:
                    i = nodesIndex[node.fim]

            case ConditionalElse():
                if lastConditionalResult[node.depth] != 1:
                    sucessoCondicional = Eval(variaveis=variaveis, askNode=node).evaluate(node.pergunta)
                    lastConditionalResult[node.depth] = sucessoCondicional
                    if sucessoCondicional == 1:
                        i = nodesIndex[node.corpo]-1
                    else:
                        i = nodesIndex[node.fim]
                else:
                    i = nodesIndex[node.fim]

            case Else():
                if lastConditionalResult[node.depth] != 1:
                    lastConditionalResult[node.depth] = 1
                    i = nodesIndex[node.corpo]-1
                else:
                    i = nodesIndex[node.fim]
        i += 1
    return

startTime = Time.time()
astCommands = Parser(varnodes=[], nodes=[],variaveis={}, indexNodes={}).parse(open("test.command").read())
parseTime = Time.time()-startTime

startTime = Time.time()
execute(nodes=astCommands.nodes, variaveis=astCommands.variaveis, nodesIndex=astCommands.indexNodes)
execTime = Time.time()-startTime

print("\nTempo de parse:", parseTime, "s")
print("Tempo de execução:" ,execTime, "s")