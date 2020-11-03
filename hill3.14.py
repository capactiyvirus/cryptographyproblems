import numpy as np


alphabet = "abcdefghijklmnopqrstuvwxyz"
plaintext = "meet me at the usual place at ten rather then eight o clock"
val = list()
rePlain = plaintext.replace(" ","").lower()
if len(rePlain)%2 != 0:
    rePlain=rePlain+"x"
for i in range(len(rePlain)):
    #print(rePlain[i] + " pl") 
    for j in range(len(alphabet)):
        
        if rePlain[i] == alphabet[j]:
            val.append(j)
            #print(val)
            
            break
    
value = "12 4 4 19 12 4 0 19 19 7 4 20 18 20 0 11 15 11 0 2 4 0 19 19 4 13 17 0 19 7 4 17 19 7 4 13 4 8 6 7 19 14 2 11 14 2 10"
#reValue = value.replace(" ","")
#for i in range(len(val)):
   # if reValue[i] != val[i]:
      #  print(reValue[i])
      #  print(val[i])

#print(reValue)
print(val)
#print(len(val))

key = np.array([[7,2],[3,5]])
key1 = np.array([[7],[3]])
Cipher = ""
for i in range(0,len(val),2):
    if i+1< len(val):
        
        B = np.array([val[i],val[i+1]])
        #print(B)
        C = key.dot(B)
        C = C%26
        Cipher = Cipher + alphabet[C[0]]
        Cipher = Cipher + alphabet[C[1]]
    else:
        B = np.array([val[i]])
        C = key1.dot(B)
        C = C%26
        Cipher = Cipher + alphabet[C[0]]

   
#print(C)
print(Cipher.upper())

inverseKey = np.array([[19,8],[25,11]])
inverseKey1 = np.array([[19],[25]])
newVal = list()
newPlain = ""
for i in range(len(Cipher)):
    #print(rePlain[i] + " pl") 
    for j in range(len(alphabet)):
        
        if Cipher[i] == alphabet[j]:
            newVal.append(j)
            #print(val)
            
            break
print(newVal)

for i in range(0,len(newVal),2):
    if i+1< len(val):
        
        B = np.array([newVal[i],newVal[i+1]])
        #print(B)
        C = inverseKey.dot(B)
        
        C = C%26
        newPlain = newPlain + alphabet[C[0]]
        newPlain = newPlain + alphabet[C[1]]
    else:
        B = np.array([newVal[i]])
        C = inverseKey1.dot(B)
        C = C%26
        newPlain = newPlain + alphabet[C[0]]

print(newPlain)


