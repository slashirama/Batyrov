#Составить функцию, которая напечатает сорок любых символов
import random
import string

random_string = ""

for _ in range(40):
    random_character = random.choice(string.ascii_letters + string.digits + string.punctuation)
    random_string += random_character

print(random_string)
