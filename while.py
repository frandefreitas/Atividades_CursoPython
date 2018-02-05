#while é o enquanto
number = 5
while number<10:
	print(number)
	number += 1   #number implementa 1
	#quando chega no 10 vai para a linha 3 e cai fora antes do print

print ("-------------------")

number1 = 5
while number1<10:
	print(number1)
	number1 += 1  
	if number1 == 8:
		print ("break")
		break          #chegou no 8 ele pula fora, logo não chega de novo no while, tampouco o print

else:                 #else para quando a condição acabar, se der um break antes, como no exemplo, não pega a linha 19	
	print ("Not true anymore")