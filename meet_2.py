list = [3,7,3,6,9,1]
a = -11
b = 2

def min_new(list):
    # n = int(input("podaj ilość elementów w liście :"))
    # list =[]
    # for i in range (0,n):
    #     list.append(input("podaj element: "))
    min = list[0]
    
    for j in range(0,len(list)):
        if min > list[j]:
            min = list[j]
    print("Max of this list is: ",min)

def max_new(list):
    max = list[0]
    for j in range(0,len(list)):
        if max < list[j]:
            max = list[j]
    
    print("Max of this list is: ",max)

def len_new(list):
    len = 0
    for k in list:
        len += 1
    print("\nLenght of this list is: ",len)

def multiply(a,b):
    score = 0
    if (a > 0 and b > 0) or (a<0 and b<0):
        for l in range (0,abs(a)):
            score += abs(b)
        print("Result of multiplication of numbers",a, "and", b, "to :",score)
    else:
        for l in range (0,abs(a)):
            score -= abs(b)
    print("Result of multiplication of numbers",a, "and", b, "to :",score)

def pow(a,b):
    score1 = a
    for l in range (1,b):
        score1 *= a
    print(a, "do potęgi",b, "to :",score1)

def div_new (a,b):
    a = int(input("Podaj pierwszą liczbę: "))
    b = int(input("Podaj druga liczbę: "))
    if (a > 0 and b > 0) or (a<0 and b<0) :
        whole = (int(a/b))
        reszta = a - (whole * b)
        print(whole,"Reszta z dzielienia to :",reszta)
        if reszta == a % b and a//b == whole:
            print("Jest ok")
    elif a < 0 or b < 0:
        whole = (int(a/b))-1
        reszta = a - (whole * b)
        print(whole,"Reszta z dzielienia to :",reszta)
        if reszta == a % b and a//b == whole:
            print("Jest ok")
    else:
        print("Jedna z liczb jest zerem !!!!")
        

len_new(list)
max_new(list)
min_new(list)
multiply(a,b)
pow(a,b)
div_new(a,b)