# Módulos e importações

Um módulo é um arquivo que reúne recursos prontos do Python. Para usar um recurso de outro módulo, escrevemos `import`.

```python
import math

raiz = math.sqrt(81)
print(raiz)
```

`math` é um módulo da biblioteca padrão: ele já vem com Python. `math.sqrt(81)` calcula a raiz quadrada de 81.

Também podemos importar apenas uma função:

```python
from random import randint

numero = randint(1, 6)
print(numero)
```

`randint(1, 6)` devolve um inteiro aleatório entre 1 e 6, incluindo os limites. Não instale bibliotecas externas para os exercícios deste curso.

### Exercícios

1. Use `math.sqrt` para calcular a raiz de 144.
2. Simule o lançamento de um dado com `randint`.

### Atividade prática

Crie um jogo simples que sorteie um número de 1 a 10 e peça um palpite.

## Materiais complementares

- [Biblioteca padrão do Python](https://docs.python.org/pt-br/3/library/)
