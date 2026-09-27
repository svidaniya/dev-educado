# Tipos de dados

Uma variável pode guardar tipos diferentes de valor. Conhecer o tipo evita surpresas: somar dois números é diferente de juntar dois textos.

```javascript
const nome = "Bianca";
const idade = 21;
const altura = 1.68;
const matriculado = true;
```

`nome` é uma `string`, isto é, texto entre aspas. `idade` e `altura` são `number`; JavaScript usa esse mesmo tipo para números inteiros e decimais. `matriculado` é `boolean`, um valor que só pode ser `true` ou `false`, sem aspas e em letras minúsculas.

Use `typeof` para investigar o tipo:

```javascript
const ano = 2026;
const mensagem = "2026";

console.log(typeof ano);
console.log(typeof mensagem);
```

Embora pareçam iguais para nós, o primeiro valor é número e o segundo é texto. Essa diferença importa especialmente em cálculos.

## Valores ausentes

`undefined` aparece quando uma variável foi declarada, mas ainda não recebeu valor. `null` representa uma ausência definida de propósito:

```javascript
let resposta;
const fotoDoPerfil = null;
```

Aqui, ainda não temos resposta; já sabemos que não existe foto. Por enquanto, o importante é reconhecer os dois valores.

## Convertendo texto em número

Quando uma pessoa digita algo, normalmente recebemos texto. `Number` tenta converter um texto numérico:

```javascript
const idadeDigitada = "18";
const idade = Number(idadeDigitada);
console.log(idade + 1);
```

O resultado é 19. Se o texto não for um número válido, a conversão gera `NaN` (“não é um número”).

### Erros comuns

- Escrever `"true"` pensando que é booleano; isso é texto.
- Colocar aspas em um número que será calculado.
- Usar vírgula em `1,5`; em JavaScript o decimal é `1.5`.

### Exercícios

1. Crie valores de texto, número, booleano e `null`.
2. Use `typeof` em cada um.
3. Converta `"45"` e some 5.

### Atividade prática

Crie dados de um evento: título, capacidade, preço e inscrições abertas. Mostre cada valor e seu tipo.
