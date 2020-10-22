def print_rangoli(size):
    width = ((size-1)*4)+1
    strings = "abcdefghijklmnopqrstuvwxyz"
    # your code goes here
    x = len(strings)
    sub_str = list(strings[:size])
    sub_str = sub_str[::-1]
    #print (sub_str)
    all_lst = []
    for i in range (size):
        tmp_lst = []
        for k in range (i+1):
            tmp_lst.append(sub_str[k])
        #print (tmp_lst)
        sub_tmp = tmp_lst[::-1]
        #print (sub_tmp[1:])
        tmp_lst = tmp_lst+sub_tmp[1:]
        #print (tmp_lst)



        res = ""
        for item in tmp_lst:
            res += item +"-"
        n = len(res)
        res = res[:n-1]
        #print (res)

        all_lst.append(res)
        rev_lst = all_lst[::-1]
        del(rev_lst[0])
    for item in all_lst:
        item = str(item)
        print (item.center(width, "-"))
    for item in rev_lst:
        item = str(item)
        print (item.center(width,"-"))






if __name__ == '__main__':
    n = int(input())
    print_rangoli(n)