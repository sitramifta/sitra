def checkPrime(num):
    for i in range(2, num):
        if(num % i == 0):
            return False
    return True

n = input("Enter a number: ")
nu = int(n)

if(n[len(n) - 1] == "9"):
    if(checkPrime(nu) and checkPrime(nu + 10)):
        print("It's porcupine number")
    else:
        print("NOT porcupine number")
    
else:
    print("NOT porcupine number")



