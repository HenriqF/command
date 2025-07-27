import sys
class Command:
    def interpret(self, code):
        self.variaveis = {}
        linhas = [x for x in code.split("\n") if x.strip() != ""]

        for linha in linhas:
            tokens = self.getTokens(linha)
            match tokens[0]:
                case "edit":
                    if tokens[2] == "=":
                        self.variaveis[tokens[1]] = self.evaluate(tokens[3:])
                case "list":
                    print(self.variaveis)
                case _:
                    raise Exception(f"""Comando desconhecido --> "{tokens[0]}", linha {linhas.index(linha)+1}""")
    
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
                if char != " ":
                    tokens.append(char)
            i += 1
        if current != "" and current != " ":
            tokens.append(format(current))
        return(tokens)

    def evaluate(self, tokens):
        def revPolNot(tokens):
            ordem = {"+":1,"-":1,"*":2,"/":2}
            result = []
            stackOrdem = []
            for i in range(len(tokens)):
                token = tokens[i]
                if token in self.variaveis:
                    result.append(self.variaveis[token])
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
            for token in tokens:
                if str(token) in "+-*/":
                    b = stack.pop()
                    a = stack.pop()
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
            return stack[0]
        
        return(getResult(tokens))

command = Command().interpret(open("test.command").read())

#Eval().evaluate(open((sys.argv[1])+".command" if ".command" not in (sys.argv[1]) else (sys.argv[1])).read())
