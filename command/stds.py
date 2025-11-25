from nos import Erro
import random

#Nome da funcao : [qtd de argumentos, nome funcao]
funcArgs = { 
    "length" : [1, "cmdLength"],
    "sort" : [1, "cmdSort"],
    "showList" : [1, "cmdShowList"],
    "showMap" : [1, "cmdShowMap"],
    "sum": [1, "cmdSum"],
    "type": [1, "cmdType"],
    "stripMarc": [1, "cmdStripMarc"],

    "indexOf": [2, "cmdIndexOf"],
    "random": [2, "cmdRandom"],
    "add": [2, "cmdAdd"],
    "delete": [2, "cmdDelete"],

    "set": [3, "cmdSet"],
    "insert": [3, "cmdInsert"],
}

def stdFuncs() -> dict:
    return funcArgs

def stdHandler(node, args) -> any:
    if funcArgs[node.execWho][0] != len(node.argumentos):
        return Erro(linha=node.linha, tipo="Quantia de argumentos indevida.")
    return globals()[funcArgs[node.execWho][1]](args)

#builtins:
def cmdSet(obj: any) -> list | str | dict:
    """Usado para alterar o valor de argumento 1 dentro de argumento 0 para argumento 2. Retorna -1 em caso de erro."""
    if isinstance(obj[2], (list, dict)):
        return -1 
    if isinstance(obj[0], dict): #Mapas
        new = obj[0].copy()
        new[obj[1]] = obj[2]
        return(new)
    elif isinstance(obj[0], (list, str)):
        if not isinstance(obj[1], int):
            return -1
        if (obj[1] >= len(obj[0]) or (obj[1] < 0 and abs(obj[1]) > len(obj[0]))):
            return -1
        elif isinstance(obj[0], list): #Listas
            new = obj[0].copy()
            new[obj[1]] = obj[2]
            return(new)
        else: #Textos
            obj[0] = list(obj[0])
            obj[0][obj[1]] = obj[2]
            obj[0] = ''.join([str(x) for x in obj[0]])
            return(obj[0])
    else:
        return -1
    
def cmdInsert(obj: any) -> list | str | dict:
    """Insere argumento 2 no indice argumento 1 dentro de argumento 0. Retorna -1 em caso de erro."""
    if isinstance(obj[2], (list, dict)):
        return -1
    if isinstance(obj[0], dict): #Mapas
        new = obj[0].copy()
        new[obj[1]] = obj[2]
        return(new)
    elif isinstance(obj[0], (list, str)):
        if not isinstance(obj[1], int):
            return -1
        if (obj[1] >= len(obj[0]) or (obj[1] < 0 and abs(obj[1]) > len(obj[0]))):
            return -1
        elif isinstance(obj[0], list): #Listas
            new = obj[0].copy()
            new.insert(obj[1], obj[2])
            return(new)
        else: #Textos
            new = list(obj[0])
            new.insert(obj[1], obj[2])
            obj[0] = ''.join([str(x) for x in new])
            return(obj[0])
    else:
        return -1

def cmdDelete(obj: any) -> list | str | dict:
    """Deleta argumento 1 de argumento 0. Retorna -1 em caso de erro."""
    if isinstance(obj[0], dict): #Mapas
        if obj[1] in obj[0]:
            new = obj[0].copy()
            del new[obj[1]]
            return new
        else:
            return -1
    elif isinstance(obj[0], (list, str)):
        if not isinstance(obj[1], int):
            return -1
        if (obj[1] >= len(obj[0]) or (obj[1] < 0 and abs(obj[1]) > len(obj[0]))):
            return -1
        elif isinstance(obj[0], list): #Listas
            new = obj[0].copy()
            del new[obj[1]]
            return(new)
        else: #Textos
            new = list(obj[0])
            del new[obj[1]]
            obj[0] = ''.join([str(x) for x in new])
            return(obj[0])
    else:
        return -1

def cmdAdd(obj: any) -> list | str:
    """adiciona ao fim de uma lista / str (argumento 0) argumento 1. Retrona -1 em caso de erro."""
    if isinstance(obj[1], (list, dict)):
        return -1
    if isinstance(obj[0], list):
        new = obj[0].copy()
        new.append(obj[1])
        return(new)
    elif isinstance(obj[0], str):
        return(obj[0] + str(obj[1]))
    else:
        return -1

def cmdShowList(obj: any) -> int:
    """Mostra uma lista, retorna -1 em caso de erro."""
    if isinstance(obj[0], list):
        for i in range(len(obj[0])):
            val = obj[0][i]
            if isinstance(val, dict):
                obj[0][i] = "{map}"
            elif isinstance(val, list):
                obj[0][i]= "[list]"

        print("[" + ', '.join([str(x) for x in obj[0]]) + "]")
        return 1
    else:
        return(-1)

def cmdShowMap(obj: any) -> int:
    """Mostra um mapa, retorna -1 em caso de erro."""
    if isinstance(obj[0], dict):
        content = ""
        for key in obj[0]:
            val = obj[0][key]
            if isinstance(val, dict):
                val = "{map}"
            elif isinstance(val, list):
                val = "[list]"

            content += f"{key} -> {val}, "
        print("{",content[:-2],"}", sep="")
        return 1
    else:
        return(-1)

def cmdRandom(obj: any) -> int:
    """Gera um número aleatório dentro do intervalo determinado. retorna -1 em caso de erro."""
    if isinstance(obj[0], int) and isinstance(obj[1], int):
        if obj[0] < obj[1]:
            return(random.randint(obj[0], obj[1]))
        return(-1)
    return(-1)

def cmdLength(obj: any) -> int:
    """Mostra o comprimento de um objeto (texto, lista ou mapa), retorna -1 em caso de erro."""
    if isinstance(obj[0], (str,list,dict)):
        return(len(obj[0]))
    else:
        return(-1)
    
def cmdSort(obj: any) -> list | str | int:
    """Organiza um objeto (seja lista ou texto), retorna -1 em caso de erro."""
    if isinstance(obj[0], list):
        return(sorted(obj[0]))
    elif isinstance(obj[0], str):
        return(''.join(sorted(obj[0])))
    else:
        return(-1)

def cmdSum(obj: any) -> int:
    """Retorna a soma dos itens de uma lista, retorna -1 em caso de erro."""
    if isinstance(obj[0], list):
        try:
            return(sum(obj[0]))
        except:
            return(-1)
    else:
        return(-1)
    
def cmdType(obj: any) -> str:
    """Retorna o tipo do objeto"""
    tipos = {int:"num",float:"num",str:"str",list:"list",dict:"map"}
    if obj[0] == None:
        return("nil")
    return(tipos[type(obj[0])])

def cmdIndexOf(obj: any) -> int:
    """Mostra onde argumento 0 está em argumento 1, retorna -1 em caso de erro."""
    if not(isinstance(obj[1], (list,str))):
        return(-1)
    try:
        return(obj[1].index(obj[0]))
    except:
        return(-1)
    
def cmdStripMarc(obj: any) -> str | int:
    """Remove aspas simples das pontas de um texto, retorna -1 em caso de erro."""
    if isinstance(obj[0], str):
        if len(obj[0]) > 1 and obj[0][0] == obj[0][-1] == "'":
            copy = obj[0][:]
            return(copy[1:-1])
        return(-1)
    return(-1)