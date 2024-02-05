import random
first_list = []
second_list = []
length = 100
number = 1

for i in range(100):
    x = random.randint (1, 100)
    first_list.append (x)
for i in range(100):
    second_list.append(first_list[length-number])
    number = number + 1

print(first_list)
print(second_list)
