# Funções

Quando uma tarefa aparece mais de uma vez, uma função ajuda a dar um nome a esse bloco de código. Criamos uma função com `def` e a executamos chamando seu nome.

```python
def mostrar_boas_vindas():
    print("Bem-vindo ao programa!")

mostrar_boas_vindas()
```

O código dentro da função só é executado quando ela é chamada. Isso deixa o programa mais organizado.

Uma função pode devolver um resultado com `return`:

```python
def dobrar(numero):
    return numero * 2

resultado = dobrar(4)
print(resultado)
```

`dobrar(4)` produz 8, que é guardado em `resultado`.

### Exercícios

1. Crie uma função que imprima seu nome.
2. Crie uma função que receba um número e devolva seu quadrado.

### Atividade prática

Faça uma função `calcular_media` que receba duas notas e devolva a média delas.
