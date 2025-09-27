from nos import Erro
import random

funcArgs = {
    "objLength" : 1,
    "objSort" : 1,
    "showList" : 1,
    "showMapa" : 1,
    "sumList": 1,
    "objType": 1,
    "stripAspas": 1,

    "indexOf": 2,
    "randomNum": 2,
}

def stdFuncs() -> dict:
    return funcArgs

def stdHandler(node, vars) -> any:
    if funcArgs[node.execWho] != len(node.argumentos):
        return Erro(linha=node.linha, tipo="Quantia de argumentos indevida.")
    args = []
    for arg in node.argumentos:
        if arg in vars:
            args.append(vars[arg].valor)
        else:
            args.append(arg)
    result = globals()[node.execWho](args)
    return result

#builtins:

def showList(obj: any) -> int:
    """Mostra uma lista, retorna -1 em caso de erro."""
    if isinstance(obj[0], list):
        print("[" + ' ,'.join([str(x) for x in obj[0]]) + "]")
        return 1
    else:
        return(-1)

def showMapa(obj: any) -> int:
    """Mostra um mapa, retorna -1 em caso de erro."""
    if isinstance(obj[0], dict):
        content = ""
        for key in obj[0]:
            content += f"{key} -> {obj[0][key]}, "
        print("{",content[:-2],"}", sep="")
        return 1
    else:
        return(-1)

def randomNum(obj: any) -> int:
    """Gera um número aleatório dentro do intervalo determinado. retorna -1 em caso de erro."""
    if isinstance(obj[0], int) and isinstance(obj[1], int):
        if obj[0] < obj[1]:
            return(random.randint(obj[0], obj[1]))
        return(-1)
    return(-1)

def objLength(obj: any) -> int:
    """Mostra o comprimento de um objeto (texto, lista ou mapa), retorna -1 em caso de erro."""
    if isinstance(obj[0], (str,list,dict)):
        return(len(obj[0]))
    else:
        return(-1)
    
def objSort(obj: any) -> list | str | int:
    """Organiza um objeto (seja lista ou texto), retorna -1 em caso de erro."""
    if isinstance(obj[0], list):
        return(sorted(obj[0]))
    elif isinstance(obj[0], str):
        return(''.join(sorted(obj[0])))
    else:
        return(-1)

def sumList(obj: any) -> int:
    """Retorna a soma dos itens de uma lista, retorna -1 em caso de erro."""
    if isinstance(obj[0], list):
        return(sum(obj[0]))
    else:
        return(-1)
    
def objType(obj: any) -> str:
    """Retorna o tipo do objeto"""
    tipos = {int:"num",float:"num",str:"str",list:"lst",dict:"dic"}
    if obj[0] == None:
        return("nil")
    return(tipos[type(obj[0])])

def indexOf(obj: any) -> int:
    """Mostra onde argumento 0 está em argumento 1, retorna -1 em caso de erro."""
    if not(isinstance(obj[1], (list,str))):
        return(-1)
    try:
        return(obj[1].index(obj[0]))
    except:
        return(-1)
    
def stripAspas(obj: any) -> str | int:
    """Remove aspas simples das pontas de um texto, retorna -1 em caso de erro."""
    if isinstance(obj[0], str):
        if len(obj[0]) > 1 and obj[0][0] == obj[0][-1] == "'":
            copy = obj[0][:]
            return(copy[1:-1])
        return(-1)
    return(-1)