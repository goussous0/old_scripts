def count_substring(string, sub_string):
    x,y  = len(string),len(sub_string)
    occur_lst = []
    for i in range (x):
        if (string[i:i+y])==sub_string:
            occur_lst.append(string)
    return len(occur_lst)


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)