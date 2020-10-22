

string = "BANANA"

#for i in range (len(string)+1):
#    print (string[i:i+1])


for i in range (len(string)+1):
    print (string[i:i+1])
    for j in range (len(string)+1):
        print (string[j:i])
