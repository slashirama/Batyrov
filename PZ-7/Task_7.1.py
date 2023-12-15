# Дано целое число N (32 < N < 126). Вывести символ с кодом, равным N.
import random

N = random.randrange(32, 127)
print("N = ", N, "; Char: ", chr(N))
