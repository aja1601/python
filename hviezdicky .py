 #hviezdicky

n=int(input("Zadaj tvar"))
for python  in range(1,n+1):
    print( python     * "python" )
   
   
n=int(input("Zadaj tvar: "))
for i in range(n):
    print( " "  *(n-i -1) + "*" * (2*i+1))

  
  
n=int(input("Zadaj tvar: "))
for i in range(n):
    print( " "  *(n-i -1) + "*" * (2*i+1))
for i in range(n):
    print( " "  *i + "*" * (2*n - 2*i-1))
    
    
    
    
    
n = int(input('zadaj n: '))
print(' '*(n-1) + '*')
for i in range(1, n-1):
    print(' '*(n-i-1) + '*' + '-'*(2*i-1) + '*')
print('*'*(2*n-1))
