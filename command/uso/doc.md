# Operações 
* Uma operação é uma expressão lógica-matemática que segue uma ordem de precedência.

<details>
<summary> Operadores </summary>

* Todos os operadores abaixo estão organizados da seguinte forma: símbolo, ordem de precedência (quanto maior, mais prioridade), função e um exemplo. 

* Operadores unários: 
        
        ! : 7 : Not lógico   : !0 = 1
        - : 7 : Negação      : -1 = 1 * -1

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

        > : 3 : Maior          : 10 > 5 = 1 (Retorna 1 caso (a>b), 0 caso contrário.)
        < : 3 : Menor          : 10 < 5 = 0 (Retorna 1 caso (a<b), 0 caso contrário.)
        = : 3 : Igualdade      : 10 = 10 = 1 (Retorna 1 caso (a=b), 0 caso contrário.)

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

* Quando uma operação é realizada entre dois tipos diferentes sem ter suporte, um erro como o seguinte aparece:

        Erro : Operação proibida com tipos diferentes. --> "set a 35 + alpha", linha 1

* Quando uma operador é usado da forma incorreta, um erro como o seguinte aparece:

        Erro : Operador mal-usado. --> "set a -sigma", linha 1

* Quando se tenta negar um valor não inteiro, um erro como o seguinte aparece:

        Erro : Negação de não-inteiro --> "set a !10.5", linha 1

* Quando se tenta dividir por 0, um erro como o seguinte aparece:

        Erro : Divisão por zero. --> "set a 10 / 0", linha 1

* Quando se tenta obter o modulo 0, um erro como o seguinte aparece:
        
        Erro : Modulo com zero. --> "set a 10 % 0", linha 1

* Quando se tenta usar o comparador de textos com números, um erro como o seguinte aparece:

        Erro : Comparador de texto com tipo numérico --> "set a 10 $ 20", linha 1

* Quando se escreve uma operação incorreta, um erro como o seguinte aparece:

        Erro : Operação malformada --> "set a --2", linha 1

* Quando parenteses não estão balanceados, um erro como o seguinte aparece:

        Erro : Parenteses não-balanceados. --> "set a 1 > 2)", linha 1


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

* "NOME" deve conter apenas letras (maiúsculas ou minúsculas).<br>
* "VALOR" é uma [OPERAÇÃO](#operações)
<details>
<summary>Erros</summary>

* Se um número for encontrado no nome de uma variável, um erro como o seguinte aparecerá:

        Erro : Numero em nome de variável. --> "set numero0 0", linha 1

* Quando um comando set é usado sem seguir a estrutura padrão, um erro como o seguinte aparece:

        Erro : Comando set com operação malformada. --> "set numero", linha 1

</details>
</details>

<br>

# Condicionais

<details>
<summary>Comando <b> if </b></summary>


* Esse comando segue a seguinte estrutura: 

        if OPERAÇÃO
            código condicional

* Ao ser executado, o comando avalia a [OPERAÇÃO](#operações). Se o resultado for 1, e SOMENTE 1, o bloco identado (código condicional) é executado.

</details>


<details>
<summary>Comando <b> elif </b></summary>

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
<summary>Comando <b> else </b></summary>

* Esse comando segue a seguinte estrutura: 

        if 10-10
            set a 0
        else
            código condicional

* Caso o resultado do comando condicional passado não seja 1, o bloco de código identado (código condicional) será executado.
</details>

<details>
<summary>Casos especiais </b></summary>

* O comando [while](#loops), por também conter uma "condicional", pode entrar em um encadeamento de condicionais:

        set a 5
        while a > 0
            set a a-1
        elif a = 0
            show Agora, `a` e nulo!

        SAÍDA:

        Agora, a e nulo!

</details>

<details>
<summary>Erros </summary>

* Caso seja criado um "if" ou um "elif" sem operação, um erro como o seguinte aparecerá:

        Erro : Condicional sem argumento. --> "if ", linha 1

* Caso seja criada uma condicional sem corpo (código identado), um erro como o seguinte aparecerá:

        Erro : Comando sem corpo --> "if 10", linha 1



</details>


<br>

# Loops
<details>
<summary> Comando <b> while </b> </summary>

* Um loop, ou ciclo, é uma estrutura que repete uma porção de código.
* Para criar um loop, usa-se a seguinte estrutura:

        while OPERAÇÃO
            código

* Enquanto o valor da [OPERAÇÃO](#operações) for igual a 1, o código identado será executado.
* Após cada execução, a operação é reavaliada. Se por ventura deixar de valer 1, o ciclo é quebrado e o programa segue.

<details>
<summary>Erros</summary>

* Quando é usado esse comando sem uma operação, um erro como o seguinte aparece:

        Erro : Loop sem argumento. --> "while ", linha 1

* Caso seja criado um while sem corpo (código identado), um erro como o seguinte aparecerá:

        Erro : Comando sem corpo --> "while 1 ", linha 1

</details>

</details>



<br>

# Funções
<details>
<summary>Comando <b> function </b> </summary>

* Usado para definir funções, segue a seguinte estrutura:

        function NOME
            código

* Há também um subcomando: <b>result</b>. Ele é utilizado para declarar que a função terminou de executar:

        function Nome
            código
            result

* Ele também pode ser usado para retornar o valor de uma variável usada dentro da função:

        function Nome
            set a 10
            result a

<details>
<summary>Erros </summary>

* Quando é criada uma função sem nome, aparece um erro como o seguinte: 

        Erro : Funcao sem argumento. --> "function", linha 1

* Quando uma função não tem corpo identado, aparece um erro como o seguinte:

        Erro : Comando sem corpo --> "function a", linha 1

* Quando tenta-se criar uma função cujo nome já foi usado em outra, um erro como o seguinte aparece:

        Erro : Uma função com tal nome já existe. --> "function a", linha 3

* Quando é dado mais de um argumento ao comando result, um erro como o seguinte aparece:

        Erro : Argumentos em demasia. --> "    result a b", linha 2

* Quando um result é usado fora de função, um erro como o seguinte aparece:

        Erro : Result sem função. --> "result", linha 1

* Quando um result tenta usar uma variável não declarada, um erro como o seguinte aparece:

        Erro : Result de variável não declarada --> "    result a", linha 2
</details>
<br>
</details>



<details>
<summary>Comando <b> execute </b> </summary>

* Usado para executar uma função, segue a seguinte estrutura:

        execute NOMEFUNCAO

<details>
<summary>Erros </summary>

* Quando não é dado um nome de função ao comando execute, um erro como o seguinte aparece:

        Erro : Execute sem nome. --> "execute", linha 1

* Quando se tenta executar uma função que não existe, um erro como o seguinte aparece:

        Erro : Funcao inexistente. --> "execute a", linha 1
</details>
<br>
</details>



<details>
<summary>Comando <b> apply </b> </summary>

* Usado para aplicar o valor retornado de uma função a uma variavel. Segue a seguinte estrutura:

        set variavel 0
        execute funcao
        apply variavel

* O valor retornado de funcao é aplicado a variavel.

<details>
<summary>Erros </summary>

* Quando é dada uma quantia indevida de argumentos ao comando apply, um erro como o seguinte aparece:

        Erro : Comando apply com quantia indevida de argumentos. --> "apply variavel a", linha 6

* Quando se tenta aplicar a uma variavel não declarada, um erro como o seguinte aparece:

        Erro : Apply em variavel não declarada. --> "apply variav ", linha 6

* Quando o comando antes de um apply não é um execute, um erro como o seguinte aparece:

        Erro : Comando antes de apply não é execute. --> "apply variavel", linha 7


</details>
<br>

</details>
<br>


# Usando o Console:
<details>
<summary>Comando <b> show </b></summary>

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


<details>
<summary>Comando <b> get </b></summary>

* Para jogar dados no console, utiliza-se a seguinte estrutura:

        get VARIAVEL ARGUMENTOS

* VARIAVEL deve ser o nome de uma variável já declarada
* ARGUMENTOS é um trecho opicional, um texto que aparece no console quando o comando é executado.

<details>
<summary>Erros</summary>

* Tentar usar o comando get com uma variável não declarada resulta em um erro como o seguinte:

        Erro : Comando get em variável não declarada. --> "get var", linha 1

* Tentar usar o comando get sem nomear uma variável resulta em um erro como o seguinte:

        Erro : Comando get sem variável. --> "get", linha 1

* Não separar a variável do argumento resulta em um erro como o seguinte:

        Erro : Comando get com argumentos misturados. --> "get var-->", linha 2

</details>
</details>
<br>

# Miscelâneos:

* Comando <b>exit</b>    : Serve para terminar a execução do script;
* Comando <b>nothing</b> : Serve principalmente para testes. Não faz nada.

<details>
<summary> Erros </summary>

* Quando é usado um comando desconhecido, um erro como o seguinte aparece:

        Erro : Comando desconhecido. --> "comandoincrivel = 20", linha 1
</details>