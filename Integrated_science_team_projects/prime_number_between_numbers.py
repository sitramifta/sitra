counter=0
num1 = int(input("Enter the first Number: "))
num2 = int(input("Enter the second number: "))
 
print('Prime numbers between',num1,' and',num2,' are:')
 
for num in range(num1,num2 + 1):
    if num > 1:
        for i in range(2,num):
            if (num % i) == 0:
                break
        else:
            print(num)
            counter=counter+1
print('{0} prime numbers'.format(counter))