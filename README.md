🎟️ Sistema Inteligente de Atendimento com Filas em Python

## 📌 Descrição

Trabalho da disciplina de **Estrutura de Dados II** que simula uma **central de atendimento** em Python.

O programa usa **fila clássica (FIFO), fila circular e fila de prioridade** para mostrar como os mesmos clientes são atendidos em cada uma delas.

## 🎯 Objetivo

Comparar os três tipos de fila na prática: a ordem dos atendimentos, o reaproveitamento de espaço e o tratamento das prioridades.

Cada cliente tem nome, senha e prioridade: **1 = emergência, 2 = prioritário e 3 = atendimento normal**. Na fila de prioridade, quem chega primeiro tem preferência entre clientes do mesmo nível.

## 🛠️ Tecnologias utilizadas

- Python
- Google Colab

## ⚙️ Funcionalidades

- Implementação de fila clássica, circular e de prioridade
- Inserção, atendimento e consulta do próximo cliente
- Consulta do tamanho e verificação de fila vazia
- Demonstração do atendimento FIFO com 10 clientes
- Fila circular com capacidade para 5 clientes
- Visualização dos índices `front` e `rear` e reutilização de posições
- Tratamento de tentativas de inserção na fila circular cheia
- Uso de `heapq` para atendimento por prioridade
- Preservação da ordem de chegada nos empates de prioridade
- Geração automática de 20 clientes com prioridades entre 1 e 3
- Uso de `random.Random(42)` para reprodução da simulação
- Exibição das ordens de chegada e atendimento e comparação dos resultados
- Verificações automáticas com `assert` e tratamento de filas vazias

## 🧩 Estrutura do projeto

### 🔹 Fila clássica

Atende por ordem de chegada. O primeiro exemplo usa **10 clientes** para conferir essa sequência.

### 🔹 Fila circular

Guarda até **5 clientes** e reaproveita os espaços que ficam livres. A execução mostra os índices `front` e `rear` a cada inserção e remoção.

### 🔹 Fila de prioridade

Atende primeiro os clientes de prioridade 1, depois os de prioridade 2 e, por último, os de prioridade 3. Em caso de empate, vale a ordem de chegada.

### 🔹 Preparação da simulação

O desafio gera **20 clientes** e usa esse mesmo grupo nas três filas. Como a circular só comporta cinco pessoas, o programa atende um cliente sempre que precisa abrir espaço para o próximo.

### 🔹 Análise dos resultados

A saída permite comparar quem chegou primeiro e quem foi atendido primeiro em cada fila. As respostas às quatro perguntas da atividade estão no final deste arquivo.

## 📚 Aprendizados

- Implementação de estruturas de fila em Python
- Aplicação do princípio FIFO
- Controle de índices circulares com o operador módulo
- Reutilização de posições em estruturas de capacidade fixa
- Uso de heap para organizar prioridades
- Preservação da ordem de chegada em empates
- Tratamento de filas cheias e vazias
- Uso de sementes fixas em simulações reproduzíveis
- Validação automática das ordens de atendimento
- Comparação de estruturas de dados aplicadas ao mesmo problema

## 🔍 Explicação das Implementações

### Fila clássica

A classe `Fila` usa `deque`, com inserção no fim e remoção no início. Oferece `enqueue`, `dequeue`, `head`, `size` e `empty`. A demonstração cadastra 10 clientes e verifica atendimento na ordem de chegada.

### Fila circular

A classe `FilaCircular` usa uma lista de cinco posições. `front` aponta para o próximo cliente a sair e `rear` para a próxima posição de entrada. O operador `%` faz o índice voltar ao início quando chega ao fim da lista. A quantidade de clientes permite distinguir fila cheia de fila vazia, já que nos dois casos pode ocorrer `front == rear`.

A demonstração preenche as cinco posições, tenta inserir na fila cheia, remove os dois primeiros clientes e insere outros dois. As posições 0 e 1 são reutilizadas: o vetor fica com as senhas `[6, 7, 3, 4, 5]`, mas a ordem de atendimento continua `3, 4, 5, 6, 7`.

### Fila de prioridade

A classe `FilaPrioridade` guarda tuplas `(prioridade, contador, cliente)` em um heap do módulo `heapq`. A prioridade define quem sai primeiro; o contador desempata pela chegada. No exemplo, Bruno e Diego têm prioridade 1, mas Bruno chegou antes. Por isso, a sequência é Bruno, Diego, Carla e Ana.

## 🧪 Desafio Final e Comparação

São gerados automaticamente 20 clientes com prioridades entre 1 e 3. A semente 42 permite reproduzir os resultados. Os mesmos clientes são usados nas três estruturas.

| Estrutura | Ordem de atendimento | Organização |
| --- | --- | --- |
| Clássica | Ordem de chegada | Armazena os 20 clientes antes de atender |
| Circular | Ordem de chegada | Capacidade 5; intercala atendimento e inserção |
| Prioridade | Prioridade 1, depois 2, depois 3; chegada nos empates | Armazena os 20 clientes antes de atender |

A clássica e a circular atendem os 20 clientes na mesma ordem. A diferença é que a circular precisa liberar espaço durante a entrada dos clientes. Já a fila de prioridade altera a sequência para atender os casos mais urgentes primeiro. Todos os clientes são atendidos. O programa compara essas sequências, sem medir tempo de execução.

## ✅ Evidências dos Testes

A saída completa está em [evidencias.txt](evidencias.txt), incluindo a chegada dos clientes, as três ordens de atendimento e os índices `front` e `rear` durante a execução circular.

O programa verifica automaticamente:

- Atendimento FIFO dos 10 clientes iniciais.
- Recusa de inserção na circular cheia sem alterar seu conteúdo.
- Reutilização das posições 0 e 1 da circular, mantendo FIFO.
- Prioridades e desempate por chegada (Bruno antes de Diego).
- Atendimento dos 20 clientes nas três estruturas, sem perdas na circular.
- Erro ao remover ou consultar o próximo cliente de filas vazias.

Se todas as verificações passarem, a última linha será `Testes concluídos sem erros.`

## 📝 Respostas do Relatório

### 1. Por que a ordem da fila de prioridade pode ser diferente da clássica?

Porque a clássica atende quem chegou primeiro, enquanto a de prioridade atende primeiro quem tem maior urgência. Assim, alguém com prioridade 1 pode chegar depois de alguém com prioridade 3 e ser atendido antes. Entre clientes de mesma prioridade, continua valendo a chegada.

### 2. Em quais situações reais uma fila de prioridade seria mais adequada?

Em situações em que alguns casos não podem esperar tanto quanto outros, como atendimento hospitalar por gravidade, chamados de suporte com falhas críticas e processamento de tarefas urgentes.

### 3. Quais são as vantagens e limitações de uma fila circular?

Ela reaproveita as posições livres e não precisa deslocar os outros elementos a cada atendimento. Também mantém um espaço fixo de armazenamento. Por outro lado, só aceita a quantidade de clientes definida na criação e exige cuidado com os índices. Quando fica cheia, é preciso liberar espaço antes de inserir outro cliente.

### 4. O que acontece ao inserir em uma fila circular cheia?

Neste código, a inserção é recusada com `OverflowError`. Os clientes que já estavam na fila permanecem nela. O teste mostra essa mensagem; no desafio com 20 clientes, o programa atende uma pessoa antes de inserir a próxima quando a fila está cheia.
