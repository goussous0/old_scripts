def mutate_string(s, i, c):
    s_lst = list(s)
    s_lst[i]=c
    s_lst = ''.join(s_lst)
    return s_lst


if __name__ =="__main__":
    s = input()
    i, c =input().split()
    s_new = mutate_string(s, int(i), c)
    print (s_new)