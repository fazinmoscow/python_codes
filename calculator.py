def sum(a,b):
	return(a+b)

def sub(a,b):
	return(a-b)

def mul(a,b):
	return(a*b)

def div(a,b):
	return(a/b)

info='\nOperations:- 1:Sum 2:Difference 3:Multiplication 4:Division 5:Exit'

print(info)

while 1==1:

	a=input('\nChoose an operation:')

	if a=='1' or a=='Sum':
		b=float(input('\nAddition\nEnter first number:'))
		c=float(input('Enter second number:'))
		print(f'\nAnswer={sum(b,c)}')
		continue

	if a=='2' or a=='Difference':
		b=float(input('\nAddition\nEnter first number:'))
		c=float(input('Enter second number:'))
		print(f'\nAnswer={sub(b,c)}')
		continue

	if a=='3' or a=='Multiplication':
		b=float(input('\nMultiplication\nEnter Multiplicand:'))
		c=float(input('Enter Multiplier:'))
		print(f'\nAnswer={mul(b,c)}')
		continue

	if a=='4' or a=='Division':
		b=float(input('\nDivision\nEnter Dividend:'))
		c=float(input('Enter Divisor:'))
		print(f'\nAnswer={div(b,c)}')
		continue

	if a=='Exit' or a=='5':
		break

	else:
		print('\n###Error###\nInvalid Choice:Choose one of the given operations\n',info)
