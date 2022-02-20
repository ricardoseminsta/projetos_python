from collections import UserDict, Counter, defaultdict, deque, namedtuple

class Pins(UserDict):
    def __contains__(self, key):
        return str(key) in self.keys()

    def __setitem__(self, key, value):
        self.data[str(key)] = value


if __name__ == "__main__":
    pins = Pins(one=1)
    print(pins)
    pins[3] = 1
    lista = [1, 2, 3]
    pins[lista] = 2
    print(pins)

    cores = [('1', 'azul'), ('2', 'amarelo'), ('3', 'vermelho'), ('1', 'branco'), ('3', 'verde')]
    cores_favoritas = defaultdict(list)

    for chave, valor in cores:
        cores_favoritas[chave].append(valor)

    print(cores_favoritas)

    coutercores = ['amarelo', 'azul', 'azul', 'vermelho', 'azul', 'verde', 'vermelho']
    contador = Counter(coutercores)
    print(contador)

    fila = deque()
    fila.append('1')
    fila.append('2')
    fila.append('3')
    print(fila)
    print(len(fila))
    fila.pop()
    print(fila)
    fila.append('3')
    print(fila)
    fila.popleft()
    print(fila)
    fila.appendleft('1')
    print(fila)

    Conta = namedtuple('Conta', 'numero titular saldo limita')
    conta = Conta('123-4', 'João', 1000, 1000)
    print(conta)
    print(conta.titular)
    print(conta[0])