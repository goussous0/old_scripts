#In this challenge, the user enters a string and a substring. You have to print the number of times that the substring occurs in the given string.
#String traversal will take place from left to right, not from right to left.

# Find a string

#t3xt = str(input())
#search = str(input())


# a search function the finds the gmail search word in a give txt file
# or without txt file it ou know a little nit of programing
#hacker rank find a string
## weedcookie
## 12/05/2019
## 4:30



def search_t3xt(t3xt, search):
    x = int(len(t3xt))
    y = int(len(search))
    count = 0
    for i in range (x):
        #print (t3xt[i:x])
        #print (t3xt[i:i+4])
        #if t3xt[i:x]== search:
         #   print (item)
        if t3xt[i:i+y]==search:
            print (t3xt)
            #print (t3xt[i-y:i+2*y])
            print (search)
            count +=1 
        else:
            pass
            #print ("Done")

#search_t3xt(t3xt, search)



handle  = open("l0gs.txt", "r")
strings = handle.readlines()
for line in strings:
    #print (str(line))
    mail = (line.split())
    try:
        t3xt= mail[0]
    except IndexError:
        break
    search = "gmail"
    #print (t3xt)
    #print (t3xt+" "+ search)
    search_t3xt(t3xt, search)
