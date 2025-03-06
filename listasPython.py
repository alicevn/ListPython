equipamentos = []
valores = []
seriais = []
departamentos = []
resposta = "S"
while resposta == "S":
  equipamentos.append(input("Equipamento: "))
  valores.append(float(input("Valor: ")))
  seriais.append(int(input("Número Serial: ")))
  departamentos.append(input("Departamento: "))
  resposta = input("Digite S para continuar ou MOSTRAR para ver a lista ou BUSCAR para buscar um item: ").upper()

if resposta == "MOSTRAR":
    for indice in range(0,len(equipamentos)):
        print("Equipamento..: ", (indice+1))
        print("Nome.........: ", equipamentos[indice])
        print("Valor........: ", valores[indice])
        print("Serial.......: ", seriais[indice])
        print("Departamento.: ", departamentos[indice])

elif resposta == "BUSCAR":
    busca=input("Digite o nome do equipamento que deseja buscar: ")
    encontrado = False
    for indice in range(0,len(equipamentos)):
        if busca==equipamentos[indice]:
            print("Equipamento: ", equipamentos[indice])
            print("Valor..: ", valores[indice])
            print("Serial.:", seriais[indice])
            encontrado = True
    if encontrado == False:
        print("Esse equipamento não está na lista!")