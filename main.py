print('Welcome to Arithemetic Project')

from sum import add
from difference import subtract
from product import multiply
from division import divide

print("2 + 3 =", add(2, 3))
print("7 - 4 =", subtract(7, 4))
print("5 * 6 =", multiply(5, 6))
print("10 / 2 =", divide(10, 2))
print("10 / 0 =", divide(10, 0))
