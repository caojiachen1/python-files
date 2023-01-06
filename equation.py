import os , sys , math
def find_common_factor_2numbers(k , o):
	k , o = int(k) , int(o)
	return next(
		(
			i
			for i in range(max(abs(k), abs(o)) + 1, 1, -1)
			if k % i == 0 and o % i == 0
		),
		1,
	)

def find_common_factor_3numbers(k , o , j):
	k , o , j = int(k) , int(o) , int(j)
	return next(
		(
			i
			for i in range(max(k, max(o, j)) + 1, 1, -1)
			if k % i == 0 and o % i == 0 and j % i == 0
		),
		1,
	)

def extract_common_factor(k , o , j):
	k , o , j = int(k) , int(o) , int(j)
	return next(
		(
			i
			for i in range(max(k, max(o, j)) + 1, 1, -1)
			if k % i == 0 and o % (i * i) == 0 and j % i == 0
		),
		1,
	)

def find_square_factor(k):
	k = int(k)
	return next((i for i in range(k + 1 , 1 , -1) if k % (i * i) == 0), 1)

def square_or_not(k):
	k = int(k)
	return any(k == i * i for i in range(k + 1))

delta , eps = 0 , 1e-21
a , b , c = int(input('a = ')) , int(input('b = ')) , int(input('c = '))
show_equation , show_result = '' , ''
show_x1 , show_x2 = '' , ''

if a == 0:
	common_factor = find_common_factor_2numbers(b , c)
	b , c = b // common_factor , c // common_factor
	#b和c互质，c必不整除b
	if b not in [1 , 0 , -1]:
		if c == 0:
			show_equation = ''
			show_result = 'x = 0'
		else:
			if c < 0:
				show_equation = '{}x - {} = 0'.format(b , -c)
				show_result = 'x = {}/{}'.format(-c , b) if b > 0 else 'x = -{}/{}'.format(-c , -b)
			else:
				show_equation = '{}x + {} = 0'.format(b , c)
				show_result = 'x = {}/{}'.format(-c , b) if b > 0 else 'x = -{}/{}'.format(c , -b)
	elif b == 1:
		show_result = 'x = {}'.format(-c)
	elif b == 0:
		show_result = 'All x' if c == 0 else 'No solution'
		os.system('pause')
		sys.exit()
	elif b == -1:
		show_result = 'x = {}'.format(c)
	os.system('pause')
	sys.exit()

common_factor = find_common_factor_3numbers(a , b , c)
a , b , c = a // common_factor , b // common_factor , c // common_factor

if c == 0:
	if a == 1:
		if b == 1:
			show_equation = 'x^2 + x = 0'
		elif b == -1:
			show_equation = 'x^2 - x = 0'
		elif b == 0:
			show_equation = 'x^2 = 0'
		else:
			show_equation = 'x^2 + {}x = 0'.format(b) if b > 0 else 'x^2 - {}x = 0'.format(-b)
	elif a == -1:
		if b == 1:
			show_equation = '-x^2 + x = 0'
		elif b == -1:
			show_equation = '-x^2 - x = 0'
		elif b == 0:
			show_equation = '-x^2 = 0'
		else:
			show_equation = '-x^2 + {}x = 0'.format(b) if b > 0 else '-x^2 - {}x = 0'.format(-b)
	else:
		if b == 1:
			show_equation = '{}x^2 + x = 0'.format(a)
		elif b == -1:
			show_equation = '{}x^2 - x = 0'.format(a)
		elif b == 0:
			show_equation = '{}x^2 = 0'.format(a)
		else:
			if b > 0:
				print('{}x^2 + {}x = 0'.format(a , b))
			elif b < 0:
				print('{}x^2 - {}x = 0'.format(a , -b))
else:
	if c > 0:
		if a == 1:
			if b == 1:
				print('x^2 + x + {} = 0'.format(c))
			elif b == -1:
				print('x^2 - x + {} = 0'.format(c))
			else:
				if b > 0:
					print('x^2 + {}x + {} = 0'.format(b , c))
				elif b < 0:
					print('x^2 - {}x + {} = 0'.format(-b , c))
				else:
					print('x^2 + {} = 0'.format(c))
		elif a == -1:
			if b == 1:
				print('-x^2 + x + {} = 0'.format(c))
			elif b == -1:
				print('-x^2 - x + {} = 0'.format(c))
			else:
				if b > 0:
					print('-x^2 + {}x + {} = 0'.format(b , c))
				elif b < 0:
					print('-x^2 - {}x + {} = 0'.format(-b , c))
				else:
					print('-x^2 + {} = 0'.format(c))
		else:
			if b == 1:
				print('{}x^2 + x + {} = 0'.format(a , c))
			elif b == -1:
				print('{}x^2 - x + {} = 0'.format(a , c))
			else: 
				if b > 0:
					print('{}x^2 + {}x + {} = 0'.format(a , b , c))
				elif b < 0:
					print('{}x^2 - {}x + {} = 0'.format(a , -b , c))
				elif b == 0:
					print('{}x^2 + {} = 0'.format(a , c))
	elif c < 0:
		if a == 1:
			if b == 1:
				print('x^2 + x - {} = 0'.format(-c))
			elif b == -1:
				print('x^2 - x - {} = 0'.format(-c))
			else:
				if b > 0:
					print('x^2 + {}x - {} = 0'.format(b , -c))
				elif b < 0:
					print('x^2 - {}x - {} = 0'.format(-b , -c))
				elif b == 0:
					print('x^2 - {} = 0'.format(-c))
		elif a == -1:
			if b == 1:
				print('-x^2 + x - {} = 0'.format(-c))
			elif b == -1:
				print('-x^2 - x - {} = 0'.format(-c))
			else:
				if b > 0:
					print('-x^2 + {}x - {} = 0'.format(b , -c))
				elif b < 0:
					print('-x^2 - {}x - {} = 0'.format(-b , -c))
				elif b == 0:
					print('-x^2 - {} = 0'.format(-c))
		else: 
			if b == 1:
				print('{}x^2 + x - {} = 0'.format(a , -c))
			elif b == -1:
				print('{}x^2 - x - {} = 0'.format(a , -c))
			else:
				if b > 0:
					print('{}x^2 + {}x - {} = 0'.format(a , b , -c)) 
				elif b < 0:
					print('{}x^2 - {}x - {} = 0'.format(a , -b , -c)) 
				elif b == 0:
					print('{}x^2 - {} = 0'.format(a , -c)) 

de = 2 * a
delta = b * b - 4 * a * c
print('Delta = {}'.format(delta))
if delta < 0:
	print('Unreal solution')
	delta = -delta
	if square_or_not(delta):
		delta = (int)(math.sqrt(delta))
		a0 , b0 = 0 , 0
		aa = find_common_factor_3numbers(b , delta , de)
		b = b // aa
		delta = delta // aa
		de = de // aa
		if b == 0:
			if de == 1:
				if delta == 1:
					print('x1 = ix2 = -i')
				else:
					print('x1 = {}ix2 = - {}i'.format(delta , delta))
			elif de == -1:
				if delta == 1:
					print('x1 = ix2 = -i')
				else:
					print('x1 = {}i'.format(delta))
					print('x2 = -{}i'.format(delta))
			else:
				if delta == 1:
					print('x1 = ({} + i)/{}'.format(-b , de))
					print('x2 = ({} - i)/{}'.format(-b , de))
				else:
					print('x1 = ({} + {}i)/{}'.format(-b , delta , de))
					print('x2 = ({} - {}i)/{}',format(-b , delta , de))
		elif b > 0:
			if de == 1:
				if delta == 1:
					print('x1 = {} + i'.format(-b))
					print('x2 = {} - i'.format(-b))
				else:
					print('x1 = {} + {}i'.format(-b , delta))
					print('x2 = {} - {}i'.format(-b , delta))
			elif de == -1:
				if delta == 1:
					print('x1 = {} + i'.format(-b))
					print('x2 = {} - i'.format(-b))
				else:
					print('x1 = {} + {}i'.format(b , delta))
					print('x2 = {} - {}i'.format(b , delta))
			else:
				if delta == 1:
					print('x1 = ({} + i)/{}'.format(-b , de))
					print('x2 = ({} - i)/{}'.format(-b , de))
				else:
					print('x1 = ({} + {}i)/{}'.format(-b , delta , de))
					print('x2 = ({} - {}i)/{}'.format(-b , delta , de))
		elif b < 0:
			if de == 1:
				if delta == 1:
					print('x1 = {} + i'.format(-b))
					print('x2 = {} - i'.format(-b))
				else:
					print('x1 = {} + {}i'.format(-b , delta))
					print('x2 = {} - {}i'.format(-b , delta))
			elif de == -1:
				if delta == 1:
					print('x1 = -{} + i'.format(-b))
					print('x2 = -{} - i'.format(-b))
				else:
					print('x1 = -{} + {}i'.format(-b , delta))
					print('x2 = -{} - {}i'.format(-b , delta))
			else:
				if delta == 1:
					print('x1 = ({} + i)/{}'.format(-b , de))
					print('x2 = ({} - i)/{}'.format(-b , de))
				else:
					print('x1 = ({} + {}i)/{}'.format(-b , delta , de))
					print('x2 = ({} - {}i)/{}'.format(-b , delta , de))
	else:
		aa = extract_common_factor(b , delta , de)
		b = b // aa
		delta = delta // (aa*aa)
		de = de // aa
		aaa = find_square_factor(delta)
		if b == 0:
			if de == 1:
				if aaa == 1:
					print('x1 = sqrt({})i'.format(delta))
					print('x2 = -sqrt({})i'.format(delta))
				else:
					print('x1 = {}sqrt({})i'.format(aaa , delta // (aaa ** 2)))
					print('x2 = {}sqrt({})i'.format(-aaa , delta // (aaa ** 2)))
			elif de == -1:
				if aaa == 1:
					print('x1 = sqrt({})i'.format(delta))
					print('x2 = -sqrt({})i'.format(delta))
				elif aaa > 0:
					print('x1 = -{}sqrt({})i'.format(aaa , delta // (aaa ** 2)))
					print('x2 = -{}sqrt({})i'.format(-aaa , delta // (aaa ** 2)))
				else:
					print('x1 = {}sqrt({})i'.format(-aaa , delta // (aaa ** 2)))
					print('x2 = -{}sqrt({})i'.format(-aaa , delta // (aaa ** 2)))
			else:
				if aaa == 1:
					print('x1 = (sqrt({})i)/{}'.format(delta , de))
					print('x2 = (-sqrt({})i)/{}'.format(delta , de))
				else:
					print('x1 = ({}sqrt({})i)/{}'.format(aaa , delta // (aaa ** 2) , de))
					print('x2 = ({}sqrt({})i)/{}'.format(-aaa , delta // (aaa ** 2) , de))
		elif b > 0:
			if de == 1:
				if aaa == 1:
					print('x1 = {} + sqrt({})i'.format(-b , delta))
					print('x2 = {} - sqrt({})i'.format(-b , delta))
				else:
					print('x1 = {} + {}sqrt({})i'.format(-b , aaa , delta // (aaa ** 2)))
					print('x2 = {} - {}sqrt({})i'.format(-b , aaa , delta // (aaa ** 2)))
			elif de == -1:
				if aaa == 1:
					print('x1 = {} + sqrt({})i'.format(b , delta))
					print('x2 = {} - sqrt({})i'.format(b , delta))
				else:
					print('x1 = {} + {}sqrt({})i'.format(b , aaa , delta // (aaa ** 2)))
					print('x2 = {} - {}sqrt({})i'.format(b , aaa , delta // (aaa ** 2)))
			else:
				if aaa == 1:
					print('x1 = ({} + sqrt({})i)/{}'.format(-b , delta , de))
					print('x2 = ({} - sqrt({})i)/{}'.format(-b , delta , de))
				else:
					print('x1 = ({} + {}sqrt({})i)/{}'.format(-b , aaa , delta // (aaa ** 2) , de))
					print('x2 = ({} - {}sqrt({})i)/{}'.format(-b , aaa , delta // (aaa ** 2) , de))
		elif b < 0:
			if de == 1:
				if aaa == 1:
					print('x1 = {} + sqrt({})i'.format(-b , delta))
					print('x2 = {} - sqrt({})i'.format(-b , delta))
				else:
					print('x1 = {} + {}sqrt({})i'.format(-b , aaa , delta // (aaa ** 2)))
					print('x2 = {} - {}sqrt({})i'.format(-b , aaa , delta // (aaa ** 2)))
			elif de == -1:
				if aaa == 1:
					print('x1 = -{} + sqrt({})i'.format(-b , delta))
					print('x2 = -{} - sqrt({})i'.format(-b , delta))
				else:
					print('x1 = -{} + {}sqrt({})i'.format(-b , aaa , delta // (aaa ** 2)))
					print('x2 = -{} - {}sqrt({})i'.format(-b , aaa , delta // (aaa ** 2)))
			else:
				if aaa == 1:
					print('x1 = ({} + sqrt({})i)/{}'.format(-b , delta , de))
					print('x2 = ({} - sqrt({})i)/{}'.format(-b , delta , de))
				else:
					print('x1 = ({} + {}sqrt({})i)/{}'.format(-b , aaa , delta // (aaa ** 2) , de))
					print('x2 = ({} - {}sqrt({})i)/{}'.format(-b , aaa , delta // (aaa ** 2) , de))
	os.system('pause')
	sys.exit()
else:
	print('Real solution')
	if square_or_not(delta):
		delta = (int)(math.sqrt(delta))
		a0 , b0 = delta - b , -b - delta
		g , h = a0 // de , b0 // de
		if abs(a0-b0) <= eps:
			print('x1 = x2 = {}'.format(g))
			os.system('pause')
			sys.exit()
		if a0 == 0:
			print('x1 = 0')
		elif a0 % de == 0:
			print('x1 = {}'.format(g))
		else:
			if g > 0:
				print('x1 = {}/{}'.format(abs(a0//find_common_factor_2numbers(a0,de)) , abs(de//find_common_factor_2numbers(a0,de))))
			else:
				print('x1 = -{}/{}'.format(abs(a0//find_common_factor_2numbers(a0,de)) , abs(de//find_common_factor_2numbers(a0,de))))
		if b0 == 0:
			print('x2 = 0')
		elif b0 % de == 0:
			print('x2 = {}'.format(h))
		else: 
			if h > 0:
				print('x2 = {}/{}'.format(abs(b0//find_common_factor_2numbers(b0,de)) , abs(de//find_common_factor_2numbers(b0,de))))
			else:
				print('x2 = -{}/{}'.format(abs(b0//find_common_factor_2numbers(b0,de)) , abs(de//find_common_factor_2numbers(b0,de))))
	else:
		aa = extract_common_factor(b , delta , de)
		b = b // aa
		delta = delta // aa ** 2
		de = de // aa
		aaa = find_square_factor(delta)
		if b == 0:
			if de == 1:
				if aaa == 1:
					print('x1 = sqrt({})'.format(delta))
					print('x2 = -sqrt({})'.format(delta))
				else:
					print('x1 = {}sqrt({})'.format(aaa , delta // (aaa ** 2)))
					print('x2 = {}sqrt({})'.format(aaa , delta // (aaa ** 2)))
			elif de == -1:
				if aa == 1:
					print('x1 = sqrt({})'.format(delta))
					print('x2 = -sqrt({})'.format(delta))
				elif aaa > 0:
					print('x1 = {}sqrt({})'.format(aaa , delta // (aaa ** 2)))
					print('x2 = {}sqrt({})'.format(-aaa , delta // (aaa ** 2)))
				elif aaa < 0:
					print('x1 = {}sqrt({})'.format(-aaa , delta // (aaa ** 2)))
					print('x2 = -{}sqrt({})'.format(-aaa , delta // (aaa ** 2)))
			else:
				if aaa == 1:
					print('x1 = (sqrt({}))/{}'.format(delta , de))
					print('x2 = (-sqrt({}))/{}'.format(delta , de))
				else:
					print('x1 = ({}sqrt({}))/{}'.format(aaa , delta // (aaa ** 2) , de))
					print('x2 = ({}sqrt({}))/{}'.format(-aaa , delta // (aaa ** 2) , de))
		elif b > 0:
			if de == 1:
				if aaa == 1:
					print('x1 = {} + sqrt({})'.format(-b , delta))
					print('x2 = {} - sqrt({})'.format(-b , delta))
				else:
					print('x1 = {} + {}sqrt({})'.format(-b , aaa , delta // (aaa ** 2)))
					print('x2 = {} - {}sqrt({})'.format(-b , aaa , delta // (aaa ** 2)))
			elif de == -1:
				if aaa == 1:
					print('x1 = {} + sqrt({})'.format(b , delta))
					print('x2 = {} - sqrt({})'.format(-b , delta))
				else:
					print('x1 = {} + {}sqrt({})'.format(b , aaa , delta // (aaa ** 2)))
					print('x2 = {} - {}sqrt({})'.format(-b , aaa , delta // (aaa ** 2)))
			else:
				if aaa == 1:
					print('x1 = ({} + sqrt({}))/{}'.format(-b , delta , de))
					print('x2 = ({} - sqrt({}))/{}'.format(-b , delta , de))
				else:
					print('x1 = ({} + {}sqrt({}))/{}'.format(-b , aaa , delta // (aaa ** 2) , de))
					print('x2 = ({} - {}sqrt({}))/{}'.format(-b , aaa , delta // (aaa ** 2) , de))
		elif b < 0:
			if de == 1:
				if aaa == 1:
					print('x1 = {} + sqrt({})'.format(-b , delta))
					print('x2 = {} - sqrt({})'.format(-b , delta))
				else:
					print('x1 = {} + {}sqrt({})'.format(-b , aaa , delta // (aaa ** 2)))
					print('x2 = {} - {}sqrt({})'.format(-b , aaa , delta // (aaa ** 2)))
			elif de == -1:
				if aaa == 1:
					print('x1 = -{} + sqrt({})'.format(-b , delta))
					print('x2 = -{} - sqrt({})'.format(-b , delta))
				else:
					print('x1 = -{} + {}sqrt({})'.format(-b , aaa , delta // (aaa ** 2)))
					print('x2 = -{} - {}sqrt({})'.format(-b , aaa , delta // (aaa ** 2)))
			else:
				if aaa == 1:
					print('x1 = ({} + sqrt({}))/{}'.format(-b , delta , de))
					print('x2 = ({} - sqrt({}))/{}'.format(-b , delta , de))
				else:
					print('x1 = ({} + {}sqrt({}))/{}'.format(-b , aaa , delta // (aaa ** 2) , de))
					print('x2 = ({} - {}sqrt({}))/{}'.format(-b , aaa , delta // (aaa ** 2) , de))
	os.system('pause')
	sys.exit()