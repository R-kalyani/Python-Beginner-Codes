n=int(input().strip())
str='H'
for i in range(1,(2*n)+1,2):
    str1=str*(i)
    print(str1.center((2*n)-1,' '))
for i in range(n+1):
    str1=str*n
    str1=str1.rjust((3*(n//2))+1,' ')+str1.rjust(4*n,' ')
    print(str1)
for i in range(n-(n//2)):
    str1=str*n
    str1=str1.rjust((3*(n//2))+1,' ')+str1*4
    print(str1)
for i in range(n+1):
    str1=str*n
    str1=str1.rjust((3*(n//2))+1,' ')+str1.rjust(4*n,' ')
    print(str1)
c=0
for i in range(1,(2*n)+1,2):
    str1=str*((2*n)-i)
    print(str1.rjust((6*n)-1-c,' '))
    c=c+1
