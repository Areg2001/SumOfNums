lst1 = []
lst2 = []
res = []
num1 = int(input())
num2 = int(input())

while num1 != 0:
    lst1 = [str(num1 % 1000)] + lst1
    num1 = num1 // 1000  

lst1[0] = ("0" * abs((len(lst1[0])) - 3)) + lst1[0]

while num2 != 0:
    lst2 = [str(num2 % 1000)] + lst2
    num2 = num2 // 1000

lst2[0] = ("0" * abs((len(lst2[0])) - 3)) + lst2[0]

max_len = max(len(lst1), len(lst2))

while len(lst1) != max_len or len(lst2) != max_len:
    if len(lst1) != max_len:
        lst1 = ["000"] + lst1 
    elif len(lst2) != max_len:
        lst2 = ["000"] + lst2   

#for i in range(len(lst1) - 1, -1, -1):
 #   for j in range(len(lst1[i]))


print(lst1)
print(lst2)

    



