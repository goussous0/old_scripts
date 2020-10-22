import textwrap

def wrap(string, max_width):
    wrp_lst = textwrap.wrap(string, max_width)
    x = len(wrp_lst)-1
    for item in wrp_lst:
        if item==wrp_lst[x]:
            return item
        else:
            print (item)


if __name__ == '__main__':
    string, max_width = input(), int(input())
    result = wrap(string, max_width)
    print(result)