print("Enter your boolean integer, 0 = True & 1 = False")
boolean= int(input())
n = int(input())

if boolean==0:
    i = 1
    while i <n:
        a = ("*" *i)
        print(a)
        i = i+1
else:
    i = 1
    while i <n:
        a = ("*" *(n-i))
        print(a)
        i = i+1