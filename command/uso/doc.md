# Operações 
* Uma operação é uma expressão lógica-matemática que segue a ordem padrão de precedência.
* Operadores funcionais:

        Soma: +
        Subtração: -
        Multiplicação: *
        Divisão: /
        Parenteses: ( )
    

* Operações podem envolver números, variáveis e em alguns casos, texto. Também podem ser compostos por apenas um elemento:

        12
        Pera
        1 + (VariavelA - VariavelB)
        fruta + maca

    
    Quando uma expressão entre dois tipos diferentes é executada (e.x.: fruta + 12), um erro como o seguinte surge:

        Operação com dois tipos diferentes: int + NoneType

    Quando uma operação é mal-escrita (e.x.: +-3), um erro como o seguinte surge:

        Operação matemática malformada.







# Criando e Modificando Variáveis:
* Para criar e/ou modificar o valor de uma variável, utiliza-se a seguinte estrutura:

        set NOME VALOR.

<br>

* "NOME" deve conter apenas letras (maiúsculas ou minúsculas) ou underlines.<br>
A violação dessa regra resultará em um erro como o seguinte:

        Caractere proibido no nome da variavel. --> "set variavelLegal12 1+2", linha 1 

    A omissão do nome resultará em um erro como o seguinte:

        Comando set sem nome. --> "set ", linha 4

* "VALOR" deve ser uma [Operação](#operações).<br>
A omissão da operação resultará em um erro como o seguinte:

        Comando set sem operação. --> "set variavel", linha 4


# Usando o Console:
<details>
<summary>Comando <b> SHOW </b></summary>

* Para jogar dados no console, utiliza-se a seguinte estrutura:

        show ARGUMENTOS

* "ARGUMENTOS" pode ser composto por texto e variáveis:

        set variavel 12
        show Numero: variavel

        SAÍDA:

        Numero: 12
    A omissão de argumentos resultará em um erro como o seguinte:

        Comando show sem argumentos. --> "show", linha 1


* Para poder mostrar o nome de uma variável, envolve-se o termo com "`", chamado de indicador:

        set variavel 12
        show Valor de `variavel`: variavel

        SAÍDA:

        Valor de variavel: 12
    
    Escrever uma estrutura não-balanceada de indicadores resultará em um erro como o seguinte:

        Quantia indevida de indicadores --> "show `b", linha 2
</details>