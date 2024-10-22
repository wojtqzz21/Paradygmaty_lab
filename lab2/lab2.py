from functools import reduce

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

new_numbers = [x ** 2 for x in numbers if x % 2 == 0]
print(new_numbers)

new_number1 = list(map(lambda x: x * 2, numbers))
print(new_number1)

new_number2 = list(filter(lambda x: x % 2 == 1, numbers))
print(new_number2)

new_number3 = reduce(lambda x, y: x + y, numbers)
print(new_number3)

a = 11
result = "3+2*1+a"
wynik = eval(result)
print(wynik)

code = '''
def greet(name):
    return "Hello, " + name

result = greet("World")
'''

exec(code)
print(result)

global_contex = {}
local_contex = {}
exec("x = 10", global_contex, local_contex)
print(local_contex['x'])
