# Repetição com for

Um loop, ou laço de repetição, repete um trecho de código. `for` é ótimo quando sabemos quantas vezes queremos repetir algo.

```python
for numero in range(1, 6):
    print(numero)
```

`range(1, 6)` produz os números de 1 até 5; o último limite não entra. A variável `numero` recebe um valor diferente em cada volta.

Também podemos percorrer letras de um texto:

```python
for letra in "sol":
    print(letra)
```

### Exercícios

1. Mostre os números de 1 a 10.
2. Mostre a tabuada do 5, de 1 a 10.

### Atividade prática

Peça um número inteiro e use `for` para calcular a soma de 1 até esse número.

## Materiais complementares

- [Função range na documentação do Python](https://docs.python.org/pt-br/3/library/stdtypes.html#range)
