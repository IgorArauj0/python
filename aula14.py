class Pessoa:
    def __init__(self, nome, idade, cargo):
        self.nome = nome
        self.idade = idade
        self.cargo = cargo

    def informacoes(self):
        print(f'Nome: {self.nome}')
        print(f'Idade: {self.idade}')
        print(f'Cargo: {self.cargo}')

    def promover(self, novo_cargo):
        self.cargo = novo_cargo
        print(f'{self.nome} foi promovido(a) para {novo_cargo}.')

    def atualizar_idade(self, nova_idade):
        if nova_idade > self.idade:
           print(f'Atualizando a idade de {self.idade} para {nova_idade}')
        else: {
            print('A nova idade tem que ser maior que a antiga')
        }
        


colaborador1 = Pessoa('Ana', 19, 'Assistente Junior')
colaborador2 = Pessoa('Fernando', 73, 'Assistente Sênior')

colaborador1.informacoes()
colaborador1.promover('Assistente Pleno')
colaborador1.atualizar_idade(18)
     
    