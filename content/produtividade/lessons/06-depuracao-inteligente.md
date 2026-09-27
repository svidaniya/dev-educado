# Depuração sem tentativa aleatória

Depurar é investigar por que um programa não faz o que deveria. O objetivo não é adivinhar uma alteração que funcione, mas reduzir a incerteza até encontrar a causa.

Leia a mensagem de erro inteira. Ela costuma informar o tipo de problema, o arquivo e a linha. Em seguida, descreva o comportamento esperado e o comportamento observado. “Não funciona” é vago; “a soma mostra 23 quando digito 2 e 3” já é uma hipótese útil: talvez os valores sejam texto.

## Um processo de investigação

1. Reproduza o erro com um caso pequeno.
2. Localize a primeira linha suspeita.
3. Mostre valores e tipos com uma saída temporária, como `console.log(valor, typeof valor)`.
4. Altere uma hipótese por vez.
5. Execute o caso novamente e remova os registros temporários quando terminar.

Pesquisar faz parte da depuração. Procure a mensagem exata e acrescente o contexto da linguagem ou biblioteca. Ao pedir ajuda, mostre o objetivo, o erro, o trecho mínimo relevante e o que já tentou.

### Exercícios

1. Pegue um erro antigo e reescreva sua descrição de modo específico.
2. Crie um exemplo onde `"2" + 3` gera resultado inesperado e investigue com `typeof`.

### Atividade prática

Use o processo de cinco passos para resolver um erro real ou inventado e escreva uma frase sobre a causa encontrada.
