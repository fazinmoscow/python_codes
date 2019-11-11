info='\nOperations\n1:Sum\n2:Difference\n3:Multiplication\n4:Division'
print(info)
while 1==1:
	a=input('\nChoose an operation:')
	if a=='1' or a=='Sum':
		b=int(input('\nAddition\nEnter first number:'))
		c=int(input('Enter second number:'))
		print(f'\nAnswer={b+c}')
	if a=='2':
		b=int(input('\nSubtraction\nEnter first number:'))
		c=int(input('Enter second number:'))
		print(f'\nAnswer={b-c}')
	if a=='3':
		b=int(input('\nMultiplication\nEnter Multiplicand:'))
		c=int(input('Enter Multiplier:'))
		print(f'\nAnswer={b*c}')
	if a=='4':
		b=int(input('\nDivision\nEnter Dividend:'))
		c=int(input('Enter Divisor:'))
		print(f'\nQuotient={int(b/c)}\nRemainder={b%c}\nFloat{b/c}')
	if a=='exit':
		break
	else:
		print(info)
