# Projeto final: lista de tarefas

Neste projeto, você criará uma lista de tarefas para o terminal. Ela usa lista, dicionário, funções, repetição, condicionais, tratamento de erro e arquivo.

Comece com uma lista vazia e funções pequenas:

```python
tarefas = []

def adicionar_tarefa(descricao):
    tarefa = {"descricao": descricao, "concluida": False}
    tarefas.append(tarefa)

def listar_tarefas():
    for indice, tarefa in enumerate(tarefas, start=1):
        status = "[x]" if tarefa["concluida"] else "[ ]"
        print(indice, status, tarefa["descricao"])
```

`enumerate` numera os itens para a pessoa escolher uma tarefa. Depois, crie um menu com `while` e as opções: adicionar, listar, concluir e sair. Ao concluir, peça o número da tarefa, converta-o com `int` e use `try`/`except` para lidar com entradas inválidas.

Quando a versão básica funcionar, salve as descrições no arquivo `tarefas.txt`. Ao iniciar, leia o arquivo se ele existir. Não se preocupe em deixar o projeto perfeito: primeiro faça cada parte funcionar e teste uma por vez.

### Roteiro sugerido

1. Crie e teste `adicionar_tarefa`.
2. Liste as tarefas com número e status.
3. Faça o menu repetir até a opção sair.
4. Marque uma tarefa como concluída.
5. Salve as tarefas em arquivo.

### Desafio opcional

Permita remover uma tarefa pelo número. Antes de remover, confira se o número existe.
