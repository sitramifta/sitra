def inertial(digits):
    lar = max(digits)
    odd = False
    
    for d in digits:
        odd = True if d % 2 == 1 else odd
        
    if not odd:
        return 0
    if lar % 2 == 1:
        return 0
    digits.sort()
    for d in reversed(digits):
        if d % 2 == 0 and d != lar:
            small = d
            break
  
    for d in digits:
        if d % 2 == 1 and d < small and small != lar:
            return 0
    return 1
nums = []
size = int(input("Enter the size of the list: "))
print("Enter the numbers here: ")
for _ in range(size):
    nums.append(int(input()))
print("Is Inertial? ", inertial(nums))