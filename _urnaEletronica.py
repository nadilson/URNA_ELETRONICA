# URNA ELETRONICA

# Ednilson Messias - Presidente - 99 - Pantera
# Renata Gomes - Presidente - 88 - Gavião
# Georgen - Senador - 881 - Pantera
# Marco Antônio - Senador - 882 - Pantera
# Nadilson Lima - Senador - 991 - Gavião


#Inicializa a urna com a lista de candidatos
class UrnaEletronica:
    def _init_(self):
        self.candidatos = {}
        self.votos = {}

    def adicionar_candidato(self, numero, nome):
        self.candidatos[numero] = nome
        self.votos[numero] = 0

    def votar(self, numero):
        if numero in self.candidatos:
            self.votos[numero] += 1
            print("Votado com sucesso!! ")
        else:
            print("Canditato não encontrado! ")

    def exibir_result(self):
        print("Resultado da Eleição 2023 ")

        for numero, nome in self.candidatos.items():
            tot_votos = self.votos[numero]
            print(f"{numero}: {nome} - {tot_votos} votos" )


#testando pra ver se vai
urna = UrnaEletronica()
urna.adicionar_candidato(1,"Candidato 1")
urna.adicionar_candidato(2,"Candidato 2")
urna.adicionar_candidato(3,"Candidato 3")
