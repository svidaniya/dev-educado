# Repetição com while

`while` repete enquanto uma condição for verdadeira. É útil quando ainda não sabemos quantas tentativas serão necessárias.

```python
tentativas = 0

while tentativas < 3:
    print("Tentativa", tentativas + 1)
    tentativas = tentativas + 1
```

No início, `tentativas` vale 0. A cada volta ela aumenta em 1, até a condição deixar de ser verdadeira. Sem essa atualização, o loop nunca terminaria.

```python
resposta = ""
while resposta != "sair":
    resposta = input("Digite 'sair' para encerrar: ")
```

### Erro comum

Evite criar um loop infinito. Sempre verifique se alguma variável usada na condição muda dentro do bloco.

### Exercícios

1. Peça números até que a pessoa digite 0.
2. Peça uma senha até ela ser igual a uma senha definida no programa.

### Atividade prática

Crie um contador regressivo que começa em 10 e termina em 1.
