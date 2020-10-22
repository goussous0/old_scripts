from itertools import permutations

def permutations_fun(usr_str , k ):
    y1 = len(usr_str)
    tmp =list(permutations(usr_str,k))
    tmp = sorted(tmp)


    for item in tmp:
        output = ""
        for Item in item:
            output += Item
        print (output)
    pass





if __name__ == '__main__':
    usr_input = input().split()
    usr_str = usr_input[0]
    k = int(usr_input[1])
    permutations_fun(usr_str, k )