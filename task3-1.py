num1 = [(input("Please, enter the first number: "))]
num2 = [(input("Please, enter the second number: "))]
res = [""]

max_len = max(len(num1[0]), len(num2[0]))

while len(num1[0]) != max_len or len(num2[0]) != max_len:
    if len(num1[0]) != max_len:
        num1[0] = "0" + num1[0]

    elif len(num2) != max_len:
        num2[0] = "0" + num2[0]

num1 = list(num1[0])
num2 = list(num2[0])

for i in range(len(num1)):
    if int(num1[len(num1) - 1 - i]) + int(num2[len(num1) - 1 - i]) >= 10:
        res[0]= (str(int(num1[len(num1) - 1 - i]) + int(num2[len(num2) - 1 - i])))[-1] + res[0]
        num1[len(num1) - 2 - i] = str((int(num1[len(num1) - 2 - i]) + 1))

    else:
        res[0] = str(int(num1[len(num1) - 1 - i]) + int(num2[len(num2) - 1 - i])) + res[0]

if int(num1[0]) + int(num2[0]) >= 10:
    res[0] = "1" + res[0]    


print(int(res[0]))
      


