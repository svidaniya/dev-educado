# Dicionários

Um dicionário relaciona uma chave a um valor. É uma boa escolha para representar informações de uma pessoa ou produto.

```python
aluno = {
    "nome": "Marcos",
    "idade": 19,
    "curso": "Python"
}
print(aluno["nome"])
```

Neste exemplo, `nome` é uma chave e `Marcos` é seu valor. Para adicionar uma informação:

```python
aluno["nota"] = 8.5
```

Percorra um dicionário com `items`, que entrega cada chave e seu valor:

```python
for chave, valor in aluno.items():
    print(chave, ":", valor)
```

### Exercícios

1. Crie um dicionário para um livro com título, autor e ano.
2. Adicione uma nova chave a ele.

### Atividade prática

Monte um cadastro simples de contato com nome, telefone e cidade e exiba suas informações.
