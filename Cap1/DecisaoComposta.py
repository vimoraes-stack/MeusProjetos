nome = input("Digite o nome: ")
idade = int(input("Digite a idade: "))
doenca_infectocontagiosa = input(" Suspeita de doença infectocontagiosa? ").upper()
if idade >= 65 and doenca_infectocontagiosa == "SIM":
    print("O paciente " + nome + " será direcionado para sala AMARELA - COM PRIORIDADE")
elif idade < 65 and doenca_infectocontagiosa == "SIM":
    print("O paciente "+nome+" será direcionado para sala AMARELA - SEM PRIORIDADE")
elif idade >= 65 and doenca_infectocontagiosa == "NAO":
    print("O paciente " + nome + " será direcionado para sala BRANCA - COM PRIORIDADE")
elif idade < 65 and doenca_infectocontagiosa == "NAO":
    print("O paciente "+nome+" será direcionado para sala BRANCA - SEM PRIORIDADE")
else:
    print("Responda a suspeita de doença infectocontagiosa com SIM ou NAO")
