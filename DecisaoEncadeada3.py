nome = input("Digite o nome: ")
idade = int(input("Digite a idade: "))
doenca_infectocontagiosa = input("Suspeita de doença infectocontagiosa? ").upper()

#Definindo o isolamento (problema 1)

if doenca_infectocontagiosa == "SIM":
    print("Encaminhe" + nome + "para a sala AMARELA")
elif doenca_infectocontagiosa == "NAO":
    print("Encaminhe" + nome + "para a sala BRANCA")
else:
    print("Responda suspeita de doença infectocontagiosa com SIM ou NAO")

# definindo segunda situaçao de prioridade

if idade >= 65:
    print("Paciente com PRIORIDADE")
else:
    genero = input("Qual o genrero do paciente ? ").upper()
    is genero == "FEMININO" and idade > 10:
        gravidez = input("A " + nome + "está gravida? ").upper()
        if gravidez == "SIM"
            print ("paciente COM PRIORIDADE")
        else:
            print("Paciente SEM PRIORIDADE")
    else:
        print("Paciente SEM PRIORIDADE")