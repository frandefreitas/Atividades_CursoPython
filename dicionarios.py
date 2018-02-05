cars = {}   #dicionarios são tipo o array associativo do php
cars['Corola'] = "red"
cars['Fit'] = "green"
cars['320'] = "black"

#se digitar -> cars.keys()
#sai -> dict_keys(['Corola', 'Fit', '320', 'Renault', 'C-3'])

#se digitar -> cars.values()
#sai -> dict_values(['red', 'green', 'black', 'yellow', 'orange'])

#se digitar -> cars2['Renault'] = "yellow"
#vai incrementar no array cars2 o carro Renault onde o value é "yellow"

#>>> cars['Corola']
#'red'



#outra forma de criar estrutura de dicionário
#>>> people = dict(Marcelo='Pé', Francisco='Nariz', Lucas='Hinz')
#>>> people
#{'Marcelo': 'Pé', 'Francisco': 'Nariz', 'Lucas': 'Hinz'}



#>>> é eu falando    ... extensão para falar mais (não esquecer de identações)    e sem nada já é o feedback
#>>> if 'Marcelo' in people:
#...     print(people['Marcelo'])            
#...
#Pé


#>>> family= {                   #igual na hora de fazer o array e dois pontos depois
#... 'Set':'Family'
#... }


#dicionario é uma estrutura de chaves de valor 

for car in cars:
	print (car)
	print ("-----------")
	print (car + " = " + cars[car])                #o carro = valor contido nele, no caso a cor, mas é gambiarra
#vai no console normal, não no python e testa
#C:\Users\Francisco\Downloads\TSI\School of Net\Python>python.exe dicionarios.py
#Corola
#Fit
#320


print ("-----------")
print ("-----------")



for key, value in cars.items():   #resultado de uma maneira mais elegante onde retira key dos carros e value do conteudo que tem nos carros
	print (key + " = " + value)   #e o items que envia a key e value para o print





















