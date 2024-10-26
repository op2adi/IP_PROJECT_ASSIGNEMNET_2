def scaling(cx,cz,k):
    for i in range(len(k)):
        k[i][0]*=cx
        k[i][1]*=cy
def printbeforescaling(k):
    j=[tuple(i)+(1,) for i in k]
    print(f'{j} {str(n)}X{str(3)}')
k,cx,cy=eval(open("q5.txt").read()),float(input("enter scaling for 1st column")),float(input("Enter scaling for 2nd column"))
n=len(k)
k=[list(i) for i in k]
printbeforescaling(k),scaling(cx,cy,k)
k=[tuple(i) for i in k],[print(tuple(i)) for i in k]