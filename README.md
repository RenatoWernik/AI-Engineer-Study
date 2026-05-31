# AI-Engineer-Study
My real journey reinforcing basic to advanced Python concepts without using AI - To become a better AI Engineer.

-Linkedin: https://www.linkedin.com/in/renato-wernik-ab389a276/


#Project 01 - Task Manager:

Pequeno gestor de tarefas em linha de comandos, construído do zero
como primeiro projeto sem seguir um molde, durante a minha jornada
de estudo de Python.

## O que faz
- Adicionar uma tarefa
- Ver todas as tarefas
- Editar uma tarefa existente
- Remover uma tarefa
- Validação de input para não rebentar quando a lista está vazia
  ou quando se tenta remover/editar uma tarefa que não existe

## Conceitos aplicados
- Listas
- Loop while para manter o programa a correr
- Condicionais if-elif-else para o menu de opções
- Métodos de lista: append, remove, index
- join para mostrar as tarefas de forma legível

## O que aprendi
Implementei as quatro operações fundamentais do CRUD (Create, Read,
Update, Delete) a partir do zero. Percebi também que os dados ficam
guardados apenas na memória RAM enquanto o programa corre, ou seja,
desaparecem quando o programa fecha. O próximo passo natural seria
adicionar persistência (guardar em ficheiro), para que as tarefas
sobrevivam entre execuções.

## Limitações conhecidas
- Identificação de tarefas é feita pelo nome, por isso tarefas com
  nomes iguais não são distinguidas corretamente. Resolver isto bem
  pede dicionários e IDs, o próximo conceito que vou aprender.
