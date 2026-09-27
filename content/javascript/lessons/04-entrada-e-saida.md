# Entrada e saída de dados

`console.log` é uma saída: ele mostra o resultado no Console. Um programa se torna mais interessante quando recebe informações. No navegador, `prompt` abre uma caixa para a pessoa digitar.

```javascript
const nome = prompt("Qual é o seu nome?");
console.log("Olá,", nome);
```

`prompt` mostra a pergunta e devolve a resposta para `nome`. Mesmo que a pessoa digite `25`, o resultado é o texto `"25"`. Por isso, converta valores antes de calcular:

```javascript
const textoDaIdade = prompt("Qual é a sua idade?");
const idade = Number(textoDaIdade);

console.log("No próximo ano você terá", idade + 1, "anos.");
```

`Number` transforma a resposta em número e permite que `idade + 1` seja uma soma.

## Mensagens com template strings

Crases criam template strings. Dentro delas, `${}` insere valores de variáveis:

```javascript
const produto = prompt("Produto comprado:");
const preco = Number(prompt("Preço:"));

console.log(`Você comprou ${produto} por R$ ${preco}.`);
```

Use crases, não aspas simples, para esse formato. Ele evita muitas concatenações e deixa a mensagem mais fácil de ler.

### Erros comuns

- Esquecer `Number` para um valor que será calculado.
- Usar aspas em vez de crases numa template string.
- Digitar letras em uma resposta que o programa espera converter para número.

### Exercícios

1. Pergunte o nome e mostre uma saudação.
2. Peça dois números, converta-os e mostre a soma.
3. Peça uma cidade e monte uma frase com template string.

### Atividade prática

Peça nome e horas estudadas hoje. Mostre uma mensagem personalizada dizendo quantas horas a pessoa estudou.

## Materiais complementares

- [Função prompt na MDN](https://developer.mozilla.org/pt-BR/docs/Web/API/Window/prompt)
