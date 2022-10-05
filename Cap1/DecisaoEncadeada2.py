nome = input("Digite o nome: ")
idade = int(input("Digite a idade: "))
doenca_infectocontagiosa = input("Suspeita de doença infectocontagiosa ? ").upper()
if idade >= 65:
    print("Paciente COM PRIORIDADE")
    if doenca_infectocontagiosa == "SIM":
        print("Encaminhe" + nome + "para a sala AMARELA")
    elif doenca_infectocontagiosa == "NAO":
        print("Encaminhe" + nome + "para a sala BRANCA")
    else:
        print(" Responda a supeita de doença infectocontagiosa com SIM ou NAO")
if idade < 65:
    print("Paciente COM PRIORIDADE")
    if doenca_infectocontagiosa == "SIM":
        print("Encaminhe" + nome + "para a sala AMARELA")
    elif doenca_infectocontagiosa == "NAO":
        print("Encaminhe" + nome + "para a sala BRANCA")
    else:
        print(" Responda a supeita de doença infectocontagiosa com SIM ou NAO")
