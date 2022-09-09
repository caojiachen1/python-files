import os , sys , math
def p(k , o):
	k , o = int(k) , int(o)
	for i in range(max(abs(k) , abs(o)) + 1 , 1 , -1):
		if k % i == 0 and o % i == 0:
			return i
	return 1

def p2(k , o , j):
	k , o , j = int(k) , int(o) , int(j)
	for i in range(max(k , max(o , j)) + 1 , 1 , -1):
		if k % i == 0 and o % i == 0 and j % i == 0:
			return i
	return 1

def sprt(k , o , j):
	k , o , j = int(k) , int(o) , int(j)
	for i in range(max(k , max(o , j)) + 1 , 1 , -1):
		if k % i == 0 and o % (i * i) == 0 and j % i == 0:
			return i
	return 1

def q(k):
	k = int(k)
	for i in range(k + 1 , 1 , -1):
		if k % (i * i) == 0:
			return i
	return 1

def isqrt(k):
	k = int(k)
	for i in range(k + 1):
		if k == i * i:
			return True
	return False

a , b , c , delta , eps = 0 , 0 , 0 , 0 , 1e-21

a = int(input('a = '))
b = int(input('b = '))
c = int(input('c = '))
if a == 0:
	xx = p(b , c)
	b = b // xx
	c = c // xx
	if b not in [1 , 0 , -1]:
		if c == 0:
			print('x = 0\n')
		else:
			if c < 0:
				print('{}x - {} = 0\n'.format(b , -c))
				if c % b == 0:
					if b > 0:
						print('x = {}\n'.format(-c / b))
					else:
						print('x = -{}\n'.format(c / b))
				else:
					if b > 0:
						print('x = {}/{}\n'.format(-c , b))
					else:
						print('x = -{}/{}\n'.format(-c , -b))
			else:
				print('{}x + {} = 0\n'.format(b , c))
				if c % b == 0:
					if b > 0:
						print('x = {}\n'.format(-c / b))
					else:
						print('x = -{}\n'.format(-c / b))
				else:
					if b > 0:
						print('x = {}/{}\n'.format(-c , b))
					else:
						print('x = -{}/{}\n'.format(c , -b))
	elif b == 1:
		print('x = {}\n'.format(-c))
	elif b == 0:
		if c == 0:
			print('All x\n')
		else:
			print('No solution\n')
		os.system('pause')
		sys.exit()
	elif b == -1:
		print('x = {}\n'.format(c))
	os.system('pause')
	sys.exit()

cj = p2(a , b , c)
a = a // cj
b = b // cj
c = c // cj

if c == 0:
	if a == 1:
		if b == 1:
			print('x^2 + x = 0\n')
		elif b == -1:
			print('x^2 - x = 0\n')
		else:
			if b > 0:
				print('x^2 + {}x = 0\n'.format(b))
			elif b < 0:
				print('x^2 - {}x = 0\n'.format(-b))
			else:
				print('x^2 = 0\n')	
	elif a == -1:
		if b == 1:
			print('-x^2 + x = 0\n')
		elif b == -1:
			print('-x^2 - x = 0\n')
		else:
			if b > 0:
				print('-x^2 + {}x = 0\n'.format(b))
			elif b < 0:
				print('-x^2 - {}x = 0\n'.format(-b))
			else:
				print('-x^2 = 0\n')
	else:
		if b == 1:
			print('{}x^2 + x = 0\n'.format(a))
		elif b == -1:
			print('{}x^2 - x = 0\n'.format(a))
		else:
			if b > 0:
				print('{}x^2 + {}x = 0\n'.format(a , b))
			elif b < 0:
				print('{}x^2 - {}x = 0\n'.format(a , -b))
			else:
				print('{}x^2 = 0\n'.format(a))
else:
	if c > 0:
		if a == 1:
			if b == 1:
				print('x^2 + x + {} = 0\n'.format(c))
			elif b == -1:
				print('x^2 - x + {} = 0\n'.format(c))
			else:
				if b > 0:
					print('x^2 + {}x + {} = 0\n'.format(b , c))
				elif b < 0:
					print('x^2 - {}x + {} = 0\n'.format(-b , c))
				else:
					print('x^2 + {} = 0\n'.format(c))
		elif a == -1:
			if b == 1:
				print('-x^2 + x + {} = 0\n'.format(c))
			elif b == -1:
				print('-x^2 - x + {} = 0\n'.format(c))
			else:
				if b > 0:
					print('-x^2 + {}x + {} = 0\n'.format(b , c))
				elif b < 0:
					print('-x^2 - {}x + {} = 0\n'.format(-b , c))
				else:
					print('-x^2 + {} = 0\n'.format(c))
		else:
			if b == 1:
				print('{}x^2 + x + {} = 0\n'.format(a , c))
			elif b == -1:
				print('{}x^2 - x + {} = 0\n'.format(a , c))
			else: 
				if b > 0:
					print('{}x^2 + {}x + {} = 0\n'.format(a , b , c))
				elif b < 0:
					print('{}x^2 - {}x + {} = 0\n'.format(a , -b , c))
				elif b == 0:
					print('{}x^2 + {} = 0\n'.format(a , c))
	elif c < 0:
		if a == 1:
			if b == 1:
				print('x^2 + x - {} = 0\n'.format(-c))
			elif b == -1:
				print('x^2 - x - {} = 0\n'.format(-c))
			else:
				if b > 0:
					print('x^2 + {}x - {} = 0\n'.format(b , -c))
				elif b < 0:
					print('x^2 - {}x - {} = 0\n'.format(-b , -c))
				elif b == 0:
					print('x^2 - {} = 0\n'.format(-c))
		elif a == -1:
			if b == 1:
				print('-x^2 + x - {} = 0\n'.format(-c))
			elif b == -1:
				print('-x^2 - x - {} = 0\n'.format(-c))
			else:
				if b > 0:
					print('-x^2 + {}x - {} = 0\n'.format(b , -c))
				elif b < 0:
					print('-x^2 - {}x - {} = 0\n'.format(-b , -c))
				elif b == 0:
					print('-x^2 - {} = 0\n'.format(-c))
		else: 
			if b == 1:
				print('{}x^2 + x - {} = 0\n'.format(a , -c))
			elif b == -1:
				print('{}x^2 - x - {} = 0\n'.format(a , -c))
			else:
				if b > 0:
					print('{}x^2 + {}x - {} = 0\n'.format(a , b , -c)) 
				elif b < 0:
					print('{}x^2 - {}x - {} = 0\n'.format(a , -b , -c)) 
				elif b == 0:
					print('{}x^2 - {} = 0\n'.format(a , -c)) 

de = 2 * a
delta = b * b - 4 * a * c
print('Delta = {}\n'.format(delta))
if delta < 0:
	print('Unreal solution\n')
	delta = -delta
	if isqrt(delta):
		delta = (int)(math.sqrt(delta))
		a0 , b0 = 0 , 0
		aa = p2(b , delta , de)
		b = b // aa
		delta = delta // aa
		de = de // aa
		if b == 0:
			if de == 1:
				if delta == 1:
					print('x1 = i\nx2 = -i\n')
				else:
					print('x1 = {}i\nx2 = - {}i\n'.format(delta , delta))
			elif de == -1:
				if delta == 1:
					print('x1 = i\nx2 = -i\n')
				else:
					print('x1 = {}i\n'.format(delta))
					print('x2 = -{}i\n'.format(delta))
			else:
				if delta == 1:
					print('x1 = ({} + i)/{}\n'.format(-b , de))
					print('x2 = ({} - i)/{}\n'.format(-b , de))
				else:
					print('x1 = ({} + {}i)/{}\n'.format(-b , delta , de))
					print('x2 = ({} - {}i)/{}\n',format(-b , delta , de))
		elif b > 0:
			if de == 1:
				if delta == 1:
					print('x1 = {} + i\n'.format(-b))
					print('x2 = {} - i\n'.format(-b))
				else:
					print('x1 = {} + {}i\n'.format(-b , delta))
					print('x2 = {} - {}i\n'.format(-b , delta))
			elif de == -1:
				if delta == 1:
					print('x1 = {} + i\n'.format(-b))
					print('x2 = {} - i\n'.format(-b))
				else:
					print('x1 = {} + {}i\n'.format(b , delta))
					print('x2 = {} - {}i\n'.format(b , delta))
			else:
				if delta == 1:
					print('x1 = ({} + i)/{}\n'.format(-b , de))
					print('x2 = ({} - i)/{}\n'.format(-b , de))
				else:
					print('x1 = ({} + {}i)/{}\n'.format(-b , delta , de))
					print('x2 = ({} - {}i)/{}\n'.format(-b , delta , de))
		elif b < 0:
			if de == 1:
				if delta == 1:
					print('x1 = {} + i\n'.format(-b))
					print('x2 = {} - i\n'.format(-b))
				else:
					print('x1 = {} + {}i\n'.format(-b , delta))
					print('x2 = {} - {}i\n'.format(-b , delta))
			elif de == -1:
				if delta == 1:
					print('x1 = -{} + i\n'.format(-b))
					print('x2 = -{} - i\n'.format(-b))
				else:
					print('x1 = -{} + {}i\n'.format(-b , delta))
					print('x2 = -{} - {}i\n'.format(-b , delta))
			else:
				if delta == 1:
					print('x1 = ({} + i)/{}\n'.format(-b , de))
					print('x2 = ({} - i)/{}\n'.format(-b , de))
				else:
					print('x1 = ({} + {}i)/{}\n'.format(-b , delta , de))
					print('x2 = ({} - {}i)/{}\n'.format(-b , delta , de))
	else:
		aa = sprt(b , delta , de)
		b = b // aa
		delta = delta // (aa*aa)
		de = de // aa
		aaa = q(delta)
		if b == 0:
			if de == 1:
				if aaa == 1:
					print('x1 = sqrt({})i\n'.format(delta))
					print('x2 = -sqrt({})i\n'.format(delta))
				else:
					print('x1 = {}sqrt({})i\n'.format(aaa , delta // (aaa ** 2)))
					print('x2 = {}sqrt({})i\n'.format(-aaa , delta // (aaa ** 2)))
			elif de == -1:
				if aaa == 1:
					print('x1 = sqrt({})i\n'.format(delta))
					print('x2 = -sqrt({})i\n'.format(delta))
				elif aaa > 0:
					print('x1 = -{}sqrt({})i\n'.format(aaa , delta // (aaa ** 2)))
					print('x2 = -{}sqrt({})i\n'.format(-aaa , delta // (aaa ** 2)))
				else:
					print('x1 = {}sqrt({})i\n'.format(-aaa , delta // (aaa ** 2)))
					print('x2 = -{}sqrt({})i\n'.format(-aaa , delta // (aaa ** 2)))
			else:
				if aaa == 1:
					print('x1 = (sqrt({})i)/{}\n'.format(delta , de))
					print('x2 = (-sqrt({})i)/{}\n'.format(delta , de))
				else:
					print('x1 = ({}sqrt({})i)/{}\n'.format(aaa , delta // (aaa ** 2) , de))
					print('x2 = ({}sqrt({})i)/{}\n'.format(-aaa , delta // (aaa ** 2) , de))
		elif b > 0:
			if de == 1:
				if aaa == 1:
					print('x1 = {} + sqrt({})i\n'.format(-b , delta))
					print('x2 = {} - sqrt({})i\n'.format(-b , delta))
				else:
					print('x1 = {} + {}sqrt({})i\n'.format(-b , aaa , delta // (aaa ** 2)))
					print('x2 = {} - {}sqrt({})i\n'.format(-b , aaa , delta // (aaa ** 2)))
			elif de == -1:
				if aaa == 1:
					print('x1 = {} + sqrt({})i\n'.format(b , delta))
					print('x2 = {} - sqrt({})i\n'.format(b , delta))
				else:
					print('x1 = {} + {}sqrt({})i\n'.format(b , aaa , delta // (aaa ** 2)))
					print('x2 = {} - {}sqrt({})i\n'.format(b , aaa , delta // (aaa ** 2)))
			else:
				if aaa == 1:
					print('x1 = ({} + sqrt({})i)/{}\n'.format(-b , delta , de))
					print('x2 = ({} - sqrt({})i)/{}\n'.format(-b , delta , de))
				else:
					print('x1 = ({} + {}sqrt({})i)/{}\n'.format(-b , aaa , delta // (aaa ** 2) , de))
					print('x2 = ({} - {}sqrt({})i)/{}\n'.format(-b , aaa , delta // (aaa ** 2) , de))
		elif b < 0:
			if de == 1:
				if aaa == 1:
					print('x1 = {} + sqrt({})i\n'.format(-b , delta))
					print('x2 = {} - sqrt({})i\n'.format(-b , delta))
				else:
					print('x1 = {} + {}sqrt({})i\n'.format(-b , aaa , delta // (aaa ** 2)))
					print('x2 = {} - {}sqrt({})i\n'.format(-b , aaa , delta // (aaa ** 2)))
			elif de == -1:
				if aaa == 1:
					print('x1 = -{} + sqrt({})i\n'.format(-b , delta))
					print('x2 = -{} - sqrt({})i\n'.format(-b , delta))
				else:
					print('x1 = -{} + {}sqrt({})i\n'.format(-b , aaa , delta // (aaa ** 2)))
					print('x2 = -{} - {}sqrt({})i\n'.format(-b , aaa , delta // (aaa ** 2)))
			else:
				if aaa == 1:
					print('x1 = ({} + sqrt({})i)/{}\n'.format(-b , delta , de))
					print('x2 = ({} - sqrt({})i)/{}\n'.format(-b , delta , de))
				else:
					print('x1 = ({} + {}sqrt({})i)/{}\n'.format(-b , aaa , delta // (aaa ** 2) , de))
					print('x2 = ({} - {}sqrt({})i)/{}\n'.format(-b , aaa , delta // (aaa ** 2) , de))
	os.system('pause')
	sys.exit()
else:
	print('Real solution\n')
	if isqrt(delta):
		delta = (int)(math.sqrt(delta))
		a0 , b0 = delta - b , -b - delta
		g , h = a0 // de , b0 // de
		if abs(a0-b0) <= eps:
			print('x1 = x2 = {}\n'.format(g))
			os.system('pause')
			sys.exit()
		if a0 == 0:
			print('x1 = 0\n')
		elif a0 % de == 0:
			print('x1 = {}\n'.format(g))
		else:
			if g > 0:
				print('x1 = {}/{}\n'.format(abs(a0//p(a0,de)) , abs(de//p(a0,de))))
			else:
				print('x1 = -{}/{}\n'.format(abs(a0//p(a0,de)) , abs(de//p(a0,de))))
		if b0 == 0:
			print('x2 = 0\n')
		elif b0 % de == 0:
			print('x2 = {}\n'.format(h))
		else: 
			if h > 0:
				print('x2 = {}/{}\n'.format(abs(b0//p(b0,de)) , abs(de//p(b0,de))))
			else:
				print('x2 = -{}/{}\n'.format(abs(b0//p(b0,de)) , abs(de//p(b0,de))))
	else:
		aa = sprt(b , delta , de)
		b = b // aa
		delta = delta // aa ** 2
		de = de // aa
		aaa = q(delta)
		if b == 0:
			if de == 1:
				if aaa == 1:
					print('x1 = sqrt({})\n'.format(delta))
					print('x2 = -sqrt({})\n'.format(delta))
				else:
					print('x1 = {}sqrt({})\n'.format(aaa , delta // (aaa ** 2)))
					print('x2 = {}sqrt({})\n'.format(aaa , delta // (aaa ** 2)))
			elif de == -1:
				if aa == 1:
					print('x1 = sqrt({})\n'.format(delta))
					print('x2 = -sqrt({})\n'.format(delta))
				elif aaa > 0:
					print('x1 = {}sqrt({})\n'.format(aaa , delta // (aaa ** 2)))
					print('x2 = {}sqrt({})\n'.format(-aaa , delta // (aaa ** 2)))
				elif aaa < 0:
					print('x1 = {}sqrt({})\n'.format(-aaa , delta // (aaa ** 2)))
					print('x2 = -{}sqrt({})\n'.format(-aaa , delta // (aaa ** 2)))
			else:
				if aaa == 1:
					print('x1 = (sqrt({}))/{}\n'.format(delta , de))
					print('x2 = (-sqrt({}))/{}\n'.format(delta , de))
				else:
					print('x1 = ({}sqrt({}))/{}\n'.format(aaa , delta // (aaa ** 2) , de))
					print('x2 = ({}sqrt({}))/{}\n'.format(-aaa , delta // (aaa ** 2) , de))
		elif b > 0:
			if de == 1:
				if aaa == 1:
					print('x1 = {} + sqrt({})\n'.format(-b , delta))
					print('x2 = {} - sqrt({})\n'.format(-b , delta))
				else:
					print('x1 = {} + {}sqrt({})\n'.format(-b , aaa , delta // (aaa ** 2)))
					print('x2 = {} - {}sqrt({})\n'.format(-b , aaa , delta // (aaa ** 2)))
			elif de == -1:
				if aaa == 1:
					print('x1 = {} + sqrt({})\n'.format(b , delta))
					print('x2 = {} - sqrt({})\n'.format(-b , delta))
				else:
					print('x1 = {} + {}sqrt({})\n'.format(b , aaa , delta // (aaa ** 2)))
					print('x2 = {} - {}sqrt({})\n'.format(-b , aaa , delta // (aaa ** 2)))
			else:
				if aaa == 1:
					print('x1 = ({} + sqrt({}))/{}\n'.format(-b , delta , de))
					print('x2 = ({} - sqrt({}))/{}\n'.format(-b , delta , de))
				else:
					print('x1 = ({} + {}sqrt({}))/{}\n'.format(-b , aaa , delta // (aaa ** 2) , de))
					print('x2 = ({} - {}sqrt({}))/{}\n'.format(-b , aaa , delta // (aaa ** 2) , de))
		elif b < 0:
			if de == 1:
				if aaa == 1:
					print('x1 = {} + sqrt({})\n'.format(-b , delta))
					print('x2 = {} - sqrt({})\n'.format(-b , delta))
				else:
					print('x1 = {} + {}sqrt({})\n'.format(-b , aaa , delta // (aaa ** 2)))
					print('x2 = {} - {}sqrt({})\n'.format(-b , aaa , delta // (aaa ** 2)))
			elif de == -1:
				if aaa == 1:
					print('x1 = -{} + sqrt({})\n'.format(-b , delta))
					print('x2 = -{} - sqrt({})\n'.format(-b , delta))
				else:
					print('x1 = -{} + {}sqrt({})\n'.format(-b , aaa , delta // (aaa ** 2)))
					print('x2 = -{} - {}sqrt({})\n'.format(-b , aaa , delta // (aaa ** 2)))
			else:
				if aaa == 1:
					print('x1 = ({} + sqrt({}))/{}\n'.format(-b , delta , de))
					print('x2 = ({} - sqrt({}))/{}\n'.format(-b , delta , de))
				else:
					print('x1 = ({} + {}sqrt({}))/{}\n'.format(-b , aaa , delta // (aaa ** 2) , de))
					print('x2 = ({} - {}sqrt({}))/{}\n'.format(-b , aaa , delta // (aaa ** 2) , de))
	os.system('pause')
	sys.exit()