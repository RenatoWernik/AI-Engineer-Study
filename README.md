# AI-Engineer-Study
My real journey reinforcing basic to advanced Python concepts without using AI - To become a better AI Engineer.

-Linkedin: https://www.linkedin.com/in/renato-wernik-ab389a276/


#Project 01 - Task Manager(project01-task_manager.py):

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



#Project 02 - Task Manager(project02-task_manager_v2.py):
Segunda versão do gestor de tarefas em linha de comandos, reescrita do
zero usando dicionários em vez de listas. Construída de cabeça, sem
consultar a versão 1, dias depois de a ter feito, para reforçar os
conceitos pela memória e não pela cópia.

## O que mudou em relação à versão 1
Na versão 1, cada tarefa era apenas um texto guardado numa lista, e as
tarefas eram identificadas pelo nome. Isto criava um problema: duas
tarefas com o mesmo nome eram indistinguíveis.

Nesta versão, cada tarefa tem um ID único (número) gerado
automaticamente. A estrutura passou a ser um dicionário, em que a chave
é o ID e o valor é o texto da tarefa. O utilizador passa a escolher as
tarefas pelo ID, o que resolve de vez o problema das tarefas com nomes
iguais.

## O que faz
- Adicionar uma tarefa, com ID único gerado automaticamente
- Ver todas as tarefas, mostrando ID e descrição numa linha cada
- Editar uma tarefa existente, escolhida pelo ID
- Remover uma tarefa, escolhida pelo ID
- Validação para não rebentar quando a lista está vazia ou quando se
  tenta editar/remover um ID que não existe

## Conceitos aplicados
- Dicionários (chave-valor) como estrutura principal
- Atribuição direta para adicionar/atualizar: dicionario[chave] = valor
- Método .items() para percorrer chave e valor ao mesmo tempo
- Operador in para verificar se um ID existe (verifica as chaves)
- del para remover uma entrada do dicionário
- Conversão de tipos com int(), porque o input devolve sempre texto
- Loop while e condicionais if-elif-else para o menu

## O que aprendi
Esta versão fez-me sentir, na prática, porque é que os dicionários
existem. Com IDs únicos, deixou de haver ambiguidade entre tarefas com
o mesmo nome, algo impossível de resolver bem com listas.

Também percebi a importância de onde se declaram as variáveis: ter o
dicionário e o contador de ID dentro do loop fazia com que fossem
reiniciados a cada volta, apagando tudo. A solução foi declará-los antes
do loop, para que sobrevivam entre as iterações.

Outra aprendizagem foi a conversão de tipos: como o input devolve sempre
texto, e as chaves do dicionário são números, foi preciso usar int()
para que a comparação de IDs funcionasse.

## Limitações conhecidas
- O programa rebenta se o utilizador escrever algo que não seja um
  número quando é pedido um ID, porque o int() não consegue converter
  texto não numérico. A solução correta é tratamento de exceções
  (try/except), conceito que ainda vou aprender. Está marcado no código
  com um comentário TODO.
- Os dados são guardados apenas em memória RAM, por isso desaparecem
  quando o programa fecha. O passo seguinte seria adicionar persistência
  (guardar em ficheiro).