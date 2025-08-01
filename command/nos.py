class Variavel:
    def __init__(self, nome, valor, linha):
        self.nome = nome
        self.valor = valor
        self.linha = linha
class Erro:
    def __init__(self, linha, tipo):
        self.linha = linha
        self.tipo = tipo
        self.expliciteErro()

    def expliciteErro(self):
        print(f"""\033[31mErro\033[0m : {self.tipo} --> "\033[1m{self.linha[0]}\033[0m", \033[31mlinha {self.linha[1]}\033[0m""")
        exit(1)

#SuperClasses
class Dummy:
    pass
class TemCorpo:
    pass
class Loop(TemCorpo):
    pass
class Conditional(TemCorpo):
    pass

#Comandos
class Setter:
    def __init__(self, setwho, setto, depth, linha):
        self.setwho = setwho
        self.setto = setto
        self.depth = depth
        self.linha = linha
class Show:
    def __init__(self, content, depth, linha):
        self.content = content
        self.depth = depth
        self.linha = linha

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
class Get:
    def __init__(self, content, setwho, depth, linha):
        self.content = content
        self.setwho = setwho
        self.depth = depth
        self.linha = linha

    def get(self):

        if self.content is not None:
            got = (input(''.join(self.content)))
        else:
            got = (input())
        try:
            got = float(got)
            if int(got) == got:
                got = int(got)
        except:
            pass
        return(got)
class Exit:
    def __init__(self, depth, linha):
        self.depth = depth
        self.linha = linha
class Nothing:
    def __init__(self, depth, linha):
        self.depth = depth
        self.linha = linha

#Loops
class WhileLoop(Loop):
    def __init__(self, pergunta, corpo, fim, depth, linha):
        self.pergunta = pergunta
        self.corpo = corpo
        self.fim = fim
        self.depth = depth
        self.linha = linha
class EndLoop(Dummy):
    def __init__(self, loopPai, depth):
        self.loopPai = loopPai
        self.depth = depth
        
#Condicionais
class ConditionalIf(Conditional):
    def __init__(self, pergunta, corpo, fim, depth, linha):
        self.pergunta = pergunta
        self.corpo = corpo
        self.fim = fim
        self.depth = depth
        self.linha = linha
class ConditionalElse(Conditional):
    def __init__(self, pergunta, corpo, fim, depth, linha):
        self.pergunta = pergunta
        self.corpo = corpo
        self.fim = fim
        self.depth = depth
        self.linha = linha
class Else(Conditional):
    def __init__(self, corpo, fim, depth, linha):
        self.corpo = corpo
        self.fim = fim
        self.depth = depth
        self.linha = linha
