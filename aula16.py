class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print(f'O meu nome é {self.nome} e tenho {self.idade} anos')

class Funcionario(Pessoa):
    def __init__(self, nome, idade,cargo):
       super().__init__(nome, idade)
       self.cargo = cargo

    def trabalhar(self):
        print(f'{self.nome} está trabalhando como {self.cargo}.')

class Cliente(Pessoa):
    pass

f1 = Funcionario('Maria', 38, 'Gerente de Contas')
f1.trabalhar()


c1 = Cliente('Arthur', 16)
c1.apresentar()


