equipamentos = []
valores = []
resposta = "S"

while resposta == "S":
    equipamentos.append(input("Equipamento: "))
    valores.append(int(input("Valor: ")))
    resposta = input("Digite S para continuar: ").upper()

depreciacao = input("Digite o nome do equipamento que será depreciado: ")
for indice in range(0, len(equipamentos)):
    if depreciacao == equipamentos[indice]:
        print("Valor antigo: ", valores[indice])
        valores[indice] = valores[indice] * 0.9
        print("Valor atual: ", valores[indice])
