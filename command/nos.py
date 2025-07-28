class Variavel:
    def __init__(self, nome, valor):
        self.nome = nome
        self.valor = valor

class Setter:
    def __init__(self, setwho, setto):
        self.setwho = setwho
        self.setto = setto

class Show:
    def __init__(self, content):
        self.content = content

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
            pass
        print()     