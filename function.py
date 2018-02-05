def call_numbers():		#que nem no ruby ele abre com def, porém não fecha com end
	for number in range (0,10):
		print(number) 

def call_numbers_with_limit(limit):		
	list = range(0,10)
	for number in list[0: limit]:
		print(number)

def call_numbers_with_limit2(limit):		
	list = range(0,10)
	for number in range(0, limit):          #quando é range é (), poderia por também só (limit) que funcionaria
		print(number)



def calculator(x, y):
	print (x-y)

def calculator2(x=10, y=15):
	print (x-y)

def calculator3(x=10, y=15):
	print (x-y)

def nova_calculator(x=10, y=15):
	return (x-y)      #ele para a execução da função na hora de retorna o resultado que está na frente

#call_numbers()          #função que imprimir numeros de 0 a 9
#print ("----------------")
#call_numbers_with_limit(5)    #função que imprimir numero de 0 até o limit, sendo que o range é de 0 a 10, ou seja, não passa de 9
#print ("----------------")
#call_numbers_with_limit2(5)    #outra maneira de fazer a função homonima, porém nesse caso passa sim se o limit está maior 10, ignorado o fim do range
#print ("----------------")
#calculator(-5, 10)
#calculator(10, -5)
#calculator(y=20, x=8)
#calculator2()
#calculator3(5)               #nesse caso o 5 passa a ser o x no lugar do 10, enquanto o y permanece 15


result = nova_calculator(5)    #esta armazenando a função já com o valor de x passando a ser 5, invés de 10 calculada e pronta para a variavel
print("Result is", result)     #imprimindo a variavel com o resultado da função