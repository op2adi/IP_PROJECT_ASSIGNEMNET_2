a,c=['Abuse', 'Adult', 'Agent', 'Anger', 'Apple', 'Award', 'Basis', 'Beach', 'Birth', 'Block', 'Blood', 'Board', 'Brain', 'Bread', 'Break', 'Brown', 'Buyer', 'Cause', 'Chain', 'Chair', 'Chest', 'Chief', 'Child', 'China', 'Claim', 'Class', 'Clock', 'Coach', 'Coast', 'Court', 'Cover', 'Cream', 'Crime', 'Cross', 'Crowd', 'Crown', 'Cycle', 'Dance', 'Death', 'Depth', 'Doubt', 'Draft', 'Drama', 'Dream', 'Dress', 'Drink', 'Drive', 'Earth', 'Enemy', 'Entry', 'Error', 'Event', 'Faith', 'Fault', 'Field', 'Fight', 'Final', 'Floor', 'Focus', 'Force', 'Frame', 'Frank', 'Front', 'Fruit', 'Glass', 'Grant', 'Grass',
 'Green', 'Group', 'Guide', 'Heart', 'Henry', 'Horse', 'Hotel', 'House', 'Image', 'Index', 'Input', 'Issue', 'Japan', 'Jones', 'Judge', 'Knife', 'Laura', 'Layer', 'Level', 'Lewis', 'Light', 'Limit', 'Lunch', 'Major', 'March', 'Match', 'Metal', 'Model', 'Money', 'Month', 'Motor', 'Mouth', 'Music', 'Night', 'Noise', 'North', 'Novel', 'Nurse', 'Offer', 'Order', 'Other', 'Owner', 'Panel', 'Paper', 'Party', 'Peace', 'Peter', 'Phase', 'Phone', 'Piece', 'Pilot', 'Pitch', 'Place', 'Plane', 'Plant', 'Plate', 'Point', 'Pound', 'Power', 'Press', 'Price', 'Pride', 'Prize', 'Proof', 'Queen', 'Radio', 'Range',
 'Ratio', 'Reply', 'Right', 'River', 'Round', 'Route', 'Rugby', 'Scale', 'Scene', 'Scope'],[]
import random
import requests
for i in a:
    c.append(i.lower())
a,jh=list(c),[]
del c
b=random.randint(0,len(a)-1)
c,ty=a[b],5
print(c)
while ty>0:
    print(f'Number of tries left {ty}')
    count=0
    p=input("enter 5 letter word ")
    resp=requests.get(f'https://api.dictionaryapi.dev/api/v2/entries/en/{p}')
    if resp.status_code==200:
        q=list(p)
        if len(p)!=5:
            print("Length is not 5")
            continue
        else:
            for j in range(5):
                if p[j]==c[j]:
                    count+=1
                else:
                    q[j]='-'
            if count==5:
                print("You found the word")
                break
            else:
                print("you guessed some words",''.join(q))
                for k in range(len(list(p))):
                    if list(p)[k] in c and list(c)[k]==list(p)[k]:
                        continue
                    elif list(p)[k] in c:
                        jh.append(list(p)[k])
                print(jh) if jh!=[] else print('')
                jh=[]
                print('present in the list but order is wrong')
            ty-=1
    else:
        print("Sorry Word not exist!!!")

