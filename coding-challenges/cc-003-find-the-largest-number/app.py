print("###  This program finds maximum number which you enter ###")
print("How many number you want to enter")
numb = int(input())
x = []
for i in range(numb):
    a = input()
    b = a.isdigit()
    if b == True:
        a = int(a)
        x.append(a)
    else:
        print("Please enter an integer number :")
print ("The orders of numbers that you entered", x)
x = sorted(x, reverse=True)
print("The oreders of numbers that you entered from max to min ", x)
print('The maximum number = ', x[0])
max = 0
for i in x:
    if i > max:
        max = i
print("The oreders of numbers that you entered from max to min", x)
print("The maximum number = ", max)