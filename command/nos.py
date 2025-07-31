class Variavel:
    def __init__(self, nome, valor, linha):
        self.nome = nome
        self.valor = valor
        self.linha = linha
    
    def info(self):
        print("info variavel #####")
        print(self.nome)
        print(self.valor)
        print("###################")

class Erro:
    def __init__(self, linha, tipo):
        self.linha = linha
        self.tipo = tipo
        self.expliciteErro()

    def expliciteErro(self):
        print(f"""\033[31mErro\033[0m : {self.tipo} --> "\033[1m{self.linha[0]}\033[0m", \033[31mlinha {self.linha[1]}\033[0m""")
        exit(1)
#Comandos


class Setter:
    def __init__(self, setwho, setto, depth, linha):
        self.setwho = setwho
        self.setto = setto
        self.depth = depth
        self.linha = linha
    def info(self):
        print("info setter #######")
        print(self.setwho)
        print(self.setto)
        print(self.depth)
        print("###################")

class Show:
    def __init__(self, content, depth, linha):
        self.content = content
        self.depth = depth
        self.linha = linha

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





class TemCorpo:
    pass

class Conditional(TemCorpo):
    pass

class ConditionalIf(Conditional):
    def __init__(self, pergunta, corpo, fim, depth, linha):
        self.pergunta = pergunta
        self.corpo = corpo
        self.fim = fim
        self.depth = depth
        self.linha = linha

    def info(self):
        print("info conditional###")
        print(self.pergunta)
        print(self.corpo)
        print(self.fim)
        print(self.depth)
        print("###################")

class ConditionalElse(Conditional):
    def __init__(self, pergunta, corpo, fim, depth, linha):
        self.pergunta = pergunta
        self.corpo = corpo
        self.fim = fim
        self.depth = depth
        self.linha = linha

    def info(self):
        print("info condElse#########")
        print(self.pergunta)
        print(self.corpo)
        print(self.fim)
        print(self.depth)
        print("######################")

class Else(Conditional):
    def __init__(self, corpo, fim, depth, linha):
        self.corpo = corpo
        self.fim = fim
        self.depth = depth
        self.linha = linha

    def info(self):
        print("info else##########")
        print(self.corpo)
        print(self.fim)
        print(self.depth)
        print("###################")
