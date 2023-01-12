import random
x = (random.randint(0, 9))
print(x)
y = (random.randint(0, 9))
print(y)
z = int(input("Answer by multiplication:"))
if z == int(x)*int(y):
    print("Great,right answer")
else:
    print("Sorry,wrong answer", "right answer is:", x*y)

