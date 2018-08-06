#!/usr/bin/env python3

import sys 

def compute_money(money1):
	other_monet = money1*0.08+money1*0.02+money1*0.005+money1*0.06
	money = money1 - 3500 - other_monet
	tax = 0
	if money <= 1500 and money >= 0:
		tax = money * 0.03
	elif money > 1500 and money <= 4500:
		tax = money * 0.1 - 105
	elif money > 4500 and money <= 9000:
		tax = money * 0.2 - 555
	elif money > 9000 and money <= 35000:
		tax = money * 0.25 - 1005
	elif money > 35000 and money <= 55000:
		tax = money * 0.3 - 2755
	elif money > 55000 and money <= 80000:
		tax = money * 0.35 - 5505
	elif money > 80000:
		tax = money * 0.45 - 13505
	if tax <= 0 :
		tax = 0
	tax = int(money1) - tax -other_monet
	tax=format(tax,'.2f')

	return tax


if __name__ == '__main__':
	#rint(compute_money(3500))
	for arg in sys.argv[1:]:
		#print(money)
		num = arg.split(':')[0]
		money = arg.split(':')[1]
		#print(num,money)
		try:
			#num = int(num)
			money = int(money)
			#print(compute_money(money))
			print(str(num)+':'+str(compute_money(money)))
		except:
			print('Parameter Error')

