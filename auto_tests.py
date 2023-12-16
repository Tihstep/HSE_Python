from Calculator import Calculator

calculator = Calculator()

assert calculator.evaluate("5 + 3 * 2") == 11

assert calculator.evaluate("(2 + 4) * 3 + 5 / 2") == 20.5

assert calculator.evaluate("10 * (4 - 2) + 5") == 25

assert calculator.evaluate("4 + 2 * (6 - 3) / 2") == 7

assert calculator.evaluate("2 * -3") == -6

assert calculator.evaluate("1.5 * ((2 - 4 + 3) * 2) / 1.2") == 2.5

assert calculator.evaluate("2 * -(-5)") == 10

assert calculator.evaluate("5 + 3 * 2") == 11

assert calculator.evaluate("(2 + 4) * 3 + 5 / 2") == 20.5

assert calculator.evaluate("10 * (4 - 2) + 5") == 25

assert calculator.evaluate("4 + 2 * (6 - 3) / 2") == 7

assert calculator.evaluate("2 * -3") == -6

assert calculator.evaluate("1.5 * ((2 - 4 + 3) * 2) / 1.2") == 2.5

assert calculator.evaluate("2 * -(-5)") == 10

assert calculator.evaluate("5 + 2 / 4 - 1") == 4.5

assert calculator.evaluate("10 / (4 + 2 * 3)") == 1

assert calculator.evaluate("(4 - 2) / 5 + 3 * 2") == 6.4

assert calculator.evaluate("-4 + 2 * (6 - 1)") == 6

assert calculator.evaluate("-2 - -3 * 4") == 10

assert calculator.evaluate("(2 * 3 - 4) / (1 + 2)") == 0.6666666666666666

print('Тесты пройдены!')
