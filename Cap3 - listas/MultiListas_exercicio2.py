equipamentos = []
valores = []
resposta = "S"

while resposta == "S":
    equipamentos.append(input("Equipamento: "))
    valores.append(int(input("Valor: ")))
    resposta = input("Digite S para continuar: ").upper()

delete = input("Digite o nome do equipamento que será deletado: ")
for indice in range(0, len(equipamentos)):
    if delete == equipamentos[indice]:
        del (equipamentos[indice])
        del (valores[indice])
        break

print("Feito")

for indice in range(0, len(equipamentos)):
   print("nome.........:", equipamentos[indice])
   print("valor........:", valores[indice])
   print("")
   (indice+1)

