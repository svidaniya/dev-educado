# Trabalhando com textos

Uma string é um texto. Além de guardar frases, ela possui operações úteis.

```python
frase = "Python é divertido"
print(frase.upper())
print(frase.lower())
print(len(frase))
```

`upper` cria uma versão em maiúsculas, `lower` em minúsculas e `len` informa quantos caracteres existem. Essas operações não alteram a variável original neste caso.

Use `strip` para remover espaços nas pontas e `in` para verificar se um trecho aparece no texto:

```python
email = input("Digite seu e-mail: ").strip()
if "@" in email:
    print("Parece um e-mail.")
```

### Exercícios

1. Peça um nome e mostre-o em letras maiúsculas.
2. Conte quantos caracteres há em uma palavra.

### Atividade prática

Peça uma frase e informe se ela contém a palavra `Python`.

## Materiais complementares

- [Métodos de strings no Python](https://docs.python.org/pt-br/3/library/stdtypes.html#string-methods)
