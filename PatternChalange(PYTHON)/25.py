n=5
print(" "*(n+1)+"*"*(n+2))
for i in range(1,n):
    #print("*"*n)
    print(" "*(n-i)+"*"+" "*(n-1)+"*")
print("*"*(n+2))
