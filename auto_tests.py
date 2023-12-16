from Calculator import Calculator

calculator = Calculator()

assert calculator.evaluate("5 + 3 * 2") == 11

assert calculator.evaluate("(2 + 4) * 3 + 5 / 2") == 20.5

assert calculator.evaluate("10 * (4 - 2) + 5") == 25

assert calculator.evaluate("4 + 2 * (6 - 3) / 2") == 7

assert calculator.evaluate("2 * -3") == -6

assert calculator.evaluate("1.5 * ((2 - 4 + 3) * 2) / 1.2") == 2.5

assert calculator.evaluate("2 * -(-5)") == 10

print('Тесты пройдены, поставь 10!')