def find(qw,s):
    for i in lop:
                kp=list(i.values())
                if kp[0][qw]==s:
                    print(f"found match {i}")
                    break
f,lid,d,l,e,lop=open('addressbook.txt','r+'),[],{},[],{},[]
f.seek(0,0)
c=0
for line in f:
    if c==0:
        lid=line.split('\n')[0:1:]
    else:
        lid+=line.split('\n')[0:1:]
    c+=1
for i in lid:
    lop.append(i[1:-1:])
lop=[eval(i) for i in lop]
print(lop)
print(''' choice letter
1)  insert a new entry
2)  delete an entry 
3) find all matching entries given a partial name
4) find the entry with a phone number or email
5) exit ''')
while True:
    a=int(input("enter choice "))
    if a==1:
        name=input('enter name ')
        address=input('enter address ')
        phno=(input("mobile number "))
        while len(phno)!=10:
            print("Wrong number not exist enter again")
            phno=input("enter mobile number ")
        email=input("enter email id ")
        e["address"]=address
        e["phno"]=phno
        e["email"]=email
        d[name]=e
        l.append(d)
        lop.append(d)
        f.write(str(l)+'\n')
        l=[]
    elif a==2:
        print("you are deleting an enter")
        s=input("enter name of the input you want to delete")
        kp=list(lop)
        sp=list(lop)
        for i in kp:
            if s in i:
                sp.remove(i)
        print('Deleted') if kp!=sp else print("NO entries found")
        lop=list(sp)
    elif a==3:
        kep=list(lop)
        s=input("enter partial name")
        for i in lop:
            if s not in str(i.keys()):
                kep.remove(i)
        print(f"matching found {kep}") if len(kep)!=0 else print("Not found")
    elif a==4:
        s=input("enter email or phone number ")
        find('phno',s) if s.isdigit() else find('email',s)
    elif a==5:
        f.close()
        with open('addressbook.txt','w') as f:
            for i in lop:
                l.append(i)
                f.write(str(l)+'\n')
                l=[]
        break
        
