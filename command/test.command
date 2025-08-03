function fib n
    if n = 0
        result 0
    if n = 1
        result 1
    else
        set na n-1
        execute fib na
        apply na

        set nb n-2
        execute fib nb
        apply nb

        result nb+na

function iterfib n
    set na 0
    set nb 1
    set numero n
    while n > 0
        if (n % 2) = 0
            set na na+nb
        else
            set nb na+nb
        set n n-1

    if (numero%2) = 0
        result na
    else
        result nb

while 1
    set escolha 0
    get escolha Iterativo ou Recursivo (i/r/s(para sair))? -->
    if escolha = i
        set n 0
        get n Posicao -->
        execute iterfib n
        apply n
        show n
    elif escolha = r
        set n 0
        get n Posicao -->
        execute fib n
        apply n
        show n
    elif escolha = s
        show igma
        exit
    else
        show `escolha` errada. puta