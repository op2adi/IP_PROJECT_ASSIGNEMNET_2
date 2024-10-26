menu,amt,c,d= [("Samosa", 15), ("Idli", 30), ("Maggie", 50), ("Dosa", 70), ("Tea", 10), ("Coffee", 20), ("Sandwich", 35), ("ColdDrink", 25),("Paty",20),("Chole Bhature",40)],0,[],''
print(menu)
while True:
    a=list(map(int,input('enter item no. then quantity').split()))
    if a!=[]:
        amt+=((menu[int(a[0])-1][1])*int(a[1]))
        c.append([menu[int(a[0])-1][0],',',a[1],',',"Rs ",((menu[int(a[0])-1][1])*int(a[1]))])
    else:
        for i in c:
            for j in i:
                print(j,end='')
            print(d)
        print('\n')
        print(f"total amount is {amt}" )
        break