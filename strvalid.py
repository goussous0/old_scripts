def validate_str(s):
    str_lst = list(s)
    count = 0
    result = [None,None,None,None,None]
    for item in str_lst:
        if result[0]==None or result[0]==False:
            result[0]= item.isalnum()
        if result[1]==None or result[1]==False:
            result[1]= item.isalpha()
        if result[2]==None or result[2]==False:
            result[2]= item.isdigit()
        if result[3]==None or result[3]==False:
            result[3]= item.islower()
        if result[4]==None or result[4]==False:
            result[4]= item.isupper()





   # result[0]= s.isalnum()
   # result[1] = s.isalpha()
   # result[2] = s.isdigit()
   # result[3] = s.islower()
   # result[4] = s.isupper()
    for item in result:
        print (item)
    return


if __name__ == '__main__':
    s = input()
    validate_str(s)

