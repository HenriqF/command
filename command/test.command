set numeroA 0
set numeroB 1

set numero 0
get numero Numero-->
while numero > 0
    if (numero % 2) = 0
        set numeroA numeroA + numeroB
    else
        set numeroB numeroA + numeroB
    set numero numero - 1

if (numero % 2) = 0
    show Pronto! numeroA
else
    show Pronto! numeroB