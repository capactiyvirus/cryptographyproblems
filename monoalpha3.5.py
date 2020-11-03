alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
key = 'The snow lay thick on the steps and the snowflakes driven by the wind looked black in the headlights of the cars'
reKey = key.replace(" ","").upper()

print(reKey)
uniqueKey = list()
for i in range(len(reKey)):
    if reKey[i] not in uniqueKey:
        uniqueKey.append(reKey[i])
#print(uniqueKey)

cipher = 'SIDKHKDM AF HCRKIABIE SHIMC KD LFEAILA'
reCipher=cipher.replace(" ","")

b = dict()

for i in range(len(uniqueKey)):
    b[alphabet[i]] = uniqueKey[i]
print(b)
plaintext = ""
for i in range(len(cipher)):
    if b.get(cipher[i]) is None:
        plaintext = plaintext + " "
    else:
        plaintext = plaintext + str(b.get(cipher[i]))
print(plaintext)