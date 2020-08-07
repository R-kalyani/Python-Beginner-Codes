def conversion(num,l1):
    if num==0:
        return ""
    elif 1<=num<4:
        return l1[0]*num
    elif num==4:
        return l1[0]+l1[1]
    elif 5<=num<9:
        return l1[1]+l1[0]*(num-5)
    else:
        return l1[0]+l1[2]
    
n=int(input('Number(1-3999): ').strip())
print (n)
if n>=4000 or n==0:
    print("Enter valid number to get converted to roman")
else:
    str1=''
    Roman_list=['I','V','X','L','C','D','M']
    while n>0:
        r=n%10
        str1=conversion(r,Roman_list[0:3])+str1
        n=n//10
        Roman_list=Roman_list[2:]
    print (str1)
    
    

        

                           
    
