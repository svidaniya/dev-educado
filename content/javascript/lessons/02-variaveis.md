# Variáveis e constantes

Programas precisam lembrar valores para usá-los depois. Uma variável é um nome associado a um valor. Em vez de repetir o preço de um produto em várias linhas, podemos guardá-lo e usar esse nome de forma clara.

```javascript
let produto = "Caderno";
let preco = 18;

console.log(produto);
console.log(preco);
```

`let` cria a variável. A primeira linha guarda o texto `"Caderno"` em `produto`; a segunda guarda o número `18` em `preco`. Quando o programa lê `console.log(produto)`, substitui o nome pelo valor armazenado.

## Quando usar `let`

Use `let` quando o valor pode mudar. Um contador é um caso frequente:

```javascript
let pontos = 0;
console.log(pontos);

pontos = 10;
console.log(pontos);
```

O primeiro resultado é 0 e o segundo é 10. Na atualização não escrevemos `let` outra vez, pois a variável já existe. O `=` significa “recebe o valor da direita”.

## Quando usar `const`

Use `const` para valores que não devem ser trocados durante o programa:

```javascript
const nomeDaEscola = "Escola Central";
console.log(nomeDaEscola);
```

Tentar fazer `nomeDaEscola = "Outra escola"` causa erro. Uma boa regra inicial é usar `const` e trocar para `let` apenas quando houver uma atualização real. Evite `var`: é uma forma antiga de declarar variáveis e tem regras mais confusas.

## Nomes claros

Prefira `totalDaCompra` a `x`. JavaScript costuma usar camelCase: a primeira palavra em minúscula e as seguintes iniciadas em maiúscula. Nomes não podem ter espaço, começar com número ou ser palavras reservadas como `let`.

### Erros comuns

- Declarar uma constante e tentar alterar seu valor.
- Usar `nome completo` em vez de `nomeCompleto`.
- Misturar `Nome` e `nome`; para JavaScript são variáveis diferentes.

### Exercícios

1. Crie constantes para seu nome e cidade.
2. Crie `let quantidadeLivros = 2`, atualize para 3 e mostre os valores.
3. Reescreva três nomes de variáveis pouco claros usando camelCase.

### Atividade prática

Guarde nome, preço e estoque de um produto. Use `let` para estoque, diminua uma unidade e mostre o estoque antes e depois.
