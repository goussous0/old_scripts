from itertools import combinations

def permutations_fun(usr_str , k ):
    tmp = []
    #tmp = list(combinations(list(usr_str), i))
    for i in range (1, k+1):
        tmp_lst = sorted(list(combinations(usr_str,i)))
        for item in (tmp_lst):
            tmp.append(item)
    

    for item in tmp:
        output = ""
        for Item in item:
            output += Item
        print (output)






if __name__ == '__main__':
    usr_input = input().split()
    usr_str = usr_input[0]
    k = int(usr_input[1])
    permutations_fun(usr_str, k )
