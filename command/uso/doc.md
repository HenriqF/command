# Operações 
* Uma operação é uma expressão lógica-matemática que segue uma ordem de precedência.

<details>
<summary> Operadores </summary>

* Todos os operadores abaixo estão organizados da seguinte forma: símbolo, ordem de precedência (quanto maior, mais prioridade), função e um exemplo. 

* Operadores unários: 
        
        ! : 7 : Not lógico   : !0 = 1
        - : 7 : Menos unário : -1 = -1

* Operadores binários:

        | : 1 : Ou lógico    : 0 | 1 = 1
        & : 2 : And lógico   : 0 & 1 = 0
        + : 4 : Soma         : 1 + 2 = 3
        - : 4 : Subtração    : 1 - 2 = -1
        * : 5 : Multiplicação: 2 * 2 = 4
        / : 5 : Divisão      : 2 / 2 = 1
        % : 5 : Módulo       : 2 % 2 = 0
        ^ : 6 : Potência     : 5 ^ 3 = 125
        ~ : 0 : Aproximação  : 0~10.6 = 11 (a ~ b → arredonda o número a com b casas decimais)

* Comparadores:

        > : 3 : Maior ou igual : 10 > 5 = 1 (Retorna 1 caso (a>=b), 0 caso contrário.)
        < : 3 : Menor ou igual : 10 < 5 = 0 (Retorna 1 caso (a<=b), 0 caso contrário.)
        $ : 3 : Texto igual    : abc $ abc = 1 (Compara strings. Retonar 1 caso a = b, 0 caso contrário.)

        Nota: Se os dois primeiros comparadores (>,<) forem usados com strings, a comparação será feita com base na quantidade de caracteres: abc > abdc será executado como 3 > 4

* Parenteses:

        Usados para "roubar" prioridade:

        2*2+2 = 6
        2*(2+2) = 8

</details>

<details>
<summary> Uso </summary>

* Operações podem envolver números, variáveis e em alguns casos, texto. Também podem ser compostos por apenas um elemento:

        12
        Pera
        1 + (VariavelA - VariavelB)
        fruta + maca

</details>

<details>
<summary>Erros</summary>

* Quando uma expressão entre dois tipos diferentes é executada (e.x.: abc + 2), um erro como o seguinte surge:

        Erro : Operação com dois tipos diferentes. --> "set a abc + 2", linha 1

* Quando uma operação é mal-escrita (e.x.: +-3), um erro como o seguinte surge:

        Erro : Operação matemática malformada. --> "set a +-3", linha 1

* Quando uma operação de lógica binária é executada com texto ( abc & bcd ), um erro como o seguinte surge:

        Erro : Logica binária com valor não numérico --> "set a abc & abc", linha 1

</details>

<br>




# Variáveis:
<details>
<summary>Tipos de variaveis (dados) </summary>


* Existem três tipos principais de dados simples nessa linguagem:

        Tipo numérico (num): Qualquer número.
        Tipo string   (txt): Qualquer sequência de texto.
        Tipo nenhum   (nil): Representa uma ausência de valor.
                
* Para representar valores booleanos (verdadeiro / falso), é usado um tipo numérico. O valor 1 representa a verdade, enquanto qualquer outro é interpretado como falso.

</details>
<details>
<summary>Criando e Modificando Variaveis</summary>

* Para criar e/ou modificar o valor de uma variável, utiliza-se a seguinte estrutura:

        set NOME VALOR.

<br>

* "NOME" deve conter apenas letras (maiúsculas ou minúsculas) ou underlines.<br>
* "VALOR" é uma [OPERAÇÃO](#operações)
<details>
<summary>Erros</summary>

* Se o nome de uma variável fugir dos padrões de nomenclatura, um erro como o seguinte aparecerá:

        Erro : Caractere proibido no nome da variavel. --> "set variavel12 10", linha 1

    A omissão do nome resultará em um erro como o seguinte:

        Erro : Comando set sem nome --> "set ", linha 1

* "VALOR" deve ser uma [Operação](#operações).<br>
A omissão da operação resultará em um erro como o seguinte:

        Erro : Comando set sem operação. --> "set variavel", linha 1

</details>
</details>

<br>

# Condicionais e adjacentes

<details>
<summary>Comando <b> IF </b></summary>


* Esse comando segue a seguinte estrutura: 

        if OPERAÇÃO
            código condicional

* Ao ser executado, o comando avalia a [OPERAÇÃO](#operações). Se o resultado for 1, e SOMENTE 1, o bloco identado (código condicional) é executado.

</details>


<details>
<summary>Comando <b> ELIF </b></summary>

* Esse comando segue a seguinte estrutura: 

        if 10-10
            set a 0
        elif OPERAÇÃO
            código condicional

* Ao ser executado, o comando avalia a [OPERAÇÃO](#operações). Se o resultado for 1 e o resultado do comando condicional passado não for 1, o bloco identado (código condicional) é executado.
* É possível criar encadeamentos com esse comando:

        if 0
            show ok!
        elif 0
            show ok!
        elif 1
            show EXECUTADO!
        elif 1
            show ok!

        SAÍDA:

        EXECUTADO!



</details>


<details>
<summary>Comando <b> ELSE </b></summary>

* Esse comando segue a seguinte estrutura: 

        if 10-10
            set a 0
        else
            código condicional

* Caso o resultado do comando condicional passado não seja 1, o bloco de código identado (código condicional) será executado.
</details>

<details>
<summary>Erros </summary>

* Caso seja criado um "if" ou um "elif" sem operação, um erro como o seguinte aparecerá:

        Erro : Condicional sem argumento. --> "if ", linha 1

* Caso seja criada uma condicional sem corpo (código identado), um erro como o seguinte aparecerá:

        Erro : Condicional sem corpo --> "if 10", linha 1



</details>


<br>

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



* Para poder mostrar o nome de uma variável, envolve-se o termo com "`", chamado de indicador:

        set variavel 12
        show Valor de `variavel`: variavel

        SAÍDA:

        Valor de variavel: 12
    

<details>
<summary>Erros</summary>

* Escrever uma estrutura não-balanceada de indicadores resultará em um erro como o seguinte:

        Erro : Quantia indevida de indicadores. --> "show `a", linha 2

* A omissão de argumentos resultará em um erro como o seguinte:

        Erro : Comando show sem argumentos. --> "show", linha 1
</details>


</details>