class Candidato:
    def __init__(self, id, nome, cargo, numero, partido):
        self.id = id
        self.nome = nome
        self.cargo = cargo
        self.numero = numero
        self.partido = partido

    def print_caditado(self):
        print(self.nome + " (" + self.cargo + ") " + " Partido: " + self.partido + " Número: " + str(self.numero))
