# Introdução à programação e ao JavaScript

Programar é escrever instruções claras para que o computador execute uma tarefa. Um programa pode calcular uma média, organizar uma lista ou responder a uma escolha. JavaScript é uma linguagem muito usada no navegador; neste curso ele será nosso instrumento para aprender lógica, sem depender de HTML ou CSS.

## Onde testar o código

Abra as ferramentas de desenvolvedor do navegador, normalmente com `F12`, e escolha a aba **Console**. Ela permite testar uma instrução por vez. Nossa primeira instrução é:

```javascript
console.log("Olá, JavaScript!");
```

`console` é o espaço de testes do navegador e `log` mostra uma mensagem nele. O texto fica entre aspas; sem elas, JavaScript procuraria uma variável com aquele nome. O ponto e vírgula marca o fim da instrução. Ao executar várias linhas, elas são processadas na ordem em que aparecem:

```javascript
console.log("Primeira mensagem");
console.log("Segunda mensagem");
```

Comentários são anotações para quem lê o código. Eles não executam:

```javascript
// Esta linha explica a próxima instrução.
console.log("Teste concluído");
```

### Erros comuns

- Escrever `Console.log`: JavaScript diferencia maiúsculas de minúsculas; use `console.log`.
- Esquecer as aspas de um texto.
- Esperar a mensagem na página; `console.log` aparece somente no Console.

### Exercícios

1. Mostre seu nome e sua cidade em duas linhas.
2. Mostre três metas de estudo, uma por `console.log`.
3. Acrescente um comentário que explique uma dessas linhas.

### Atividade prática

Crie um cartão de apresentação com quatro mensagens: saudação, nome, cidade e motivo para estudar programação.

## Materiais complementares

- [Guia JavaScript da MDN](https://developer.mozilla.org/pt-BR/docs/Web/JavaScript/Guide)
