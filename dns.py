from collections import deque
#one round DES encrypt

hexKey = "0 1 2 3 4 5 6 7 8 9 A B C D E F"

bitVal = "0000 0001 0010 0011 0100 0101 0110 0111 1000 1001 1010 1011 1100 1101 1110 1111"

reHexKey = hexKey.replace(" ", "")
rebitVal = bitVal.replace(" ","")

randomKey1 = "0001001100110100010101110111100110011011101111001101111111110001"
randomKey = "1011011100011110110101010101100010110010110001001001100011100110"
randomHex = "B71ED558B2C498E6"

PC1 =[57,   49 ,   41 ,  33 ,   25  ,  17 ,   9, 
            1 ,  58  ,  50 ,  42 ,   34,    26,  18,
              10 ,   2  ,  59 ,  51 ,   43  ,  35,   27,
              19,   11   ,  3  , 60   , 52   , 44  , 36,
              63  , 55  ,  47  , 39 ,   31 ,   23 ,  15,
               7  , 62 ,   54 ,  46  ,  38  ,  30 ,  22,
              14 ,   6 ,   61  , 53   , 45  ,  37 ,  29,
              21 ,  13    , 5  , 28  ,  20  ,  12 ,   4]

PC2 =[14 ,   17 ,  11  ,  24  ,   1  ,  5,
                  3,    28 ,  15  ,   6  ,  21 ,  10,
                 23 ,   19 ,  12 ,    4   , 26  ,  8,
                 16,     7 ,  27 ,   20 ,   13,    2,
                 41  ,  52 ,  31  ,  37  ,  47 ,  55,
                 30  ,  40,   51   , 45   , 33 ,  48,
                 44  ,  49,   39  ,  56  ,  34 ,  53,
                 46  ,  42 ,  50 ,   36 ,   29 ,  32 ]

IP = [58  ,  50  , 42   , 34  ,  26 ,  18   , 10  ,  2,
            60  ,  52 ,  44 ,   36  ,  28  , 20 ,   12 ,   4,
            62  ,  54  , 46  ,  38  ,  30 ,  22 ,   14 ,   6,
            64 ,   56 ,  48  ,  40  ,  32   ,24  ,  16 ,   8,
            57   , 49  , 41  ,  33 ,   25  , 17  ,   9  ,  1,
            59,    51 ,  43  ,  35  ,  27  , 19 ,   11,    3,
            61  ,  53 ,  45   , 37   , 29 ,  21 ,   13,   5,
            63  ,  55  , 47  ,  39  ,  31  , 23  ,  15 ,   7]

EBIT = [ 32 ,    1  ,  2  ,   3  ,   4   , 5,
                  4 ,    5  ,  6  ,   7  ,   8 ,   9,
                  8  ,   9  , 10 ,   11  ,  12 ,  13,
                 12 ,   13  , 14 ,   15  ,  16 ,  17,
                 16  ,  17 ,  18  ,  19 ,   20,  21,
                 20  ,  21 ,  22   , 23  ,  24,   25,
                 24  ,  25 ,  26 ,  27    ,28  , 29,
                 28  ,  29 ,  30  ,  31 ,   32 ,   1]

#a)
#this prints the original key
print(randomKey)
K_1 = ""
for i in range(len(PC1)):
    K_1 = K_1 + randomKey[PC1[i]-1]

C_1 = K_1[0:len(K_1)/2]
D_1 = K_1[len(K_1)/2:len(K_1)]

#this prints out the key only after PC-1 applied to it
print(K_1)
#then shift the bits to the left and first bit goes to back
# of left and right by them selfs 


items1 = deque(C_1)
items1.rotate(-1)
items2= deque(D_1)
items2.rotate(-1)

C_1shifted=""
D_1shifted=""
for i in range(len(items1)):
    C_1shifted = C_1shifted + items1[i]
    D_1shifted = D_1shifted + items2[i]

combinedKey = C_1shifted+D_1shifted
print(combinedKey)
K_1 =""

for i in range(len(PC2)):
   
    K_1 = K_1 + combinedKey[PC2[i]-1]

#this prints out the key after the shift and after the PC-2 applied to it
print(K_1)


#b)

#to get the R_0 and L_0 we need to apply the inital permutation on the original key that we got 
K_0 = ""
for i in range(len(IP)):
    K_0 = K_0 + rebitVal[IP[i]-1]
#print(rebitVal)
#print(K_0)
L0 = K_0[0:len(K_0)/2]
R0 = K_0[len(K_0)/2:len(K_0)]
#print(L0)
print(R0 + " this is R0")


#c) 
#calculate E[R_0] using EBIT
ER0 = ""
for i in range(len(EBIT)):
    ER0 = ER0 + R0[EBIT[i]-1]
print(ER0)

#d)
A = ""
for i in range(len(ER0)):
    A = A + str(int(ER0[i])^int(K_1[i]))
print(A)

#e)

S = list()

for i in range(1,len(A)+1):
    if i%6 == 0:
        S.append(A[i-6:i])
print(S)

middlebits = ["0000",	"0001",	"0010",	"0011",	"0100"	,"0101",	"0110",	"0111",	"1000",	'1001'	,'1010',	'1011',	'1100',	'1101',	'1110',	'1111']
middle01 = ['1110',	'1011',	'0010',	'1100',	'0100'	,'0111',	'1101'	,'0001'	,'0101'	,'0000'	,'1111'	,'1010',	'0011',	'1001',	'1000','0110']
dict00 = {"0000":"0010",
"0001":"1100",
"0010":"0100",
"0011":"0001",
"0100":"0111",
"0101":"1010",
"0110":"1011",
"0111":"1000",
"1000":"1000",
"1001":"0101",
"1010":"0011",
"1011":"1111",
"1100":"1101",
"1101":"0000",
"1110":"1110",
"1111":"1001"}

dict01 = {}
dict10 = {}
dict11 = {}
#	1100	1101	1110	1111
#	1101	0000	1110	1001
for i in range(len(S)):
    
    startval = S[i][0]
    endval = S[i][len(S[i])-1]
   # print(startval)
   # print(endval)
    #if str(startval)+str(endval) == "00":
       # print("helo1")
    #elif str(startval)+str(endval) == "01":
       # print("helo2")
   # elif str(startval)+str(endval) == "10":
       # print("helo3")
   # elif str(startval)+str(endval) == "11":
       # print("helo4")

B = "10001000011110000111000101010100"

P = [ 16 ,  7,  20,  21,
     29,  12 , 28,  17,
     1 , 15,  23, 26,
     5 , 18,  31 , 10,
     2 ,  8 , 24 , 14,
    32,  27  , 3 ,  9,
    19 , 13 , 30 ,  6,
    22 , 11 ,  4,  25]
pOfB = ""
for i in range(len(P)):
    pOfB = pOfB + B[P[i]-1]
#print(B)
print(L0)
print(pOfB)
R1 = ""
for i in range(len(pOfB)):
    R1 = R1 + str(int(pOfB[i])^int(L0[i]))
print(R1 + " This is R1")