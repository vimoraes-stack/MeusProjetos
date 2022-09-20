nome = input("Digite o nome: ")
idade = int(input("Digite a idade: "))
doenca_infectocontagiosa = input("Suspeita de doença infectocontagiosa? ").upper()

##Definindo o isolamento (problema 1)

while doenca_infectocontagiosa != "SIM" and doenca_infectocontagiosa != "NAO":
    print("Digite SIM ou NAO")
    doenca_infectocontagiosa = input("Suspeita de doença infectocontagiosa? ").upper()

if doenca_infectocontagiosa == "SIM":
    print("Encaminhe" + nome + " para a sala AMARELA")
else:
    doenca_infectocontagiosa == "NAO"
    print("Encaminhe" + nome + " para a sala BRANCA")

# definindo segunda situaçao de prioridade

if idade >= 65:
    print("Paciente com PRIORIDADE")
else:
    genero = input("Qual o genero do paciente ? ").upper()
    if genero == "FEMININO" and idade > 10:
        gravidez = input("A " + nome + " está gravida? ").upper()
        if gravidez == "SIM":
            print("paciente COM PRIORIDADE")
        else:
            print("Paciente SEM PRIORIDADE")
    else:
        print("Paciente SEM PRIORIDADE")
