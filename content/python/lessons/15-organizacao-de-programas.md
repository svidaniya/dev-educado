# Organização simples de programas

À medida que um programa cresce, separar tarefas em funções torna a leitura mais fácil. Uma boa função faz uma coisa clara e tem um nome que explica sua intenção.

```python
def ler_nota():
    return float(input("Digite uma nota: "))

def situacao(media):
    if media >= 7:
        return "Aprovado"
    return "Reprovado"

nota1 = ler_nota()
nota2 = ler_nota()
media = (nota1 + nota2) / 2
print(situacao(media))
```

O programa fica dividido em leitura e decisão. Comentários curtos podem explicar escolhas, mas nomes claros reduzem a necessidade deles.

Também é útil ter um ponto de início:

```python
def main():
    print("Programa iniciado")

main()
```

### Exercícios

1. Transforme um programa anterior em pelo menos duas funções.
2. Dê nomes mais claros às variáveis de um cálculo.

### Atividade prática

Organize um programa de média em funções para ler notas, calcular a média e mostrar o resultado.
