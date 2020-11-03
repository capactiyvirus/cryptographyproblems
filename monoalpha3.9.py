# problem 3.9

#    KXJEY UREBE ZWEHE WRYTU HEYFS
#    KREHE GOYFI WTTTU OLKSY CAJPO
#    BOTEI ZONTX BYBNT GONEY CUZWR
#    GDSON SXBOU YWRHE BAAHY USEDQ

# key =  royal new zealand navy
# Translate TT into tt.

alphabet = "abcdefghiklmnopqrstuvwxyz"
key = "royal new zealand navy"

cipher = [["KXJEY","UREBE", "ZWEHE" ,"WRYTU" ,"HEYFS"], 
        ["KREHE", "GOYFI", "WTTTU", "OLKSY", "CAJPO"],
        ['BOTEI', 'ZONTX', 'BYBNT', 'GONEY', 'CUZWR'],
        ['GDSON', 'SXBOU', 'YWRHE', 'BAAHY', 'USEDQ']]


cipher1 = "KXJEY UREBE ZWEHE WRYTU HEYFS KREHE GOYFI WTTTU OLKSY CAJPO BOTEI ZONTX BYBNT GONEY CUZWR GDSON SXBOU YWRHE BAAHY USEDQ"
reCipher1 = cipher1.replace(" ","").lower()


keyArray = [[],[],[],[],[]]
reKey = key.replace(" ","")
print(reKey)
m, n = 0,0
tracker = list()
for i in range(25): 
    #print(reKey[i])
    if m == 5:
        m=0
        n+=1
    m+=1
    if i < len(reKey):
        if reKey[i] not in tracker:
            tracker.append(reKey[i])
            #print(tracker)
            keyArray[n].append(reKey[i])
        else:
            for i in range(len(alphabet)):
                if alphabet[i] not in tracker:
                    tracker.append(alphabet[i])
                    keyArray[n].append(alphabet[i])
                    alphabet = alphabet[i:]
                    break
    else:
        for i in range(len(alphabet)):
                if alphabet[i] not in tracker:
                    tracker.append(alphabet[i])
                    keyArray[n].append(alphabet[i])
                    alphabet = alphabet[i:]
                    break
print(keyArray)
#print(alphabet)
a,b = 0,0
d,c = 0,0

for i in range(0,len(reCipher1)-1,2):
    char1 = reCipher1[i]
    char2 = reCipher1[i+1]
    print(char1 + " 1")
    print(char2 + " 2")
    for j in range(len(keyArray)-1):
       
        if char1 in keyArray[j]:
           # print(char1 + "1")
            a,b = i%5,j%5
            #print(a)
            #print(b)

        if char2 in keyArray[j]:
           # print(char2 + "2")
            c,d = i%5,j%5
            #print(c)
            #print(d)
        if a == c:
            holder = [keyArray[a][b],keyArray[c][d]]
            z = b
            y = d
            for m in range(4):
                if z < 0:
                    z = 4
                if z == 0:
                    keyArray[a][0] = keyArray[a][4]
                else:
                    print(keyArray[a][z-1])
                    keyArray[a][z] = keyArray[a][z-1]
                    
                z-=1

   # print(reCipher1[i:i+2])



print(keyArray[2][3] + keyArray[3][4])
print(keyArray[2][4] + keyArray[3][3])

print(keyArray)

#[y][x]  if yy then move both right 
# if xx then move down
# if xy then change take yx 

