class Variavel:
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor
    
    def info(self):
        print("info variavel #####")
        print(self.nome)
        print(self.valor)
        print("###################")

#Comandos

class Setter:
    def __init__(self, setwho, setto, depth):
        self.setwho = setwho
        self.setto = setto
        self.depth = depth
    def info(self):
        print("info setter #######")
        print(self.setwho)
        print(self.setto)
        print(self.depth)
        print("###################")

class Show:
    def __init__(self, content, depth):
        self.content = content
        self.depth = depth

    def info(self):
        print("info show #########")
        print(self.content)
        print(self.depth)
        print("###################")

    def show(self, variaveis):
        content = self.content
        l = len(content)
        i = 0 
        while i < l:
            if content[i] == '`':
                i+=1
                while content[i] != '`':
                    print(content[i], end="")
                    i += 1
                i+=1
            if i < l:
                if content[i] in variaveis:
                    print(variaveis[content[i]].valor, end="")
                else:
                    print(content[i], end="")
                i+=1
        print()     

class Conditional:
    def __init__(self, pergunta, corpo, fim, depth):
        self.pergunta = pergunta
        self.corpo = corpo
        self.fim = fim
        self.depth = depth

    def info(self):
        print("info conditional###")
        print(self.pergunta)
        print(self.corpo)
        print(self.fim)
        print(self.depth)
        print("###################")

class ConditionalElse:
    def __init__(self, pergunta, corpo, fim, depth):
        self.pergunta = pergunta
        self.corpo = corpo
        self.fim = fim
        self.depth = depth

    def info(self):
        print("info condElse#########")
        print(self.pergunta)
        print(self.corpo)
        print(self.fim)
        print(self.depth)
        print("######################")

class Else:
    def __init__(self, corpo, fim, depth):
        self.corpo = corpo
        self.fim = fim
        self.depth = depth

    def info(self):
        print("info else##########")
        print(self.corpo)
        print(self.fim)
        print(self.depth)
        print("###################")
