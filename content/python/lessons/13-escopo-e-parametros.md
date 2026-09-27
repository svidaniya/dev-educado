# Parâmetros e escopo

Parâmetros são valores que uma função recebe para trabalhar de maneiras diferentes. Eles são escritos entre parênteses na definição.

```python
def saudacao(nome):
    print("Olá,", nome)

saudacao("Carla")
saudacao("Rui")
```

`nome` recebe o valor enviado em cada chamada. Uma variável criada dentro de uma função normalmente só existe ali; isso é chamado de escopo local.

```python
def calcular_desconto(preco, percentual):
    desconto = preco * percentual / 100
    return preco - desconto

valor_final = calcular_desconto(100, 10)
print(valor_final)
```

`desconto` é usada apenas durante a execução da função. Devolver o resultado com `return` é mais claro do que depender de uma variável criada fora dela.

### Exercícios

1. Crie uma função que receba nome e cidade e mostre uma saudação.
2. Crie uma função que receba dois números e devolva o maior deles.

### Atividade prática

Crie uma função para calcular o preço final de um produto após aplicar uma porcentagem de desconto.
