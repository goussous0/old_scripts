

string = "BANANA"

vowels = ['A','E','I','O','U']
str_lst = list(string)
    ## the player that searchs for vowel begining substring Kevin
p1_substr = []
sub_str = []

for item in str_lst:
    if [letter for letter in vowels if letter == item in vowels ]:
        p1_substr.append(str_lst.index(item))


for item in p1_substr:
    for i in range (len(string)+1):
        word = (string[item:i])
        if word == "":
            pass
        else:
            sub_str.append(word)
for item in sub_str:
    print (item)


#for item in p1_substr:
#    x = len (string[item:])+1
#    for i in range (x):
#        print (string[item:i+1] + "<-----")
