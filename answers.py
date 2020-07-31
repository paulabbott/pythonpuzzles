hashes = [659471584116336832,
 -3495090546375936701,
 11520034651,
 15360046201,
 2046744907087422980,
 -4392774335228555657,
 15360092280138501,
 -8251564009657796216,
 -11898355873423883,
 3052910072140387471,
 -6477545829442136474,
 -3159372328817883329,
 -522747127365073322,
 -1925086808195474851,
 5432214084380532074
 ]

#remember to update the index for the password you are trying to crack
def check(index,input):
    if hash(input) == hashes[index]:
        print('yes, you cracked the password it was ' + input)
        exit()
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# passwords n+2
# hashing is expensive, could do that once and save to a file. 
# could also then sort hashes and binary search.

# passwords n+1
# recursission is cleaver but also pretty stupid optimisation wise. 

# passwords 9,10,11 (ok you might just have to guess these)
# 9 - 5 chars, all lowercase or space
# 10 - 6 chars, all lowercase or space
# 11 - 10 char, upper and lower and a space. you!
def checkem(v):
    #need to add a statment to exit if out of bounds, all recursion has to stop somewhere
    if (v >= len(ts)):
        exit()
    if ts[v] >= len(posChar)-1:
        ts[v] = 0
        checkem(v+1)
    else:
        ts[v] = ts[v] + 1  
posChar = []
# for i in range(65,68): #uppercase goes from 65 to 90
#     posChar.append(chr(i))
for i in range(97,123): #lowercase goes from 97 to 122
    posChar.append(chr(i))
posChar.append(' ')    
print('posChar=',posChar)

ts = []
#init with the known length of the password
for z in range(0,5):
    ts.append(0)
combinations = pow(len(posChar),len(ts))    
print(posChar)
print(ts)
print(combinations)

for k in range(0,combinations):
    if(k%100000 == 0):
        print(str(100*k/combinations)+'%')
    # print(ts)     
    temp = ""
    for i in ts:
        temp = temp + (posChar[i])
    # print('try '+temp)
    check(9,temp)
    checkem(0)
print('done')
exit()

# password ... there should be a bunch more puzzels here to lead upto the harder passwords

# password 8
# 4 chars, any of lowercase o,p,s (bounus points for not using 4 nested loops)
def checkem2(v):
    #need to add a statment to exit if out of bounds, all recursion has to stop somewhere
    if (v >= len(ts)):
        exit()
    if ts[v] >= len(posChar)-1:
        ts[v] = 0
        checkem(v+1)
    else:
        ts[v] = ts[v] + 1  
posChar = ['o','p','s']
ts = [0,0,0,0]
combinations = pow(len(posChar),len(ts))

for k in range(0,combinations):
    # print(ts)     
    temp = ""
    for i in ts:
        temp = temp + (posChar[i])
    print('try '+temp)
    check(8,temp)
    checkem(0)
print("done")
exit()

# password 7
# 3 charaters could be any combination of upper and lowercase letters and a space
posChar = []
for i in range(65,91): #goes from 65 to 90
    posChar.append(chr(i))
for i in range(97,123): #goes from 97 to 122
    posChar.append(chr(i))
posChar.append(' ')    
print('posChar=',posChar)

for c1 in posChar:
    for c2 in posChar:    
        for c3 in posChar:
            c123 = c1 + c2 + c3
            # print('try ' + c123)        
            check(7,c123)
print("done")
exit()

# password 6
# note2self: what to do just remove this.
check(6,'xo')
exit()

# password 5 - two lowercase colours of the rainbow not seperated by a space
# hint: you could use two for loops one inside the other
colours = ["red","orange","yellow","green","blue","indigo","violet"]
for colour1 in colours:
    for colour2 in colours:    
        twoColours = colour1 + colour2
        print('try ' + twoColours)        
        check(5,twoColours)
print("done")
exit()

# password 4 - lowercase colour of the rainbow
# hint: google 'python loop through list'
colours = ["red","orange","yellow","green","blue","indigo","violet"]
for i in colours:
    print('try ' + i)        
    check(4,i)
print("done")
exit()

# password 3 - 1 uppercase or lowercase letter A-Z and a-z
# (note2self: might be better to force the player to concat arrays here rather than just two independent loops)
for i in range(65,91): #goes from 65 to 90
    #print(i,chr(i))
    s = chr(i)
    print('try ' + s)        
    check(3,s)
for i in range(97,123): #goes from 97 to 122
    #print(i,chr(i))
    s = chr(i)
    print('try ' + s)        
    check(3,s)    
print("done")
exit()


# password 2 - 1 single uppercase letter between A-Z (these are not very good passwords)
# hints: things to google python chr, ascii table
for i in range(65,91): #goes from 65 to 90
    #print(i,chr(i))
    s = chr(i)
    print('try ' + s)        
    check(2,s)
print("done")
exit()


# password 1
# another 4 digit pin but might have leading zero, ie you will need to test 0123 not just 123
for i in range(1000):    
    s = str(i)
    # how long is the string
    padding = 4 - len(s)
    for p in range(padding):
        s = '0' + s 
    print('try ' + s)        
    check(1,s)
print("done.")
exit()    

# password 0 (lists start from zero in programming)
# password is 4 digit pin code, remember your testing strings not numbers.
# let learn how to turn numbers into strings
for i in range(9999):    
    s = str(i)
    print("is the password " + s)
    check(0,s)    