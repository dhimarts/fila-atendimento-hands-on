from collections import deque
from dataclasses import dataclass
import heapq
import random


@dataclass
class Cliente:
    nome: str
    senha: int
    prioridade: int

    def __str__(self):
        return f'{self.nome} (senha={self.senha}, prioridade={self.prioridade})'


class Fila:
    """Atende os clientes na ordem de chegada."""

    def __init__(self):
        self.dados = deque()

    def enqueue(self, cliente):
        self.dados.append(cliente)

    def dequeue(self):
        if self.empty():
            raise IndexError('Fila vazia')
        return self.dados.popleft()

    def head(self):
        if self.empty():
            raise IndexError('Fila vazia')
        return self.dados[0]

    def size(self):
        return len(self.dados)

    def empty(self):
        return self.size() == 0


class FilaCircular:
    """front indica a próxima saída; rear indica a próxima entrada."""

    def __init__(self, capacidade=5):
        if capacidade <= 0:
            raise ValueError('Capacidade deve ser positiva')
        self.capacidade = capacidade
        self.dados = [None] * capacidade
        self.front = 0
        self.rear = 0
        self.quantidade = 0

    def size(self):
        return self.quantidade

    def empty(self):
        return self.quantidade == 0

    def full(self):
        return self.quantidade == self.capacidade

    def enqueue(self, cliente):
        if self.full():
            raise OverflowError('Fila circular cheia: não há espaço para outro cliente')
        self.dados[self.rear] = cliente
        self.rear = (self.rear + 1) % self.capacidade
        self.quantidade += 1

    def dequeue(self):
        if self.empty():
            raise IndexError('Fila circular vazia')
        cliente = self.dados[self.front]
        self.dados[self.front] = None
        self.front = (self.front + 1) % self.capacidade
        self.quantidade -= 1
        return cliente

    def head(self):
        if self.empty():
            raise IndexError('Fila circular vazia')
        return self.dados[self.front]

    def estado(self):
        posicoes = [c.senha if c else None for c in self.dados]
        return f'front={self.front}, rear={self.rear}, tamanho={self.size()}, posicoes={posicoes}'


class FilaPrioridade:
    def __init__(self):
        self.dados = []
        self.contador = 0

    def enqueue(self, cliente):
        heapq.heappush(self.dados, (cliente.prioridade, self.contador, cliente))
        self.contador += 1

    def dequeue(self):
        if self.empty():
            raise IndexError('Fila de prioridade vazia')
        return heapq.heappop(self.dados)[2]

    def head(self):
        if self.empty():
            raise IndexError('Fila de prioridade vazia')
        return self.dados[0][2]

    def size(self):
        return len(self.dados)

    def empty(self):
        return self.size() == 0


def esvaziar(fila):
    atendidos = []
    while not fila.empty():
        atendidos.append(fila.dequeue())
    return atendidos


def mostrar(titulo, clientes):
    print('\n' + titulo)
    for cliente in clientes:
        print(cliente)


def main():
    print('1. Fila clássica - 10 clientes')
    clientes10 = [Cliente(f'Cliente {i:02d}', i, 3) for i in range(1, 11)]
    fila = Fila()
    for cliente in clientes10:
        fila.enqueue(cliente)
    print('Tamanho:', fila.size(), '| Próximo:', fila.head())
    resultado10 = esvaziar(fila)
    mostrar('Ordem de atendimento FIFO:', resultado10)
    assert resultado10 == clientes10 and fila.empty()
    print('Os 10 clientes foram atendidos na ordem de chegada.')

    print('\n2. Fila circular - capacidade de 5 clientes')
    circular = FilaCircular(5)
    for cliente in clientes10[:5]:
        circular.enqueue(cliente)
        print('Inseriu', cliente.senha, '|', circular.estado())
    estado_cheio = circular.estado()
    try:
        circular.enqueue(clientes10[5])
    except OverflowError as erro:
        print('Tentativa de inserir o sexto cliente:', erro)
    else:
        raise AssertionError('A fila cheia deveria recusar a inserção')
    assert circular.estado() == estado_cheio
    for _ in range(2):
        print('Atendeu', circular.dequeue().senha, '|', circular.estado())
    for cliente in clientes10[5:7]:
        circular.enqueue(cliente)
        print('Inseriu', cliente.senha, '|', circular.estado())
    assert [c.senha for c in circular.dados] == [6, 7, 3, 4, 5]
    assert [c.senha for c in esvaziar(circular)] == [3, 4, 5, 6, 7]
    print('As posições 0 e 1 foram reutilizadas. Atendimento: 3, 4, 5, 6, 7.')

    print('\n3. Fila de prioridade - desempate por chegada')
    exemplo = [Cliente('Ana', 1, 3), Cliente('Bruno', 2, 1),
               Cliente('Carla', 3, 2), Cliente('Diego', 4, 1)]
    prioridade = FilaPrioridade()
    for cliente in exemplo:
        prioridade.enqueue(cliente)
    ordem = esvaziar(prioridade)
    mostrar('Atendimento por prioridade:', ordem)
    assert [c.nome for c in ordem] == ['Bruno', 'Diego', 'Carla', 'Ana']
    print('Bruno e Diego têm prioridade 1. Bruno foi atendido antes porque chegou primeiro.')

    print('\nDesafio final - 20 clientes nas três filas')
    gerador = random.Random(42)
    clientes = [Cliente(f'Cliente {i:02d}', i, gerador.randint(1, 3))
                for i in range(1, 21)]
    mostrar('Ordem de chegada:', clientes)
    fifo = Fila()
    prioridade = FilaPrioridade()
    for cliente in clientes:
        fifo.enqueue(cliente)
        prioridade.enqueue(cliente)
    ordem_fifo = esvaziar(fifo)
    ordem_prioridade = esvaziar(prioridade)
    mostrar('Ordem de atendimento - clássica:', ordem_fifo)

    print('\nFila circular: quando está cheia, atende um cliente antes de inserir o próximo.')
    circular = FilaCircular(5)
    ordem_circular = []
    for cliente in clientes:
        if circular.full():
            atendido = circular.dequeue()
            ordem_circular.append(atendido)
            print('Atendeu', atendido.senha, '|', circular.estado())
        circular.enqueue(cliente)
        print('Inseriu', cliente.senha, '|', circular.estado())
    while not circular.empty():
        atendido = circular.dequeue()
        ordem_circular.append(atendido)
        print('Atendeu', atendido.senha, '|', circular.estado())
    mostrar('Ordem de atendimento - circular:', ordem_circular)
    mostrar('Ordem de atendimento - prioridade:', ordem_prioridade)

    assert ordem_fifo == clientes
    assert ordem_circular == clientes
    assert ordem_prioridade == sorted(clientes, key=lambda c: c.prioridade)
    assert len({c.senha for c in ordem_circular}) == 20
    for classe in (Fila, FilaCircular, FilaPrioridade):
        vazia = classe()
        for operacao in (vazia.dequeue, vazia.head):
            try:
                operacao()
            except IndexError:
                pass
            else:
                raise AssertionError('A operação em fila vazia deveria falhar')
    print('\nComparação dos resultados')
    print('Clássica: atendeu os 20 clientes na ordem de chegada.')
    print('Circular: manteve a mesma ordem, reutilizando as 5 posições.')
    print('Prioridade: atendeu os níveis 1, 2 e 3, nessa ordem, respeitando a chegada nos empates.')
    print('A clássica e a de prioridade receberam todos os clientes antes de atender.')
    print('Na circular, foi preciso intercalar entradas e atendimentos para liberar espaço.')
    print('Testes concluídos sem erros.')


def clientes_em_ordem(fila):
    """Consulta sem remover clientes da fila."""
    if isinstance(fila, FilaCircular):
        return [fila.dados[(fila.front + i) % fila.capacidade]
                for i in range(fila.size())]
    if isinstance(fila, FilaPrioridade):
        return [item[2] for item in sorted(fila.dados)]
    return list(fila.dados)


def menu():
    filas = {'1': Fila(), '2': FilaCircular(5), '3': FilaPrioridade()}
    nomes = {'1': 'Clássica', '2': 'Circular', '3': 'Prioridade'}
    escolha = '1'
    proxima_senha = 1
    print('\nMenu de atendimento')
    print('Cada fila mantém seus próprios clientes. As senhas são geradas automaticamente.')
    while True:
        fila = filas[escolha]
        print(f'\nFila selecionada: {nomes[escolha]}')
        print('1 - Inserir cliente')
        print('2 - Atender próximo cliente')
        print('3 - Consultar a fila')
        print('4 - Visualizar o estado do sistema')
        print('5 - Trocar de fila')
        print('0 - Sair')
        try:
            opcao = input('Opção: ').strip()
            if opcao == '0':
                print('Atendimento encerrado.')
                return filas
            if opcao == '1':
                if isinstance(fila, FilaCircular) and fila.full():
                    print('Fila circular cheia. Atenda um cliente antes de inserir outro.')
                    continue
                nome = input('Nome: ').strip()
                if not nome:
                    print('Informe um nome para o cliente.')
                    continue
                valor = input('Prioridade (1 = emergência, 2 = prioritário, 3 = normal): ').strip()
                if valor not in ('1', '2', '3'):
                    print('Prioridade inválida. Use 1, 2 ou 3.')
                    continue
                cliente = Cliente(nome, proxima_senha, int(valor))
                fila.enqueue(cliente)
                proxima_senha += 1
                print('Cliente inserido:', cliente)
            elif opcao == '2':
                if fila.empty():
                    print('Não há clientes para atender nesta fila.')
                else:
                    print('Cliente atendido:', fila.dequeue())
            elif opcao == '3':
                if fila.empty():
                    print('A fila está vazia.')
                else:
                    print('Próximo cliente:', fila.head())
                    mostrar('Clientes na ordem de atendimento:', clientes_em_ordem(fila))
            elif opcao == '4':
                for chave, atual in filas.items():
                    print(f'{nomes[chave]}: {atual.size()} cliente(s) aguardando')
                    if not atual.empty():
                        print('Próximo:', atual.head())
                    if isinstance(atual, FilaCircular):
                        print(atual.estado())
                        print('Cheia:', 'sim' if atual.full() else 'não')
            elif opcao == '5':
                nova = input('Escolha a fila (1 = clássica, 2 = circular, 3 = prioridade): ').strip()
                if nova in filas:
                    escolha = nova
                else:
                    print('Fila inválida. Use 1, 2 ou 3.')
            else:
                print('Opção inválida. Escolha uma das opções do menu.')
        except (EOFError, KeyboardInterrupt):
            print('\nAtendimento encerrado.')
            return filas


if __name__ == '__main__':
    main()
    menu()
