# Entrada e saída de dados

`print` mostra uma saída para quem usa o programa. Para receber uma resposta digitada, usamos `input`:

```python
nome = input("Digite seu nome: ")
print("Olá,", nome)
```

O texto dentro de `input` é o convite mostrado na tela. A resposta é guardada em `nome`. `input` sempre devolve texto, mesmo quando a pessoa digita um número.

Para transformar um texto numérico em inteiro, use `int`:

```python
ano_nascimento = int(input("Em que ano você nasceu? "))
idade_aproximada = 2026 - ano_nascimento
print("Você tem aproximadamente", idade_aproximada, "anos.")
```

Aqui, `int` converte a resposta para que a subtração seja possível. Se a pessoa digitar letras, essa conversão falhará; aprenderemos a lidar com isso mais adiante.

### Exercícios

1. Peça o nome e a cidade de uma pessoa e mostre uma frase.
2. Peça dois números inteiros e mostre-os na tela.

### Atividade prática

Crie um programa que pergunte a idade atual e informe a idade que a pessoa terá no próximo ano.
