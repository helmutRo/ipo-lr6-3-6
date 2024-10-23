import random
from itertools import combinations
number = [random.randint(-10, 10) for i in range(4)for i in range(20)] #создает список
print("список: ", number) #выводится список
unic = list(combinations(number, 2))
print("уникальные пары: ", unic)
a = list(input("введите целое число: "))
scet = sum(1 for para in unic if sum(para) < a)
print(f"положительные элементы  {a}: {scet} ") #вывод колва пол знач

