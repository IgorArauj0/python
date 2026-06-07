class Animal:
    def __init__(self, nome, cor, especie):
        self.nome = nome
        self.cor = cor
        self.especie = especie

    def apresentar(self):
        print(f'Eu sou o {self.especie} chamado {self.nome}')


class Gato(Animal):
    def emitir_som(self):
        print('Miau!')

class Cachorro(Animal):
    def emitir_som(self):
        print('Au Au Au...!')

class Elefante(Animal):
      def emitir_som(self):
        print('Bru Bru Bru...!')

gato1 = Gato('Felix', 'Branco', 'Siamese')
gato1.apresentar()
gato1.emitir_som()
    
cachorro1 = Cachorro('Russo', 'Preto', 'Pastor Alemão')
cachorro1.apresentar()
cachorro1.emitir_som()

elefante1 = Elefante('Cesar', 'Cinza', 'Asiático Elephant')
elefante1.apresentar()
elefante1.emitir_som()