import array
from candidato import Candidato
from urnaEletronica import UrnaEletronica

# Cadastra candidatos
presidentes = [
        Candidato(1, "Ednilson Messias", "Presidente", 99, "Pantera"),
        Candidato(2, "Renata Gomes", "Presidente", 88, "Gavião")
    ]

senadores = [
        Candidato(3, "Georgen", "Senador", 881, "Gavião"),
        Candidato(4, "Marco Antônio", "Senador", 882, "Gavião"),
        Candidato(5, "Nadilson Lima", "Senador", 991, "Pantera")
    ]

urna = UrnaEletronica([],[])


print("################################")
print("####### ELEIÇÕES ABERTAS #######")
print("################################\n")

print("0 - Iniciar uma sessão de votação")
print("1 - Encerrar as eleições\n")

#Inicia loop para Eleições
opcao = input("Digite a opção desejada:\n")
while opcao != "1":
    match opcao:
        case "0":
            print("*** PRESIDENTES ***")
            for presidente in presidentes:
                presidente.print_caditado()
            
            votoPresidente = int(input("Digite o número para PRESIDENTE:\n"))

            presidenteSelecionado = list(filter( lambda presidente: presidente.numero == votoPresidente, presidentes))

            while(len(presidenteSelecionado) == 0):
                print("\n")
                print("Candidato não cadastrado.")
                print("Selecione um novo candidato.")
                votoPresidente = int(input("Digite o número para PRESIDENTE:\n"))
                presidenteSelecionado = list(filter( lambda senador: senador.numero == votoPresidente, presidentes))
                print("\n")
            
            urna.votosPresidente.append(votoPresidente)            
            # TODO verificar se o número é um dos presidentes cadastrados, se não for pedir pra informar um número ou dar a opção de abortar (colocar em um while)

            print("*** SENADORES ***")
            for senador in senadores:
                senador.print_caditado()
            
            votoSenador = int(input("Digite o número para SENADOR:\n"))

            senadorSelecionado = list(filter( lambda obj: obj.numero == votoSenador, senadores))

            while(len(senadorSelecionado) == 0):
                print("\n")
                print("Candidato não cadastrado.")
                print("Selecione um novo candidato.")
                votoSenador = int(input("Digite o número para SENADOR:\n"))
                senadorSelecionado = list(filter( lambda obj: obj.numero == votoSenador, senadores))
                print("\n")

            urna.votosSenador.append(votoSenador)
            # TODO verificar se o número é um dos senadores cadastrados, se não for pedir pra informar um número ou dar a opção de abortar (colocar em um while)

            print("\n")
            print("################################")
            print("####### ELEIÇÕES ABERTAS #######")
            print("################################\n")

            print("0 - Iniciar uma sessão de votação")
            print("1 - Encerrar as eleições\n")
            opcao = input("Digite a opção desejada:\n")
        case "1":
            continue
        case _: 
            print("Opção invalida:\n")
            print("0 - Iniciar uma sessão de votação")
            print("1 - Encerrar as eleições\n")
            opcao = input("Digite a opção desejada:\n")


# TODO apresentar votos sumarizados como nome dos canditados e quantos votos receberam

print("\n")
print("################################")
print("##### ELEIÇÕES ENCERRADAS ######")
print("################################\n")

votosPresidenteSumarizado = {}
print("***** Votos para PRESIDENTE ***** ")

for voto in urna.votosPresidente:
    if voto in votosPresidenteSumarizado:
        votosPresidenteSumarizado[voto] = votosPresidenteSumarizado[voto] + 1
    else:
        votosPresidenteSumarizado[voto] = 1

for key, value in votosPresidenteSumarizado.items():
    for presidente in presidentes:
        if(presidente.numero == key):
            print(presidente.nome + ": " + str(value) + " votos")
print("\n")

votosSenadorSumarizado = {}
print("***** Votos para SENADOR*****")
for voto in urna.votosSenador:
    if voto in votosSenadorSumarizado:
        votosSenadorSumarizado[voto] = votosSenadorSumarizado[voto] + 1
    else:
        votosSenadorSumarizado[voto] = 1

for key, value in votosSenadorSumarizado.items():
    for senador in senadores:
        if(senador.numero == key):
            print(senador.nome + ": " + str(value) + " votos")        

print("\n")

