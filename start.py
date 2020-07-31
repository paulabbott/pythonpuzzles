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
        print('yes, you cracked the password ' + str(index) + ' it was ' + input)
        exit()
# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

# passwords 9-14 
# 9 - 5 chars, all lowercase or space
# 10 - 6 chars, all lowercase or space (took awhile to run)
# 11 - 5 lowercase letters
# 12 - (part 1) 5 lowercase letters
# 13 - (part 2) 3 lowercase letters
# 14 - Upper and lowercase and spaces, 10 charaters. (YOU might just have to guess this one)
# your code goes here:

print("done")
exit()  

# ... there should be a bunch more puzzels here to lead upto the harder passwords

# password 8
# 4 chars, any of lowercase o,p,s (bounus points for not using 4 nested loops)
# your code goes here:

print("done")
exit()  

# password 7
# 3 charaters could be any combination of upper and lowercase letters and a space
# your code goes here:

print("done")
exit()  

# password 6
# note2self: this should check the non recursive version.
check(6,'xo')
exit()

# password 5 - two lowercase colours of the rainbow not seperated by a space
# hint: you could use two for loops one inside the other
# your code goes here:

print("done")
exit()  

# password 4 - lowercase colour of the rainbow
# hint: google 'python loop through list'
# your code goes here:

print("done")
exit()  

# password 3 - 1 uppercase or lowercase letter A-Z and a-z
# (note2self: might be better to force the player to concat arrays here rather than just two independent loops)
# your code goes here:

print("done")
exit()  

# password 2 - 1 single uppercase letter between A-Z (these are not very good passwords)
# hints: things to google python chr, ascii table
# your code goes here:

print("done")
exit()  

# password 1
# another 4 digit pin but might have leading zero, ie you will need to test 0123 not just 123
# your code goes here:

print("done")
exit()  

# password 0 (lists start from zero in programming)
# password is 4 digit pin code, remember your testing strings not numbers.
# let learn how to turn numbers into strings
for i in range(9999):    
    s = str(i)
    print("is the password " + s)
    check(0,s)   
print("done")
exit()     