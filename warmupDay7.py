# File name: warmupDay7.py
num = 0
while num < 101:
    if num % 5 == 0:
        print(num)
    num += 1

for i in range(101):
    if i % 5 == 0:
        print(i)

starnum = 7
while starnum > 0:
    print('*' * starnum)
    starnum -= 2

for i in range(4,83):
  if i % 2 == 0:
    print(i, "blue")
  else:
    print(i, "green")
