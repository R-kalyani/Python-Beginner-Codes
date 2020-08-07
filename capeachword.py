def solve(s):
    list1=s.split(' ')
    str2=''
    for i in range(len(list1)):
        if(list1[i]==''):
            list1[i]=' '
        elif (list1[i][0].isalpha()):
            list1[i]=list1[i].capitalize()
        else:
            continue
    for i in list1:
        if(i==' '):
            str2=str2+i
        else:
            str2=str2+i+' '
    print (str2)
s=input()
solve(s)

