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

def end():
    os.system('pause')
    sys.exit(0)

delta , eps = 0 , 1e-21
a , b , c = int(input('a = ')) , int(input('b = ')) , int(input('c = '))
show_equation , show_result = '' , ''
show_x1 , show_x2 = '' , ''
result = ['' , '']

if a == 0:
    common_factor = find_common_factor_2numbers(b , c)
    b , c = b // common_factor , c // common_factor
    #b和c互质，c必不整除b
    match b:
        case 1:
            show_equation = ''
            show_result = f'x = {-c}'
            result = [show_equation , show_result]
            print(show_result)
            end()
        case 0:
            show_equation = ''
            show_result = 'All x' if c == 0 else 'No solution'
            result = [show_equation , show_result]
            print(show_result)
            end()
        case -1:
            show_result = f'x = {c}'
            print(show_result)
            end()
    if c == 0:
        show_equation = ''
        show_result = 'x = 0'
        print(show_result)
    elif c < 0:
        show_equation = f'{b}x - {-c} = 0'
        show_result = f'x = {-c}/{b}' if b > 0 else f'x = -{-c}/{-b}'
        print(show_equation)
        print(show_result)
    elif c > 0:
        show_equation = f'{b}x + {c} = 0'
        show_result = f'x = {-c}/{b}' if b > 0 else f'x = -{c}/{-b}'
        print(show_equation)
        print(show_result)
    end()

common_factor = find_common_factor_3numbers(a , b , c)
a , b , c = a // common_factor , b // common_factor , c // common_factor

if c == 0:
    match a:
        case 1:
            match b:
                case 1:
                    show_equation = 'x^2 + x = 0'
                case -1:
                    show_equation = 'x^2 - x = 0'
                case 0:
                    show_equation = 'x^2 = 0'
                case _:
                    show_equation = 'x^2 + {}x = 0'.format(b) if b > 0 else 'x^2 - {}x = 0'.format(-b)
        case -1:
            match b:
                case 1:
                    show_equation = '-x^2 + x = 0'
                case -1:
                    show_equation = '-x^2 - x = 0'
                case 0:
                    show_equation = '-x^2 = 0'
                case _:
                    show_equation = '-x^2 + {}x = 0'.format(b) if b > 0 else '-x^2 - {}x = 0'.format(-b)
        case _:
            match b:
                case 1:
                    show_equation = '{}x^2 + x = 0'.format(a)
                case -1:
                    show_equation = '{}x^2 - x = 0'.format(a)
                case 0:
                    show_equation = '{}x^2 = 0'.format(a)
                case _:
                    show_equation = '{}x^2 + {}x = 0'.format(a , b) if b > 0 else '{}x^2 - {}x = 0'.format(a , -b)
else:
    if c > 0:
        match a:
            case 1:
                match b:
                    case 1:
                        show_equation = 'x^2 + x + {} = 0'.format(c)
                    case -1:
                        show_equation = 'x^2 - x + {} = 0'.format(c)
                    case 0:
                        show_equation = 'x^2 + {} = 0'.format(c)
                    case _:
                        show_equation = 'x^2 + {}x + {} = 0'.format(b , c) if b > 0 else 'x^2 - {}x + {} = 0'.format(-b , c)
            case -1:
                match b:
                    case 1:
                        show_equation = '-x^2 + x + {} = 0'.format(c)
                    case -1:
                        show_equation = '-x^2 - x + {} = 0'.format(c)
                    case 0:
                        show_equation = '-x^2 + {} = 0'.format(c)
                    case _:
                        show_equation = '-x^2 + {}x + {} = 0'.format(b , c) if b > 0 else '-x^2 - {}x + {} = 0'.format(-b , c)
            case _:
                match b:
                    case 1:
                        show_equation = '{}x^2 + x + {} = 0'.format(a , c)
                    case -1:
                        show_equation = '{}x^2 - x + {} = 0'.format(a , c)
                    case 0:
                        show_equation = '{}x^2 + {} = 0'.format(a , c)
                    case _:
                        show_equation = '{}x^2 + {}x + {} = 0'.format(a , b , c) if b > 0 else '{}x^2 - {}x + {} = 0'.format(a , -b , c)
    elif c < 0:
        match a:
            case 1:
                match b:
                    case 1:
                        show_equation = 'x^2 + x - {} = 0'.format(-c)
                    case -1:
                        show_equation = 'x^2 - x - {} = 0'.format(-c)
                    case 0:
                        show_equation = 'x^2 - {} = 0'.format(-c)
                    case _:
                        show_equation = 'x^2 + {}x - {} = 0'.format(b , -c) if b > 0 else 'x^2 - {}x - {} = 0'.format(-b , -c)
            case -1:
                match b:
                    case 1:
                        show_equation = '-x^2 + x - {} = 0'.format(-c)
                    case -1:
                        show_equation = '-x^2 - x - {} = 0'.format(-c)
                    case 0:
                        show_equation = '-x^2 - {} = 0'.format(-c)
                    case _:
                        show_equation = '-x^2 + {}x - {} = 0'.format(b , -c) if b > 0 else '-x^2 - {}x - {} = 0'.format(-b , -c)
            case _:
                match b:
                    case 1:
                        show_equation = '{}x^2 + x - {} = 0'.format(a , -c)
                    case -1:
                        show_equation = '{}x^2 - x - {} = 0'.format(a , -c)
                    case 0:
                        show_equation = '{}x^2 - {} = 0'.format(a , -c)
                    case _:
                        show_equation = '{}x^2 + {}x - {} = 0'.format(a , b , -c) if b > 0 else '{}x^2 - {}x - {} = 0'.format(a , -b , -c)

print(show_equation)
de = 2 * a
delta = b * b - 4 * a * c
print(f'Delta = {delta}')
if delta < 0:
    print('Unreal solution')
    delta = - delta
    if square_or_not(delta):
        delta = (int)(math.sqrt(delta))
        a0 , b0 = 0 , 0
        aa = find_common_factor_3numbers(b , delta , de)
        b , delta , de = b // aa , delta // aa , de // aa
        if b == 0:
            match de:
                case 1:
                    show_result = 'x1 = i\nx2 = -i' if delta == 1 else 'x1 = {}i\nx2 = - {}i'.format(delta , delta)
                case -1:
                    show_result = 'x1 = i\nx2 = -i' if delta == 1 else 'x1 = {}i\nx2 = -{}i'.format(delta , delta)
                case _:
                    show_result = 'x1 = ({} + i)/{}\nx2 = ({} - i)/{}'.format(-b , de , -b , de) if delta == 1 else 'x1 = ({} + {}i)/{}\nx2 = ({} - {}i)/{}'.format(-b , delta , de , -b , delta , de)
        elif b > 0:
            if de == 1:
                show_result = 'x1 = {} + i\nx2 = {} - i'.format(-b , -b) if delta == 1 else f'x1 = {-b} + {delta}i\nx2 = {-b} - {delta}i'
            elif de == -1:
                show_result = 'x1 = {} + i\nx2 = {} - i'.format(-b , -b) if delta == 1 else f'x1 = {b} + {delta}i\nx2 = {b} - {delta}i'
            else:
                show_result = f'x1 = ({-b} + i)/{de}\nx2 = ({-b} - i)/{de}' if delta == 1 else f'x1 = ({-b} + {delta}i)/{de}\nx2 = ({-b} - {delta}i)/{de}'
        elif b < 0:
            if de == 1:
                show_result = 'x1 = {} + i\nx2 = {} - i'.format(-b , -b) if delta == 1 else f'x1 = {-b} + {delta}i\nx2 = {-b} - {delta}i'
            elif de == -1:
                show_result = 'x1 = -{} + i\nx2 = -{} - i'.format(-b , -b) if delta == 1 else 'x1 = -{} + {}i\nx2 = -{} - {}i'.format(-b , delta , -b , delta)
            else:
                show_result = 'x1 = ({} + i)/{}\nx2 = ({} - i)/{}'.format(-b , de , -b , de) if delta == 1 else 'x1 = ({} + {}i)/{}\nx2 = ({} - {}i)/{}'.format(-b , delta , de , -b , delta , de)
    else:
        aa = extract_common_factor(b , delta , de)
        b , delta , de = b // aa , delta // (aa*aa) , de // aa
        aaa = find_square_factor(delta)
        if b == 0:
            if de == 1:
                if aaa == 1:
                    show_result = 'x1 = sqrt({})i\nx2 = -sqrt({})i'.format(delta , delta)
                else:
                    show_result = 'x1 = {}sqrt({})i\nx2 = {}sqrt({})i'.format(aaa , delta // (aaa ** 2) , -aaa , delta // (aaa ** 2))
            elif de == -1:
                if aaa == 1:
                    show_result = 'x1 = sqrt({})i\nx2 = -sqrt({})i'.format(delta , delta)
                elif aaa > 0:
                    show_result = 'x1 = -{}sqrt({})i\nx2 = -{}sqrt({})i'.format(aaa , delta // (aaa ** 2) , -aaa , delta // (aaa ** 2))
                else:
                    show_result = 'x1 = {}sqrt({})i\nx2 = -{}sqrt({})i'.format(-aaa , delta // (aaa ** 2) , -aaa , delta // (aaa ** 2))
            else:
                if aaa == 1:
                    show_result = 'x1 = (sqrt({})i)/{}\nx2 = (-sqrt({})i)/{}'.format(delta , de , delta , de)
                else:
                    show_result = f'x1 = ({aaa}sqrt({delta // (aaa ** 2)})i)/{de}\nx2 = ({-aaa}sqrt({delta // (aaa ** 2)})i)/{de}'
        elif b > 0:
            if de == 1:
                if aaa == 1:
                    show_result = 'x1 = {} + sqrt({})i\nx2 = {} - sqrt({})i'.format(-b , delta , -b , delta)
                else:
                    show_result = f'x1 = {-b} + {aaa}sqrt({delta // (aaa ** 2)})i\nx2 = {-b} - {aaa}sqrt({delta // (aaa ** 2)})i'
            elif de == -1:
                if aaa == 1:
                    show_result = 'x1 = {} + sqrt({})i\nx2 = {} - sqrt({})i'.format(b , delta , b , delta)
                else:
                    show_result = f'x1 = {b} + {aaa}sqrt({delta // (aaa ** 2)})i\nx2 = {b} - {aaa}sqrt({delta // (aaa ** 2)})i'
            else:
                if aaa == 1:
                    show_result = f'x1 = ({-b} + sqrt({delta})i)/{de}\nx2 = ({-b} - sqrt({delta})i)/{de}'
                else:
                    show_result = f'x1 = ({-b} + {aaa}sqrt({delta // (aaa ** 2)})i)/{de}\nx2 = ({-b} - {aaa}sqrt({delta // (aaa ** 2)})i)/{de}'
        elif b < 0:
            if de == 1:
                if aaa == 1:
                    show_result = 'x1 = {} + sqrt({})i\nx2 = {} - sqrt({})i'.format(-b , delta , -b , delta)
                else:
                    show_result = f'x1 = {-b} + {aaa}sqrt({delta // (aaa ** 2)})i\nx2 = {-b} - {aaa}sqrt({delta // (aaa ** 2)})i'
            elif de == -1:
                if aaa == 1:
                    show_result = 'x1 = -{} + sqrt({})i\nx2 = -{} - sqrt({})i'.format(-b , delta , -b , delta)
                else:
                    show_result = f'x1 = -{-b} + {aaa}sqrt({delta // (aaa ** 2)})i\nx2 = -{-b} - {aaa}sqrt({delta // (aaa ** 2)})i'
            else:
                if aaa == 1:
                    show_result = 'x1 = ({} + sqrt({})i)/{}\nx2 = ({} - sqrt({})i)/{}'.format(-b , delta , de , -b , delta , de)
                else:
                    show_result = f'x1 = ({-b} + {aaa}sqrt({delta // (aaa ** 2)})i)/{de}\nx2 = ({-b} - {aaa}sqrt({delta // (aaa ** 2)})i)/{de}'
else:
    print('Real solution')
    if square_or_not(delta):
        delta = (int)(math.sqrt(delta))
        a0 , b0 = - b + delta , - b - delta
        g , h = a0 // de , b0 // de
        if abs(a0 - b0) <= eps:
            show_result = f'x1 = x2 = {g}'
            print(show_result)
            end()
        if a0 == 0:
            show_result = 'x1 = 0\n'
        elif a0 % de == 0:
            show_result = f'x1 = {g}\n'
        else:
            factor = find_common_factor_2numbers(a0 , de)
            if g > 0:
                show_result = 'x1 = {}/{}\n'.format(abs(a0 // factor) , abs(de // factor))
            else:
                show_result = 'x1 = -{}/{}\n'.format(abs(a0 // factor) , abs(de // factor))
        if b0 == 0:
            show_result += 'x2 = 0'
        elif b0 % de == 0:
            show_result += 'x2 = {}'.format(h)
        else:
            factor = find_common_factor_2numbers(b0 , de)
            if h > 0:
                show_result += 'x2 = {}/{}'.format(abs(b0 // factor) , abs(de // factor))
            else:
                show_result += 'x2 = -{}/{}'.format(abs(b0 // factor) , abs(de // factor))
    else:
        aa = extract_common_factor(b , delta , de)
        b = b // aa
        delta = delta // aa ** 2
        de = de // aa
        aaa = find_square_factor(delta)
        if b == 0:
            if de == 1:
                show_result = 'x1 = sqrt({})\nx2 = -sqrt({})'.format(delta , delta) if aaa == 1 else f'x1 = {aaa}sqrt({delta // (aaa ** 2)})\nx2 = {aaa}sqrt({delta // (aaa ** 2)})'
            elif de == -1:
                if aa == 1:
                    show_result = 'x1 = sqrt({})\nx2 = -sqrt({})'.format(delta , delta)
                elif aaa > 0:
                    show_result = f'x1 = {aaa}sqrt({delta // (aaa ** 2)})\nx2 = {-aaa}sqrt({delta // (aaa ** 2)})'
                elif aaa < 0:
                    show_result = f'x1 = {-aaa}sqrt({delta // (aaa ** 2)})\nx2 = -{-aaa}sqrt({delta // (aaa ** 2)})'
            else:
                if aaa == 1:
                    show_result = 'x1 = (sqrt({}))/{}\nx2 = (-sqrt({}))/{}'.format(delta , de , delta , de)
                else:
                    show_result = f'x1 = ({aaa}sqrt({delta // (aaa ** 2)}))/{de}\nx2 = ({-aaa}sqrt({delta // (aaa ** 2)}))/{de}'
        elif b > 0:
            if de == 1:
                if aaa == 1:
                    show_result = 'x1 = {} + sqrt({})\nx2 = {} - sqrt({})'.format(-b , delta , -b , delta)
                else:
                    show_result = f'x1 = {-b} + {aaa}sqrt({delta // (aaa ** 2)})\nx2 = {-b} - {aaa}sqrt({delta // (aaa ** 2)})'
            elif de == -1:
                if aaa == 1:
                    show_result = 'x1 = {} + sqrt({})\nx2 = {} - sqrt({})'.format(b , delta , -b , delta)
                else:
                    show_result = f'x1 = {b} + {aaa}sqrt({delta // (aaa ** 2)})\nx2 = {-b} - {aaa}sqrt({delta // (aaa ** 2)})'
            else:
                if aaa == 1:
                    show_result = 'x1 = ({} + sqrt({}))/{}\nx2 = ({} - sqrt({}))/{}'.format(-b , delta , de , -b , delta , de)
                else:
                    show_result = f'x1 = ({-b} + {aaa}sqrt({delta // (aaa ** 2)}))/{de}\nx2 = ({-b} - {aaa}sqrt({delta // (aaa ** 2)}))/{de}'
        elif b < 0:
            if de == 1:
                if aaa == 1:
                    show_result = 'x1 = {} + sqrt({})\nx2 = {} - sqrt({})'.format(-b , delta , -b , delta)
                else:
                    show_result = f'x1 = {-b} + {aaa}sqrt({delta // (aaa ** 2)})\nx2 = {-b} - {aaa}sqrt({delta // (aaa ** 2)})'
            elif de == -1:
                if aaa == 1:
                    show_result = f'x1 = -{-b} + sqrt({delta})\nx2 = -{-b} - sqrt({delta})'
                else:
                    show_result = f'x1 = -{-b} + {aaa}sqrt({delta // (aaa ** 2)})\nx2 = -{-b} - {aaa}sqrt({delta // (aaa ** 2)})'
            else:
                if aaa == 1:
                    show_result = f'x1 = ({-b} + sqrt({delta}))/{de}\nx2 = ({-b} - sqrt({delta}))/{de}'
                else:
                    show_result = f'x1 = ({-b} + {aaa}sqrt({delta // (aaa ** 2)}))/{de}\nx2 = ({-b} - {aaa}sqrt({delta // (aaa ** 2)}))/{de}'
print(show_result)
end()