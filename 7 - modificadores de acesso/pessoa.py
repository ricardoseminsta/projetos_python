class Pessoa:
    def __init__(self, idade):
        self._idade = idade


pessoa = Pessoa(20)
print(dir(pessoa))
pessoa._idade = 25
print(pessoa._idade)

#pessoa._Pessoa__idade = 25
#print(pessoa._Pessoa__idade)
