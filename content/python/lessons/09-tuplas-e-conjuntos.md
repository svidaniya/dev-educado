# Tuplas e conjuntos

Tuplas também guardam vários valores, mas são feitas para dados que não devem mudar. Elas usam parênteses:

```python
dias = ("segunda", "terça", "quarta")
print(dias[1])
```

Você pode ler uma tupla como uma lista, mas não pode usar `append` nela.

Conjuntos, criados com chaves, guardam valores sem repetição:

```python
cores = {"azul", "verde", "azul"}
print(cores)
```

Mesmo com `azul` escrito duas vezes, o conjunto terá apenas um `azul`. A ordem dos itens de um conjunto não deve ser usada como referência.

### Exercícios

1. Faça uma tupla com os meses de férias que você prefere.
2. Crie um conjunto com números repetidos e observe o resultado.

### Atividade prática

Leia cinco cores em uma lista e crie um conjunto a partir dela para descobrir quantas cores diferentes foram informadas.
