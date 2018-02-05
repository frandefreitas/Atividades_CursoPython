list = [2, 4, 6, 8, 10]

for item in list:         #a cada item que vai percorrer na list
	print (item)          #concatenar sempre string com string

for item in list[0:3]:    #percorre de 0 a 2 na list
	if item > 3:   		  #se o conteudo dos indices listados for maior que 3
		print ("grater than 2")          
	



list2 = ["Marcos", "Manuel"]
for name in list2:
	print (name)


list3 = ["Marco", "Mateus"]
for name1 in list3:
	if name1=="Marco":    #sempre dois pontos ao abrir algum laço, se tiver indice com Marco
		print (name1)

list4 = ["Lucas", "Francisco"]
for name2 in list4:		  
	if not name2=="Francisco": #if not é como o !=   
		print (name2)