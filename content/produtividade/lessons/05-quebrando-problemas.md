# Quebrando problemas em partes menores

Problemas de programação parecem difíceis quando são descritos como um todo: “fazer um sistema de tarefas” ou “corrigir o login”. Quebrar o problema é transformá-lo em partes que possam ser entendidas, testadas e concluídas separadamente.

Imagine uma lista de tarefas. Antes de codificar, separe: representar uma tarefa, adicionar uma tarefa, listar, marcar como concluída e remover. Cada parte tem uma pergunta mais simples e pode ser testada antes da próxima.

## Do requisito ao teste

Para cada etapa, escreva entrada, processamento e saída. Em “adicionar tarefa”, a entrada é uma descrição; o processamento cria e armazena o item; a saída é a lista atualizada. Essa estrutura ajuda a descobrir o que ainda não está claro.

Use exemplos pequenos. Em vez de testar com vinte tarefas, crie uma. Se falhar, observe valores e mensagens. Só avance quando a parte atual tiver um comportamento que você consegue explicar.

### Erros comuns

- Começar a codificar antes de decidir o que a função deve receber e devolver.
- Tentar corrigir vários erros ao mesmo tempo.
- Considerar uma tarefa “quase pronta” sem um teste simples.

### Exercícios

1. Escolha um programa pequeno e divida-o em cinco partes.
2. Para duas partes, escreva entrada, processamento e saída.

### Atividade prática

Pegue um exercício pendente e faça somente a menor parte testável. Registre o que falta sem tentar concluir tudo na mesma sessão.
