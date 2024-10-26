b,c,wt=[],0,[(10, 5), (20, 5), (100, 15), (40, 10),(50,15),(50,50)]
with open ('ipmarks.txt','r') as f:
    a=f.readlines()
    f.seek(0)
    for i in range(len(a)):
        a=f.readline().split(',')
        b.append(a)
def check_write(c):
    for i in b:
        k=i[0]
        i=i[1::]
        for j in range(len(i)):c+=(int(i[j])*wt[j][1])/wt[j][0]
        grade='A' if c>80 else 'A-'if c>70 else 'B' if c>60 else 'B-' if c>50 else 'C' if c>40 else 'C-' if c>35 else 'D' if c>30 else 'F'
        with open('ipGrade.txt','a') as g:
            k=str(k)
            g.write(str(k)+str(',')+str(c)+str(',')+str(grade)+'\n')
        c=0
check_write(c)