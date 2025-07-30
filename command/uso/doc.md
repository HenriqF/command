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


<details>
<summary>Erros</summary>

* Quando uma expressão entre dois tipos diferentes é executada (e.x.: fruta + 12), um erro como o seguinte surge:

        Operação com dois tipos diferentes: num + nil

* Quando uma operação é mal-escrita (e.x.: +-3), um erro como o seguinte surge:

        Operação matemática malformada.

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

        Caractere proibido no nome da variavel. --> "set variavelLegal12 1+2", linha 1 

    A omissão do nome resultará em um erro como o seguinte:

        Comando set sem nome. --> "set ", linha 4

* "VALOR" deve ser uma [Operação](#operações).<br>
A omissão da operação resultará em um erro como o seguinte:

        Comando set sem operação. --> "set variavel", linha 4
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

        Quantia indevida de indicadores --> "show `b", linha 2

* A omissão de argumentos resultará em um erro como o seguinte:

        Comando show sem argumentos. --> "show", linha 1
</details>


</details>