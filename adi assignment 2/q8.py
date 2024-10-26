d,e,c,main={},[],0,{}
with open("q8.txt","r") as f:
    for line in f:
        a=line.split()
        d[a[0].split(',')[0]] =0
f=open('q8.txt','r')
g=[line.split() for line in f]
for i in range(len(g)):
    m=list(d.keys())[i]
    for j in range(len(g)):
        jp=str(g[j])
        c=jp.count("URL")-1
        if g[j][0]==m+",":continue
        else:
            if g[j].count(m+',')>0:e.append(round(((float(g[j][1][:-1:])))/c,2))
    main[m],e=round(sum(e),2),[]
ordered,n=sorted(main.items(),key=lambda x:x[1],reverse=True),int(input("Enter The rank"))
print(dict(ordered[0:n])) if n<=len(ordered) else print("Entered 0 or negative value") if n<=0 else print(dict(ordered),"Given n is greater than total links")