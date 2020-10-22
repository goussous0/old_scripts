from itertools import product

def gen_sets(set1, set2):
    x1 = len(set1)
    y1 = len(set2)
    tmp_lst = []
    for item in set1:
        x = set1.index(item)
        set1[x]=int(item)

    for item in set2:
        x = set2.index(item)
        set2[x]=int(item)

    ## reverse the places of the set1 and set2 to get the right result 
    ## output should be as a tuple not as a list
    
    for i in range (y1):
        tmp_lst.append(set2[i])
    tmp =list(product(set1,tmp_lst))
    for item in tmp:
        print (item, end=" ")
    return 



if __name__ == '__main__':
    set1 = input().split()
    set2 = input().split()
    gen_sets(set1, set2)
    
