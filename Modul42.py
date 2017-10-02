list_1 = []     # The first list is for the input
list_2 = []     # The second one is for the input which has gone through the modulus
list_3 = []     # The third one is for the last list where its distinct answers are counted

def modulus(x):
    return x % 42

for i in range (1,11):
    x = int(input())
    list_1.append(x)

for i in range (0, len(list_1)):
        a = modulus(list_1[i])
        list_2.append(a)

for y in set(list_2):
    list_3.append(y)

print(" ")
print ("The distinct answers are:" , len(list_3))
