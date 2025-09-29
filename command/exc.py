import sys
from nos import *
from eval import *
from stds import stdFuncs, stdHandler
import time as Time

def execute(nodes, variaveis, funcoes, nodesIndex):    
    environment = [variaveis]
    lastConditionalResult = {}
    errorImmunity = []

    def execErro(erro):
        if not errorImmunity:
            erro.execErr()
        else:
            i = nodesIndex[errorImmunity[-1].fim]
            if errorImmunity[-1].resultVar is not None:
                environment[-1][errorImmunity[-1].resultVar].valor = 1
            errorImmunity.pop()
            return i

    i = 0
    while i < len(nodes):
        node = nodes[i]
        
        if not isinstance(node, (Conditional, Loop, Dummy)):
            lastConditionalResult[node.depth] = 1
        match node:
            
            case Check():
                errorImmunity.append(node)
                if node.resultVar is not None:
                    environment[-1][node.resultVar].valor = 0

            case EndCheck():
                if errorImmunity:
                    errorImmunity.pop()

            case Result():
                if node.funcaoPai is None:
                    i = execErro(Erro(linha=node.linha, tipo="Result sem função."))
                else:
                    if node.retorno is not None:
                        node.valor = Eval(variaveis=environment[-1], askNode=node).executeAst(operationAst=node.retorno, variaveis=environment[-1])
                    if isinstance(node.valor, Erro):
                        i = execErro(node.valor)
                    else:
                        if node.valor is not None:
                            funcoes[node.funcaoPai].caller[-1].valor = node.valor
                        environment.pop()
                        i = nodesIndex[funcoes[node.funcaoPai].caller[-1]]
                        funcoes[node.funcaoPai].caller.pop()

            case Function():
                i = nodesIndex[node.fim]

            case Execute():
                nodeArgumentosExist = node.argumentos is None
                foundErrorInArgs = False

                if not nodeArgumentosExist:
                    args = []
                    for arg in node.argumentos:
                        if isinstance(arg, Operacao):
                            args.append(Eval(variaveis=environment[-1], askNode=node).executeAst(operationAst=arg, variaveis=environment[-1]))
                            if isinstance(args[-1], Erro):
                                i = execErro(args[-1])
                                foundErrorInArgs = True
                        else:
                            args.append(arg)
                            if isinstance(args[-1], Erro):
                                i = execErro(args[-1])
                                foundErrorInArgs = True

                if not foundErrorInArgs:
                    if node.execWho not in funcoes:
                        if node.execWho in stdFuncs():
                            result = stdHandler(node, environment[-1])
                            if isinstance(result, Erro):
                                i = execErro(result)
                            else:
                                node.valor = result
                        else:
                            i = execErro(Erro(linha=node.linha, tipo="Funcao inexistente."))
                    elif (funcoes[node.execWho].argumentos is None) != (nodeArgumentosExist):
                        i = execErro(Erro(linha=node.linha, tipo="Quantia de argumentos indevida."))
                    elif (not nodeArgumentosExist) and (type(funcoes[node.execWho].argumentos) != type(args)):
                        i = execErro(Erro(linha=node.linha, tipo="Quantia de argumentos indevida."))
                    elif (not nodeArgumentosExist) and (len(funcoes[node.execWho].argumentos) != len(args)):
                        i = execErro(Erro(linha=node.linha, tipo="Quantia de argumentos indevida."))
                    else:
                        newEnv = {}
                        for env in funcoes[node.execWho].environment:
                            newEnv[env] = funcoes[node.execWho].environment[env].copy()
                        if args is not None:
                            for i, var in enumerate(funcoes[node.execWho].argumentos):
                                if args[i] in environment[-1]:
                                    newEnv[var].valor = environment[-1][args[i]].valor
                                else:
                                    newEnv[var].valor = args[i]
                        environment.append(newEnv)
                        funcoes[node.execWho].caller.append(node)
                        i = nodesIndex[funcoes[node.execWho].corpo]-1

            case Apply():
                prevIndex = nodesIndex[node]-1
                if node.variavel not in environment[-1]:
                    i = execErro(Erro(linha=node.linha, tipo="Apply em variavel não declarada."))
                elif not isinstance(nodes[prevIndex], Execute):
                    i = execErro(Erro(linha=node.linha, tipo="Comando antes de apply não é execute."))
                else:
                    if nodes[prevIndex].valor is not None:
                        environment[-1][node.variavel].valor = nodes[prevIndex].valor

            case WhileLoop():
                sucessoCondicional = Eval(variaveis=environment[-1], askNode=node).executeAst(operationAst=node.pergunta, variaveis=environment[-1])
                if isinstance(sucessoCondicional, Erro):
                    i = execErro(sucessoCondicional)
                else:
                    lastConditionalResult[node.depth] = sucessoCondicional
                    if sucessoCondicional != 1:
                        i = nodesIndex[node.fim]
            
            case BreakLoop():
                if node.loopPai == None:
                    i = execErro(Erro(linha=node.linha, tipo="Comando break fora de loop."))
                else:
                    i = nodesIndex[node.loopPai.fim]
                    
            case EndLoop():
                i = nodesIndex[node.loopPai]-1

            case Setter():
                foundErrorInData = False
                processed = node.setto
                if isinstance(node.setto, list):
                    processed = []
                    for j in range(len(node.setto)):
                        processed.append(Eval(variaveis=environment[-1], askNode=node).executeAst(operationAst=node.setto[j], variaveis=environment[-1]))
                        if isinstance(processed[-1], Erro):
                            i = execErro(processed[-1])
                            foundErrorInData = True

                elif isinstance(node.setto, dict):
                    processed = {}
                    for key in node.setto:
                        processedValue = Eval(variaveis=environment[-1], askNode=node).executeAst(operationAst=node.setto[key], variaveis=environment[-1])
                        if isinstance(processedValue, Erro):
                            i = execErro(processedValue)
                            foundErrorInData = True
                        processed[key] = processedValue
                        
                if not foundErrorInData:
                    valor = Eval(variaveis=environment[-1], askNode=node).executeAst(operationAst=processed, variaveis=environment[-1])
                    if isinstance(valor, Erro):
                        i = execErro(valor)
                    else:
                        environment[-1][node.setwho].valor = valor

            case Show():
                result = node.show(environment[-1])
                if isinstance(result, Erro):
                    i = execErro(result)
        
            case Get():
                environment[-1][node.setwho].valor = node.get()

            case ConditionalIf():
                sucessoCondicional = Eval(variaveis=environment[-1], askNode=node).executeAst(operationAst=node.pergunta, variaveis=environment[-1])
                if isinstance(sucessoCondicional, Erro):
                    i = execErro(sucessoCondicional)
                else:
                    lastConditionalResult[node.depth] = sucessoCondicional
                    if sucessoCondicional == 1:
                        i = nodesIndex[node.corpo]-1
                    else:
                        i = nodesIndex[node.fim]

            case ConditionalElse():
                if node.depth in lastConditionalResult:
                    if lastConditionalResult[node.depth] != 1:
                        sucessoCondicional = Eval(variaveis=environment[-1], askNode=node).executeAst(operationAst=node.pergunta, variaveis=environment[-1])
                        if isinstance(sucessoCondicional, Erro):
                            i = execErro(sucessoCondicional)
                        else:
                            lastConditionalResult[node.depth] = sucessoCondicional
                            if sucessoCondicional == 1:
                                i = nodesIndex[node.corpo]-1
                            else:
                                i = nodesIndex[node.fim]
                    else:
                        i = nodesIndex[node.fim]
                else:
                    i = nodesIndex[node.fim]

            case Else():
                if node.depth in lastConditionalResult:
                    if lastConditionalResult[node.depth] != 1:
                        lastConditionalResult[node.depth] = 1
                        i = nodesIndex[node.corpo]-1
                    else:
                        i = nodesIndex[node.fim]
                else:
                    i = nodesIndex[node.fim]
            
            case Exit():
                return

        i += 1
    return