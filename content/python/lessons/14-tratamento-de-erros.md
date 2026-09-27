# Tratamento básico de erros

Algumas entradas podem ser inválidas. Por exemplo, `int("dez")` não pode virar um inteiro. `try` e `except` permitem orientar a pessoa sem encerrar o programa de forma inesperada.

```python
try:
    idade = int(input("Digite sua idade: "))
    print("Idade informada:", idade)
except ValueError:
    print("Digite apenas um número inteiro.")
```

O código em `try` é tentado primeiro. Se ocorrer `ValueError` durante a conversão, o bloco `except` é executado.

Para pedir novamente, combine com `while`:

```python
while True:
    try:
        numero = int(input("Digite um número: "))
        break
    except ValueError:
        print("Entrada inválida. Tente novamente.")
```

`break` encerra o loop depois de uma resposta válida.

### Exercícios

1. Proteja a leitura de um preço usando `try` e `except ValueError`.
2. Peça um número até que a pessoa digite um inteiro válido.

### Atividade prática

Faça uma calculadora de soma que trate entradas não numéricas.
