# Tomando decisões com condicionais

Um programa nem sempre deve seguir o mesmo caminho. `if` permite executar um bloco somente quando uma condição é verdadeira.

```python
idade = int(input("Digite sua idade: "))

if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")
```

`>=` significa “maior ou igual”. Os espaços no começo de `print` são a indentação: eles mostram qual linha pertence ao `if` ou ao `else`.

Outras comparações úteis são `==` (igual), `!=` (diferente), `<` e `>`. Use `elif` quando houver mais uma possibilidade:

```python
nota = 7
if nota >= 7:
    print("Aprovado")
elif nota >= 5:
    print("Recuperação")
else:
    print("Reprovado")
```

### Erro comum

Não confunda `=` com `==`. O primeiro atribui um valor; o segundo compara.

### Exercícios

1. Informe se um número é positivo, negativo ou zero.
2. Peça uma senha e mostre uma mensagem diferente para a senha correta.

### Atividade prática

Peça duas notas, calcule a média e informe a situação do aluno.
