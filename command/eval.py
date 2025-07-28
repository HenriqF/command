class Eval:
    def __init__(self,variaveis):
        self.variaveis = variaveis

    def getValor(self,token):
        valor = self.variaveis[token].valor
        while isinstance(valor, str) and valor in self.variaveis:
            valor = self.variaveis[valor].valor
        return valor  #adicionar self.evaluate(valor) para recursao, (tal caso, adicionar err hand para ref ciclica a=b b=a...)

    def evaluate(self, tokens):
        def revPolNot(tokens):
            ordem = {"+":1,"-":1,"*":2,"/":2}
            result = []
            stackOrdem = []
            for i in range(len(tokens)):
                token = tokens[i]

                #print(self.variaveis, token)
                if token in self.variaveis:
                    result.append(self.getValor(token))

                elif not isinstance(token, str):
                    result.append(token)
                elif token in ordem:
                    while stackOrdem and stackOrdem[-1] in ordem and ordem[stackOrdem[-1]] >= ordem[token]:
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
            #print(tokens)
            for token in tokens:
                if str(token) in "+-*/":
                    if len(stack) < 2:
                        raise Exception("Operação matemática malformada.")

                    b = stack.pop()
                    a = stack.pop()

                    if type(a) != type(b):
                        raise Exception(f"Operação com dois tipos diferentes: {type(a).__name__} {token} {type(b).__name__}")

                    if token == "+":
                        stack.append(a + b)
                    elif token == "-":
                        stack.append(a - b)
                    elif token == "*":
                        stack.append(a*b)
                    else:
                        stack.append(a/b)
                else:
                    stack.append(token)
            if len(stack) > 1:
                raise Exception("Operação matemática malformada.")
            if not stack:
                raise Exception("Operação não presente.")
            return stack[0]
        
        return(getResult(tokens))