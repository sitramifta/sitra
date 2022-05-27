n = int(input("Input 'n': "))

if(n < 0):
    print("Only positive numbers allowed!")

elif (n < 2):
    print(n)

else:
    while(n != 1):
        print(int(n), end=', ')
        if(n % 2 == 0):
            n = n / 2
        else:
            n = n * 3 + 1
        

print(1)
