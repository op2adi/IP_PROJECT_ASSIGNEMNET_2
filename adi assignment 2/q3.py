d,e,po,g={},[],[],[]
with open("yearbook.txt","r") as f:
    a=int((len(f.readlines()))**(0.5))
    f.seek(0,0)
    for i in range(a):
        for j in range(a):
            b=f.readline()
            if ":" == b[-2]:
                c=b[:-2:]
            else:
                e.append(int(b[-2]))
        d[c]=sum(e)
        e=[]
maximum,minimum=max(list(d.values())),min(list(d.values()))
for i in list(d.keys()):e.append(i) if d[i]==maximum else po.append(i) if d[i]==minimum else g.append(3)
print(f"Max signatures are of {e}")
print(f"Minimum signatures are of {po}")