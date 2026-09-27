# Operadores e cálculos

Operadores são símbolos que realizam ações com valores. Os aritméticos mais comuns são `+`, `-`, `*` e `/`.

```javascript
const precoUnitario = 12.5;
const quantidade = 3;
const total = precoUnitario * quantidade;

console.log(total);
```

As duas primeiras linhas guardam os dados da compra. A terceira multiplica preço por quantidade e guarda 37.5 em `total`. Os operadores `%` e `**` calculam, respectivamente, o resto de uma divisão e uma potência:

```javascript
console.log(17 % 2);
console.log(2 ** 3);
```

O primeiro resultado é 1; isso ajuda a verificar se um número é par. O segundo é 8.

## O comportamento de `+`

Com números, `+` soma. Com texto, junta valores:

```javascript
console.log(10 + 5);
console.log("10" + 5);
```

Os resultados são `15` e `"105"`. Antes de calcular algo vindo de `prompt`, transforme o texto com `Number`.

## Comparações

Comparações devolvem `true` ou `false` e serão usadas nas decisões da próxima aula:

```javascript
const nota = 8;
console.log(nota >= 7);
console.log(nota === 10);
console.log(nota !== 5);
```

`>=` significa maior ou igual; `===` compara valor e tipo; `!==` verifica se são diferentes. Prefira `===` a `==`, pois a comparação estrita evita conversões inesperadas.

Também podemos atualizar uma variável com uma conta:

```javascript
let saldo = 100;
saldo = saldo - 25;
saldo += 10;
console.log(saldo);
```

O saldo termina em 85. `saldo += 10` é uma forma reduzida de `saldo = saldo + 10`.

### Erros comuns

- Comparar com `=` em vez de `===`.
- Calcular com texto em vez de número.
- Usar `==` e obter uma comparação confusa entre tipos.

### Exercícios

1. Calcule o total de quatro produtos de R$ 7,50.
2. Calcule a média de três notas.
3. Encontre o resto de 25 dividido por 2.
4. Compare uma idade com 18 usando `>=`.

### Atividade prática

Peça preço e quantidade com `prompt`, converta ambos, calcule o total e mostre uma template string. Compare o total com 100 e exiba o resultado no Console.
