# Listas

Uma lista reúne vários valores em uma única variável. Ela usa colchetes e os itens são separados por vírgulas.

```python
frutas = ["maçã", "banana", "uva"]
print(frutas[0])
```

O primeiro item tem posição 0, então o resultado é `maçã`. Para acrescentar um item, use `append`:

```python
frutas.append("laranja")
print(frutas)
```

Podemos percorrer uma lista com `for`:

```python
for fruta in frutas:
    print(fruta)
```

### Erro comum

Tentar acessar uma posição que não existe causa erro. Uma lista com três itens só possui posições 0, 1 e 2.

### Exercícios

1. Crie uma lista com três filmes de que você gosta.
2. Acrescente outro filme e mostre todos usando `for`.

### Atividade prática

Peça três nomes, guarde-os em uma lista e exiba a lista ao final.
