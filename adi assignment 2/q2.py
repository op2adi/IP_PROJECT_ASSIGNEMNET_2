c,tot,sgpa,d=[],0,0,[]
while True:
    a=list(map(str,input("enter input").split()))
    if len(a)==3:
        a[1]=int(a[1])
    if len(a)==3:
        for i in range(len(a[0])):
            if a[0][i].isdigit():
                fg=a[0][i+1::]
                if fg=='':
                    break
                else:
                    for j in fg:
                        if j.isalpha():
                            a[0]='cse'
                            break
                    break
    if len(a)==3 and (a[0].isalnum() and a[0].isupper() and (a[1] in [1,2,4]) and a[2].lower() in ['a+','a','a-','b','b-','c','c-','d','f'] and a[0][-1].isdigit()):
        tmp=0
        if a[2].lower() in ["a+","a"]:
            tmp+=10
        elif a[2].lower() in ["a-"]:
            tmp+=9
        elif a[2].lower() in ["b"]:
            tmp+=8
        elif a[2].lower() in ["b-"]:
            tmp+=7
        elif a[2].lower() in ["c"]:
            tmp+=6
        elif a[2].lower() in ['c-']:
            tmp+=5
        elif a[2].lower() in ["d"]:
            tmp+=4
        elif a[2].lower() in ["f"]:
            tmp+=2
        c.append([a[0],': ',a[2]])
        d.append(tmp*a[1])
        tot+=a[1]
    elif a==[]:
        for i in c:
            for j in i:
                print(j,end='')
            print()
        sgpa=sum(d)/tot
        print(f"your sgpa is {round(sgpa,2)}")
        break
    else:
        print ("improper course no","incorrect credit","incorrect grade","less data provided",sep=' or ') 