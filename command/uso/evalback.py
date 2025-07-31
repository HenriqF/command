from nos import Erro

class Eval:
    def __init__(self,variaveis, askNode):
        self.variaveis = variaveis
        self.askNode = askNode
        self.ordem = {"~":0, #aproximacao ( 1~10.07 arredonde 10.07 para a primeira casa : 10.1)
                      "|":1, #ou
                      "&":2, #ands
                      ">":3, "<":3, "$":3, #comparacao ($ comparador de strings)
                      "+":4,"-":4,
                      "*":5,"/":5,"%":5,
                      "^":6,
                      }
        self.unario = {"!","-"}

    def getValor(self,token):
        valor = self.variaveis[token].valor
        while isinstance(valor, str) and valor in self.variaveis:
            valor = self.variaveis[valor].valor
        return valor  #adicionar self.evaluate(valor) para recursao, (tal caso, adicionar err hand para ref ciclica a=b b=a...)

    def evaluate(self, tokens):
        def revPolNot(tokens): #tambem calcula operadores unarios
            if len(tokens) == 0 and (tokens[0] in self.ordem or tokens[0] in self.unario):
                Erro(linha=self.askNode.linha, tipo="Operação matemática malformada.")

            result = []
            stackOrdem = []
            i = 0
            while i < len(tokens):
                if tokens[i] in self.variaveis:
                    tokens[i] = self.variaveis[tokens[i]].valor
                i += 1
            i = 0
            while i < len(tokens):
                token = tokens[i]
                prevToken = None
                futureToken = None
                if i-1 >= 0:
                    prevToken = tokens[i-1]
                if i+1 < len(tokens):
                    futureToken = tokens[i+1]

                if (token in self.unario) and (prevToken is None or prevToken in self.ordem or prevToken in {"(",")"}) and (futureToken not in self.ordem) and (futureToken not in self.unario and futureToken):
                    if futureToken in self.variaveis:
                        valor = self.variaveis[futureToken].valor
                        if isinstance(valor, int):
                            valor = float(valor)
                        futureToken = valor
                    match token:
                        case "-":
                            if isinstance(futureToken, (int, float)):
                                tokens[i] = futureToken * -1
                                tokens.pop(i+1)
                                i-=2
                            else:
                                Erro(linha=self.askNode.linha, tipo="Operação matemática malformada")
                        case "!":
                            if isinstance(futureToken, (int, float)):
                                if futureToken == 1:
                                    tokens[i] = 0
                                elif futureToken == 0:
                                    tokens[i] = 1
                                else:
                                    tokens[i] = ~futureToken
                                tokens.pop(i+1)
                                i-=2
                            else:
                                Erro(linha=self.askNode.linha, tipo="Operação matemática malformada")


                i += 1
                
            for i in range(len(tokens)):
                token = tokens[i]
                #print(self.variaveis, token)
                if not isinstance(token, str):
                    if isinstance(token, int):
                        token = float(token)
                    result.append(token)
                elif token in self.ordem:
                    while stackOrdem and stackOrdem[-1] in self.ordem and self.ordem[stackOrdem[-1]] >= self.ordem[token]:
                        result.append(stackOrdem.pop())
                    stackOrdem.append(token)
                elif token == "(":
                    stackOrdem.append(token)
                elif token == ")":
                    while stackOrdem[-1] != "(":
                        result.append(stackOrdem.pop())
                    stackOrdem.pop()
                else:
                    result.append(token)
            while stackOrdem:
                result.append(stackOrdem.pop())
            return result
        
        def getResult(tokens):
            tokens = revPolNot(tokens)

            stack = []
            for token in tokens:
                if token in self.ordem:
                    if len(stack) < 2:
                        Erro(linha=self.askNode.linha, tipo="Operação matemática malformada.")
                    b = stack.pop()
                    a = stack.pop()

                    if type(a) != type(b):
                        Erro(linha=self.askNode.linha, tipo="Operação com dois tipos diferentes.")

                    match token:
                        #Logica binaria
                        case "&":
                            if isinstance(a, (int, float)):
                                a = int(a)
                                b = int(b)
                            else:
                                Erro(linha=self.askNode.linha, tipo="Logica binária com valor não numérico")

                            stack.append(float(a&b))
                        case "|":
                            if isinstance(a, (int, float)):
                                a = int(a)
                                b = int(b)
                            else:
                                Erro(linha=self.askNode.linha, tipo="Logica binária com valor não numérico")

                            stack.append(float(a|b))

                        #Comparacao
                        case ">":
                            if isinstance(a, (float,int)):
                                stack.append(1.0 if a >= b else 0.0)
                            if isinstance(a, str):
                                stack.append(1.0 if len(a) >= len(b) else 0.0)
                        case "<":
                            if isinstance(a, (float,int)):
                                stack.append(1.0 if a <= b else 0.0)
                            if isinstance(a, str):
                                stack.append(1.0 if len(a) <= len(b) else 0.0)
                            pass
                        case "$":
                            if isinstance(a, str):
                                stack.append(1.0 if a == b else 0.0)
                        #Operacao

                        case "~":
                            if isinstance(a, (float,int)):
                                a = int(a)
                                stack.append(round(b, a))
                        case "^":
                            stack.append(a**b)
                        case "+":
                            stack.append(a+b)
                        case "-":
                            stack.append(a-b)
                        case "*":
                            stack.append(a*b)
                        case "/":
                            stack.append(a/b)
                        case "%":
                            stack.append(a%b)
                    
                else:
                    stack.append(token)

            if len(stack) > 1:
                Erro(linha=self.askNode.linha, tipo="Operação matemática malformada.")
            if not stack:
                Erro(linha=self.askNode.linha, tipo="Operação não presente.")
            return stack[0]
        
        result = getResult(tokens)
        if type(result) != str and int(result) == result:
            result = int(result)
        return(result)