# 🎟️ Sistema Inteligente de Atendimento com Filas em Python

## 📌 Descrição

Projeto acadêmico desenvolvido na disciplina de **Estrutura de Dados II**, utilizando Python para implementar e analisar estruturas de fila aplicadas ao contexto de uma **Central de Atendimento**.

O projeto compara **fila clássica (FIFO), fila circular e fila de prioridade**, observando como a ordem de chegada, a capacidade de armazenamento e o nível de prioridade influenciam a organização e o atendimento dos clientes.

## 🎯 Objetivo

Aplicar conceitos de estruturas de dados por meio da implementação prática de três tipos de fila, comparando seu comportamento em uma simulação de atendimento.

Também é objetivo demonstrar a reutilização de posições na fila circular e preservar a ordem de chegada entre clientes com a mesma prioridade. Cada cliente possui nome, senha e prioridade: **1 = emergência, 2 = prioritário e 3 = atendimento normal**.

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

A classe `Fila` utiliza `deque` para aplicar o princípio **FIFO**, em que o primeiro cliente a chegar é o primeiro a ser atendido. A demonstração inicial utiliza **10 clientes** e verifica a preservação da ordem de chegada.

### 🔹 Fila circular

A classe `FilaCircular` utiliza uma lista com capacidade para **5 clientes**. Os índices `front` e `rear` avançam de forma circular, permitindo reutilizar posições liberadas após os atendimentos.

### 🔹 Fila de prioridade

A classe `FilaPrioridade` utiliza o módulo `heapq` com a estrutura `(prioridade, contador, cliente)`. Os menores valores de prioridade são atendidos primeiro, enquanto o contador mantém a ordem de chegada nos empates.

### 🔹 Preparação da simulação

São gerados automaticamente **20 clientes**, utilizando uma semente fixa. Os mesmos clientes são utilizados nas três estruturas. Na circular, inserções e atendimentos são intercalados para respeitar a capacidade de cinco posições.

### 🔹 Análise dos resultados

O programa apresenta a ordem de chegada, as ordens de atendimento e o estado da fila circular. Os resultados são comparados e as quatro questões do relatório são respondidas neste README.

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

A classe `FilaCircular` utiliza uma lista de capacidade fixa igual a 5. `front` indica a próxima remoção e `rear` a próxima inserção. Os índices avançam com módulo da capacidade. Um contador distingue os estados cheio e vazio, pois ambos podem apresentar `front == rear`.

A demonstração preenche as cinco posições, tenta inserir na fila cheia, remove os dois primeiros clientes e insere outros dois. As posições 0 e 1 são reutilizadas: o vetor fica com as senhas `[6, 7, 3, 4, 5]`, mas a ordem de atendimento continua `3, 4, 5, 6, 7`.

### Fila de prioridade

A classe `FilaPrioridade` usa `heapq` com tuplas `(prioridade, contador, cliente)`. A menor prioridade numérica sai primeiro. O contador crescente preserva a ordem de chegada nos empates. Na demonstração, a saída esperada é Bruno, Diego, Carla e Ana.

## 🧪 Desafio Final e Comparação

São gerados automaticamente 20 clientes com prioridades entre 1 e 3. A semente 42 permite reproduzir os resultados. Os mesmos clientes são usados nas três estruturas.

| Estrutura | Ordem de atendimento | Organização |
| --- | --- | --- |
| Clássica | Ordem de chegada | Armazena os 20 clientes antes de atender |
| Circular | Ordem de chegada | Capacidade 5; intercala atendimento e inserção |
| Prioridade | Prioridade 1, depois 2, depois 3; chegada nos empates | Armazena os 20 clientes antes de atender |

A fila circular mantém a mesma sequência FIFO da clássica, utilizando apenas cinco posições. No desafio, quando está cheia, o programa atende um cliente antes de inserir o próximo. Nenhum cliente é descartado. A fila de prioridade muda a sequência conforme a urgência. A comparação é de ordem e comportamento; não é uma medição de desempenho.

## ✅ Evidências dos Testes

A saída completa está em [evidencias.txt](evidencias.txt), incluindo a chegada dos clientes, as três ordens de atendimento e os índices `front` e `rear` durante a execução circular.

O programa verifica automaticamente:

- Atendimento FIFO dos 10 clientes iniciais.
- Recusa de inserção na circular cheia sem alterar seu conteúdo.
- Reutilização das posições 0 e 1 da circular, mantendo FIFO.
- Prioridades e desempate por chegada (Bruno antes de Diego).
- Atendimento dos 20 clientes nas três estruturas, sem perdas na circular.
- Erro ao remover ou consultar o próximo cliente de filas vazias.

A execução bem-sucedida termina com `PASSOU: todos os testes, inclusive fila vazia e ausencia de perdas.`

## 📝 Respostas do Relatório

### 1. Por que a ordem da fila de prioridade pode ser diferente da clássica?

A fila clássica considera apenas a ordem de chegada. A de prioridade considera primeiro o nível de urgência: um cliente de prioridade 1 pode chegar depois de um cliente de prioridade 3 e ser atendido antes. A chegada só desempata clientes da mesma prioridade.

### 2. Em quais situações reais uma fila de prioridade seria mais adequada?

Em triagem de emergência hospitalar, atendimento de incidentes críticos de sistemas e processamento de tarefas urgentes. Nessas situações, a urgência ou importância deve influenciar a ordem de atendimento.

### 3. Quais são as vantagens e limitações de uma fila circular?

As vantagens são reutilizar posições liberadas, manter uso de memória limitado e inserir/remover sem deslocar todos os elementos. As limitações são a capacidade fixa, a necessidade de tratar a fila cheia e o controle cuidadoso dos índices e da quantidade. Ela mantém FIFO, sem dar preferência a emergências.

### 4. O que acontece ao inserir em uma fila circular cheia?

Nesta implementação, a operação lança `OverflowError` e recusa a inserção, preservando os clientes existentes. A demonstração captura e apresenta esse erro. No desafio final, o programa evita a tentativa inválida atendendo um cliente antes de inserir outro. Sobrescrever clientes não é o comportamento adotado.
