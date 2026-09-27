# Leitura e escrita de arquivos

Arquivos permitem que dados continuem existindo depois que o programa termina. `open` abre um arquivo; o modo `"w"` escreve e cria ou substitui o arquivo.

```python
with open("recado.txt", "w", encoding="utf-8") as arquivo:
    arquivo.write("Lembrar de estudar Python.\n")
```

`with` fecha o arquivo automaticamente quando o bloco termina. A opção `encoding="utf-8"` preserva acentos. Use `"a"` para acrescentar sem apagar o conteúdo anterior.

Para ler, use o modo `"r"`:

```python
with open("recado.txt", "r", encoding="utf-8") as arquivo:
    conteudo = arquivo.read()

print(conteudo)
```

Se o arquivo ainda não existir, a leitura gera `FileNotFoundError`, que pode ser tratado com `try` e `except`.

### Exercícios

1. Escreva seu nome em um arquivo de texto.
2. Leia o arquivo e mostre seu conteúdo.

### Atividade prática

Faça um programa que acrescente uma tarefa por linha em `tarefas.txt`.

## Materiais complementares

- [Leitura e escrita de arquivos no tutorial oficial](https://docs.python.org/pt-br/3/tutorial/inputoutput.html#reading-and-writing-files)
