n = int(input("enter a num:"))
is_prime=True
if n<2:
   is_prime = False
else:
    for i in range(2,n):
        if n%i==0:
           is_prime = False
           break
print("prime" if is_prime else"not prime")