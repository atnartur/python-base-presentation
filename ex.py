def divide(a, b, with_mod=False):
	print('Делим', a, 'на', b) 
	res = 1
	while res * b < a:
		res += 1
	res -= 1
	print("Результат", res)
	if with_mod:
		mod = a - res * b
		print("Остаток", mod)


first = 25
second = 4
with_mod = True
divide(first, second, with_mod)