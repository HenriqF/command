from nos import Erro

class Operacao:
    def __init__(self, operador, es, di, askNode):
        self.operador = operador
        self.es = es
        self.di = di
        self.askNode = askNode

    def operate(self):
        esquerda = self.es
        direita = self.di
        if isinstance(self.es, Operacao):
            esquerda = self.es.operate()
        if isinstance(self.di, Operacao):
            direita = self.di.operate()

        if esquerda is not None:
            if isinstance(esquerda, (int, float)) != isinstance(direita, (int, float)):
                if not(isinstance(esquerda,(str)) and isinstance(direita, (int,float)) and self.operador == "*"):
                    Erro(linha=self.askNode.linha, tipo="Operação proibida com tipos diferentes.")

        if isinstance(esquerda, (str)) and ((self.operador not in {"+","*","=",">","<"}) or (isinstance(direita, (str)) and self.operador == "*")):
            Erro(linha=self.askNode.linha, tipo="Operador mal-usado.")

        match self.operador:
            #Operadores unários
            case "u-":
                return(direita * -1)
            case "!":
                if direita == 1:
                    return(0.0)
                if direita == 0:
                    return(1.0)
                if isinstance(direita, (str, float)):
                    Erro(linha=self.askNode.linha, tipo="Negação de não-inteiro")
                return(~ direita)
            
            #Logica binária
            case "&":
                esquerda = int(esquerda)
                direita = int(direita)
                return(float(esquerda&direita))
            case "|":
                esquerda = int(esquerda)
                direita = int(direita)
                return(float(esquerda|direita))

            #Operadores binários
            case "~":
                if isinstance(esquerda, (float,int)):
                    esquerda = int(esquerda)
                    return(round(direita, esquerda))
            case "^":
                return(esquerda**direita)
            case "+":
                return(esquerda + direita)
            case "-":
                return(esquerda - direita)
            case "*":
                return(esquerda * direita)
            case "/":
                if direita == 0:
                    Erro(linha=self.askNode.linha, tipo="Divisão por zero.")
                return(esquerda / direita)
            case "%":
                if direita == 0:
                    Erro(linha=self.askNode.linha, tipo="Modulo com zero.")
                return(esquerda%direita)

            #Comparadores
            case ">":
                if isinstance(esquerda, (float,int)):
                    return(1.0 if esquerda > direita else 0.0)
                if isinstance(esquerda, str):
                    return(1.0 if len(esquerda) > len(direita) else 0.0)
            case "<":
                if isinstance(esquerda, (float,int)):
                    return(1.0 if esquerda < direita else 0.0)
                if isinstance(esquerda, str):
                    return(1.0 if len(esquerda) < len(direita) else 0.0)
            case "=":
                if direita == esquerda:
                    return(1.0)
                else:
                    return(0.0)

class Eval:
    def __init__(self,variaveis, askNode):
        self.variaveis = variaveis
        self.askNode = askNode

        self.ordem = {"~":0, #aproximacao ( 1~10.07 arredonde 10.07 para a primeira casa : 10.1)
                      "|":1, #ou
                      "&":2, #ands
                      ">":3, "<":3, "=":3,
                      "+":4,"-":4,
                      "*":5,"/":5,"%":5,
                      "^":6,
                      "!":7,"u-":7
                      }
        self.binario = {"~","|","&",">","<","=","+","-","*","/","%","^"}
        self.unario = {"!","u-"}

    def getValor(self,token):
        valor = self.variaveis[token].valor
        while isinstance(valor, str) and valor in self.variaveis:
            valor = self.variaveis[valor].valor
        return valor 

    def evaluate(self, operation):
        tokens = operation[:]
        def transform(tokens):
            i = 0
            while i < len(tokens):
                token = tokens[i]
                lastchar = None
                if i-1 >= 0:
                    lastchar = tokens[i-1]

                if tokens[i] in self.variaveis:
                    tokens[i] = self.getValor(tokens[i])
                elif token == "-" and ((lastchar in self.ordem or lastchar in {"(",")"}) or (lastchar == None)):
                    tokens[i] = "u-"
                i+=1
            return(tokens)

        def revPolNot(tokens):
            final = []
            stacksinal = []
            for token in tokens: #poe em ordem reversa polonesa
                if isinstance(token, (float, int)):
                    final.append(token)
                elif token in self.ordem:
                    while stacksinal and (stacksinal[-1] not in "()") and (self.ordem[stacksinal[-1]] >= self.ordem[token]):
                        final.append(stacksinal.pop())
                    stacksinal.append(token)
                elif token == "(":
                    stacksinal.append("(")
                elif token == ")":
                    while stacksinal and stacksinal[-1] != "(":
                        final.append(stacksinal.pop())
                    if stacksinal:
                        stacksinal.pop()
                    else:
                        Erro(linha=self.askNode.linha, tipo="Parenteses não-balanceados.")
                else:
                    final.append(token)
            while stacksinal:
                final.append(stacksinal.pop())
            return(final)

        def createOPAST(tokens):
            tokens = revPolNot(transform(tokens))

            resultado = [] #AST root
            for token in tokens: #Cria a AST
                if token in self.binario:
                    if len(resultado) < 2:
                        Erro(linha=self.askNode.linha, tipo="Operação malformada")
                    b = resultado.pop()
                    a = resultado.pop()
                    resultado.append(Operacao(operador=token, es=a, di=b, askNode=self.askNode))
                elif token in self.unario:
                    if len(resultado) < 1:
                        Erro(linha=self.askNode.linha, tipo="Operação malformada")
                    b = resultado.pop()
                    resultado.append(Operacao(operador=token, es=None, di=b, askNode=self.askNode))
                else:
                    resultado.append(token)

            return(resultado[0])

        opAST = createOPAST(tokens)
        result = opAST
        if isinstance(opAST, Operacao):
            result = opAST.operate()
        
        if isinstance(result, float) and int(result) == float(result):
            return(int(result))
        return(result)