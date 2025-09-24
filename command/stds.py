from nos import Erro
import random

funcArgs = {
    "objLength" : 1,
    "objSort" : 1,
    "showList" : 1,
    "sumList": 1,
    "objType": 1,
    "stripAspas": 1,

    "indexOf": 2,
    "randomNum": 2,
}
def stdFuncs():
    return funcArgs

def stdHandler(node, vars):
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

def randomNum(obj):
    if isinstance(obj[0], int) and isinstance(obj[1], int):
        if obj[0] < obj[1]:
            return(random.randint(obj[0], obj[1]))
        return(-1)
    return(-1)

def objLength(obj):
    if isinstance(obj[0], (str,list,dict)):
        return(len(obj[0]))
    else:
        return(-1)
    
def objSort(obj):
    if isinstance(obj[0], list):
        return(sorted(obj[0]))
    elif isinstance(obj[0], str):
        return(''.join(sorted(obj[0])))
    else:
        return(-1)

def showList(obj):
    if isinstance(obj[0], list):
        print("[" + ' ,'.join([str(x) for x in obj[0]]) + "]")
    else:
        return(-1)
    
def sumList(obj):
    if isinstance(obj[0], list):
        return(sum(obj[0]))
    else:
        return(-1)
    
def objType(obj):
    tipos = {int:"num",float:"num",str:"str",list:"lst",dict:"dic"}
    if obj[0] == None:
        return("nil")
    return(tipos[type(obj[0])])

def indexOf(obj):
    if not(isinstance(obj[1], (list,str))):
        return(-1)
    try:
        return(obj[1].index(obj[0]))
    except:
        return(-1)
    
def stripAspas(obj):
    if isinstance(obj[0], str):
        if len(obj[0]) > 1 and obj[0][0] == obj[0][-1] == "'":
            copy = obj[0][:]
            return(copy[1:-1])
        return(-1)
    return(-1)