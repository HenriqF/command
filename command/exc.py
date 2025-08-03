import sys
from nos import *
from eval import *
import time as Time


def execute(nodes, variaveis, funcoes, nodesIndex):
    environment = [variaveis]
    lastConditionalResult = {}
    i = 0 
    while i < len(nodes):
        node = nodes[i]
        if not isinstance(node, (Conditional, Loop, Dummy)):
            lastConditionalResult[node.depth] = 1
        match node:

            case Result():
                if node.funcaoPai is None:
                    Erro(linha=node.linha, tipo="Result sem função.")
                if node.varRetorno is not None:
                    if node.varRetorno not in environment[-1]:
                        Erro(linha=node.linha, tipo="Result de variável não declarada")
                    node.valor = environment[-1][node.varRetorno].valor
                funcoes[node.funcaoPai].caller.valor = node.valor

                environment.pop()
                i = nodesIndex[funcoes[node.funcaoPai].caller]

            case Function():
                i = nodesIndex[node.fim]

            case Execute():
                if node.execWho in funcoes:
                    newEnv = {}
                    for env in funcoes[node.execWho].environment:
                        newEnv[env] = funcoes[node.execWho].environment[env].copy()
                    environment.append(newEnv)
                    funcoes[node.execWho].caller = node
                    i = nodesIndex[funcoes[node.execWho].corpo]-1
                else:
                    Erro(linha=node.linha, tipo="Funcao inexistente.")

            case Apply():
                prevIndex = nodesIndex[node]-1
                if node.variavel not in environment[-1]:
                    Erro(linha=node.linha, tipo="Apply em variavel não declarada.")
                if not isinstance(nodes[prevIndex], Execute):
                    Erro(linha=node.linha, tipo="Comando antes de apply não é execute.")

                environment[-1][node.variavel].valor = nodes[prevIndex].valor

                


            case WhileLoop():
                sucessoCondicional = Eval(variaveis=environment[-1], askNode=node).executeAst(operationAst=node.pergunta, variaveis=environment[-1])
                lastConditionalResult[node.depth] = sucessoCondicional
                if sucessoCondicional != 1:
                    i = nodesIndex[node.fim]

            case Setter():
                environment[-1][node.setwho].valor = Eval(variaveis=environment[-1], askNode=node).executeAst(operationAst=node.setto, variaveis=environment[-1])

            case Show():
                
                node.show(environment[-1])
        
            case Get():
                environment[-1][node.setwho].valor = node.get()

            case ConditionalIf():
                sucessoCondicional = Eval(variaveis=environment[-1], askNode=node).executeAst(operationAst=node.pergunta, variaveis=environment[-1])
                lastConditionalResult[node.depth] = sucessoCondicional
                if sucessoCondicional == 1:
                    i = nodesIndex[node.corpo]-1
                else:
                    i = nodesIndex[node.fim]

            case ConditionalElse():
                if lastConditionalResult[node.depth] != 1:
                    sucessoCondicional = Eval(variaveis=environment[-1], askNode=node).executeAst(operationAst=node.pergunta, variaveis=environment[-1])
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

            case Exit():
                return

            case EndLoop():
                i = nodesIndex[node.loopPai]-1

        i += 1
    return